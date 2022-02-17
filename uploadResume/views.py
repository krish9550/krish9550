from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def Home(request):
    if request.method == 'POST':
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
        #    n1=form.cleaned_data.get('fname')
            form.save()
            obj=form.instance
            form=ResumeForm()
            return render(request,'home.html',{'form':form,'obj':obj})
        else:
            return render(request,'home.html',{'form':form})

    else:
        form=ResumeForm()
        msg='Please Fill the fields'
        return render(request,'home.html',{'form':form,'msg':msg})
def Display(request):
    if request.method == 'GET':
        resumes=ResumeModel.objects.all()
        return render(request,'details.html',{'resumes':resumes})
def Contact(request):
    return render(request,'contact.html')
