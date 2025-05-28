from django.shortcuts import render, redirect
from .forms import AadharForm
from .models import Aadhar

# Create your views here.
def Index(request):
  form = AadharForm()
  if request.method == 'POST':
    form = AadharForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      print('saved')
      try:
        data = Aadhar.objects.all().order_by('-aadhar_num')[0]
      except:
        print('AADHAR NUMBER NOT FOUND')
      return render(request,'display.html',{'data':data})
    else:
      print(form.errors)
  
  return render(request,'index.html',{'form':form})

def Hero(request):
  return render(request,'home.html')

def Download(request):
  if request.method == 'POST':
    aadhar = request.POST.get('aadhar')
    data = Aadhar.objects.get(aadhar_num = aadhar)
    return render(request,'display.html',{'data':data})
  
  return render(request,'download.html')