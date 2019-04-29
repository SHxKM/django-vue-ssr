# Django Nuxt SSR
### TL;DR

A simple to-do app built with Django REST framework, Nuxt.js, and Tailwind.

### About 

Django To Do With Vue v2 is an expirement in utilizing technologies and practices in web development that I haven't used before.

This project is over-engineered on the one hand, and not really production-ready on the other (you can help with that). My goal wasn't to build a todo app per se, but to expirement with all the "cutting-edge" stuff out there.

It can serve as a general template, but is not to be relied upon to utilize best practices in produciton.

### Stack

This web-app is built as a Vue SSR app, which means some of the content is rendered server-side in order to avoid SEO penalties.

The backend is built in Python with Django and the Django REST framework.

The frontend is where it gets more interesting. Unlike its v1 counterpart written purely in Vue, v2 isn't an SPA, and it utilizes the `Nuxt.js` framework to make life a little easier. A `Vuex` store handles state management, and the young but wonderful `Tailwind` is used as a CSS framekwork.


### Heroku

At least at the time this repo was made public, deployment to Heroku was not exactly a breeze. 

Attempts to push the entire repo as a single app [had failed](https://github.com/SHxKM/django-vue-ssr/issues/3), 
and I'm currently pushing the same source-code to two Heroku apps, and setting the `web:` Procfile directive 
dynamically using environment variables.

It certainly can be argued that *this is how it's supposed to work*, and this single repo structure does make 
things a little more involved. Some would say this project should really be two repos (backend and frontend),
 but I am determined to look for ways to ship this is a single Heroku app, if only for education-purposes.

See the [Procfile](https://github.com/SHxKM/django-vue-ssr/blob/master/Procfile), which utilizes environment variables to
 decide which `web:` command to run.

#### Procfile-related envs for `backend`:

`WEB_PREFIX`: `cd api`

`WEB`: `gunicorn api.wsgi`

#### Procfile-related envs for `frontend`:

`WEB`: `npm run start`