from django.shortcuts import render
from .models import Building, Comment, Rating
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth import authenticate, login
from ipware.ip import get_ip
from django.db.models import Avg

import json

# Create your views here.

def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'uboapp/building_list.html', {'buildings': buildings})


def post_rating(request):
    if request.method == 'POST':
        post_rate = request.POST.get('the_post')
        active_building = request.POST.get('active_building')

        response_data = {}

        ip = get_ip(request)

        rating = Rating(rate=post_rate, client_ip=ip, building=Building.objects.get(id=active_building))
        rating.save()

        response_data['result'] = 'Post Rating successful!'
        response_data['postpk'] = rating.pk
        response_data['rate'] = rating.rate
        response_data['created'] = rating.created.strftime('%B %d, %Y %I:%M %p')

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )




def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        comment = Comment(text=post_text, building=Building.objects.get(streetname="BERRY STREET"))
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


def get_building(request):
    if request.method == 'GET':
        get_id = request.GET.get('the_post')
        response_data = {}

        building = Building.objects.get(id=get_id)

        response_data['result'] = 'Get successful!'
        response_data['postpk'] = building.pk
        response_data['streetname'] = building.streetname
        response_data['streetnumber'] = building.streetnumber

        response_data['building_class'] = building.building_class
        response_data['year_built'] = building.yearbuilt

        response_data['stories'] = building.stories
        response_data['res_units'] = building.res_units

        response_data['com_units'] = building.com_units
        response_data['structure_type'] = building.structure_type

        response_data['grade'] = building.grade
        response_data['construction_type'] = building.construction_type

        response_data['area'] = building.area
        response_data['lotsize'] = building.lotsize

        response_data['marketvalue'] = building.marketvalue

        response_data['ratings_count'] = Rating.objects.filter(building=building.pk).count()
        b = Rating.objects.filter(building=building.pk)
        response_data['ratings_rate'] = b.aggregate(Avg('rate'))

        response_data['ratings_one'] = Rating.objects.filter(building=building.pk, rate='1').count()
        response_data['ratings_two'] = Rating.objects.filter(building=building.pk, rate='2').count()
        response_data['ratings_three'] = Rating.objects.filter(building=building.pk, rate='3').count()
        response_data['ratings_four'] = Rating.objects.filter(building=building.pk, rate='4').count()
        response_data['ratings_five'] = Rating.objects.filter(building=building.pk, rate='5').count()


        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
