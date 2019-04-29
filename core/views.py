from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import ToDoItem
from .serializers import ToDoItemSerializer
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = ToDoItem.objects.all().order_by('-created_at')
    serializer_class = ToDoItemSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        async_to_sync(channel_layer.group_send)(
            'index',
            {'type': 'chat_message',
             'message': "do_update",
             }
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_id = instance.id
        if instance_id == 1:
            return Response(data={'id': instance_id}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            async_to_sync(channel_layer.group_send)(
                'index',
                {'type': 'chat_message',
                 'message': "do_update",
                 }
            )
            self.perform_destroy(instance)
        return Response(data={'id': instance_id}, status=status.HTTP_200_OK)

