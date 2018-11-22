from django.shortcuts import render, render_to_response

def app_one(request):
    return render_to_response('app/app.html')