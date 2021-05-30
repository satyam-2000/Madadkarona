
from django.shortcuts import render
import requests
import json
from corona.models.lucknowarea import LucknowArea
from corona.models.delhiarea import DelhiArea
from corona.models.lucknowdealers import LucknowDealer
from corona.models.delhidealers import DelhiDealer
from corona.models.kanpurdealers import KanpurDealer
from corona.models.lkobeds import Lucknowbeds
from corona.models.delhibeds import Delhibeds
from corona.models.kanpurbeds import Kanpurbeds

# Create your views here.

def index(request):
    areas=LucknowArea.get_all_area()
    dealers=None
    area_id=request.GET.get('area')
    
    if area_id:
        dealers=LucknowDealer.get_dealers_byarea(area_id)
    else:
        dealers=LucknowDealer.get_all_dealers()
    text="Lucknow"
    

    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring={"country":"India"}

    headers = {
    'x-rapidapi-key': "5f3c787debmsha43306ccb206c5ep143ecajsn5d1bfc6a613b",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers,params=querystring).json()
    data=response['response']
    d=data[0]

    print(d)
    context={
        'all':d['cases']['total'],
        'rec':d['cases']['recovered'],
        'deaths':d['deaths']['total'],
        'new':d['cases']['new'],
        'critical':d['cases']['critical'],
        'areas':areas,
        'dealers':dealers,
        'text':text,

    }
   

    
    return render(request,'index.html',context)

def delhi(request):
    text="Delhi"
    areas=DelhiArea.get_all_area()
    dealers=None
    area_id=request.GET.get('area')
    print(area_id)
    if area_id:
        dealers=DelhiDealer.get_dealers_byarea(area_id)
    else:
        dealers=DelhiDealer.get_all_dealers()
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring={"country":"India"}

    headers = {
    'x-rapidapi-key': "5f3c787debmsha43306ccb206c5ep143ecajsn5d1bfc6a613b",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers,params=querystring).json()
    data=response['response']
    d=data[0]
    context={
         'all':d['cases']['total'],
        'rec':d['cases']['recovered'],
        'deaths':d['deaths']['total'],
        'new':d['cases']['new'],
        'critical':d['cases']['critical'],
        'text':text,
        'areas':areas,
        'dealers':dealers,
    }
    
    return render(request,'corona/delhi.html',context)

def donate(request):
    if request.method=='GET':

        return render(request,'corona/donate.html')

    else:
        order_amount = 100
        order_currency = 'INR'
        client=razorpay.Client(auth=('rzp_test_Z2HP9qq6AWn98h','08Uww3zeQzylFluEOZlKnm6G'))
        payment=client.order.create({'amount':order_amount, 'currency':order_currency,'payment_capture':'1'})
   

def lbeds(request):
    beds=Lucknowbeds.get_all_beds()
    context={
        'beds':beds,
    }
    return render(request,'corona/lucknowbeds.html',context)
def dbeds(request):
    beds=Delhibeds.get_all_beds()
    context={
        'beds':beds,
    }
    return render(request,'corona/delhibeds.html',context)
def kbeds(request):
    beds=Kanpurbeds.get_all_beds()
    context={
        'beds':beds,
    }
    return render(request,'corona/kanpurbeds.html',context)



def kanpur(request):
    text="Kanpur"
    
    dealers=KanpurDealer.get_all_dealers()
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring={"country":"India"}

    headers = {
    'x-rapidapi-key': "5f3c787debmsha43306ccb206c5ep143ecajsn5d1bfc6a613b",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers,params=querystring).json()
    data=response['response']
    d=data[0]
    context={
         'all':d['cases']['total'],
        'rec':d['cases']['recovered'],
        'deaths':d['deaths']['total'],
        'new':d['cases']['new'],
        'critical':d['cases']['critical'],
        'text':text,
        'dealers':dealers,
    }
    return render(request,'corona/kanpur.html',context)