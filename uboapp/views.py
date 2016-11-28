from django.shortcuts import render
from .models import Building, Comment
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth import authenticate, login

import json

# Create your views here.

def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'uboapp/building_list.html', {'buildings': buildings})




def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        comment = Comment(text=post_text, building=Building.objects.get(streetname="UBO"))
        comment.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = comment.pk
        response_data['text'] = comment.text
        response_data['created'] = comment.created.strftime('%B %d, %Y %I:%M %p')

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )