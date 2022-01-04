from django.shortcuts import render
from .models import *
import json
from .forms import *
#import django.models jsonresponse


# Create your views here.

def serarch_phone(request):
    #data = json.loads(request.body)
    #phone_lis= []
    #name =  form.cleaned_data["name"]
    #print(name)
    #phone_data = Phone.objects.filter(name)
    phone_data = Phone.objects.filter(name = request.GET.get('name'))

    # for name in Phone.objects.filter(name=data["mobile_name"]):
    #     pass
        # phone_details = {}
        # phone_details['model_no'] =name.model
        # phone_details['serial_no'] =name.serial_no
        # phone_details['description'] =name.description
        # phone_lis.append(phone_details)
    return render(request, "phone.html",{'phone_data':phone_data,"forms":PhoneForm})


