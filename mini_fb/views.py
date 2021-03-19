from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import time

def homePageView(request):
    '''Respond to an Http request with a simple web page.'''

    response_html = ''' 
    <html>
    <h1>Hello,world!</h1>
    <p>
    This is our first Django web application!
    </p>
    <hr>
    this page was generated at %s.
    </html>
    '''% time.ctime()
    return HttpResponse(response_html)
