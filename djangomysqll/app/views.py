from django.shortcuts import render
from .models import Customer
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,'home.html')



def Saveparty(request):   
    return render(request,'saveparty.html',{})

def insertuser(request): 
    vcustomer=request.POST['tcustomer'];
    vaddrs1=request.POST['tadd1'];
    vemail=request.POST['temail'];
    vllno=request.POST['tlln'];
    vcontprsn=request.POST['tcp'];
    vcity=request.POST['tcity'];
    vaddrs2=request.POST['tadd2'];
    vmob=request.POST['tmob'];
    vgstno=request.POST['tgstno'];
    cs=Customer(customer=vcustomer,address1=vaddrs1,email=vemail,landline_no=vllno,contact_person=vcontprsn,city=vcity,address2=vaddrs2,mobile=vmob,gstno=vgstno);
    cs.save();
    return render(request,'home.html',{})
    