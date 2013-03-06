django-py2app-demo
==================

An example of a Django py2app bundle. 

Roughly based off of a few examples I found online, including
+ http://misunderstandings.wordpress.com/2008/06/26/django-desktop-app/
+ http://en.usenet.digipedia.org/thread/15865/5178/
+ https://bitbucket.org/Lawouach/cherrypy-recipes/src/9c35b4b62ef1/frameworks/django_?at=default
and a few others. 

At the moment, I think it does not work if you double-click the application to
launch it. Instead, I would recommend opening it via command line:

    open dist/demosite.app/Contents/MacOS/demosite

I did solve this in production, but I cannot remember how exactly. I believe I did it
by using django-supervisor.
