"""
WSGI config for sidu-help project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os.path, sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

def myAppl(environ, start_response):
    global myMessage
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Wartungsdienst - maintenance service!\n", myMessage + "\n"]

cdir = os.getcwd()
myMessage = "chdir: " + cdir
sys.path.insert(0, cdir)
sys.path.insert(1, "/usr/share/sidu-base")
sys.path.insert(2, "/usr/share/sidu-base/djinn")
sys.path.insert(3, "/usr/share/pyygle")
#myMessage += "\nsys.path extended:" + "\n".join(sys.path)
import manual.settings 

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.

from manual.urls import getPatterns
urlpatterns = getPatterns()
from mdjinn.wsgihandler import WSGIHandler
application = WSGIHandler(urlpatterns)
#application = myAppl
