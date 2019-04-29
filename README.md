## Django Nuxt SSR (backend repo)

The frontend repo can be found [here](https://github.com/SHxKM/django-nuxt-ssr-front).

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

After many failed attempts to deploy the codebase as a single repository, I've
 finally came to the conclusion that it's not only wrong, but also quite cumbersome.