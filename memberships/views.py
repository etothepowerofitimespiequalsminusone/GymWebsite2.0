from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from .models import Type,Classes


# Create your views here.
class IndexView(generic.ListView):
    model = Type
    template_name = 'memberships/index.html'


class MembershipView(generic.ListView):
    model = Type
    template_name = 'memberships/details.html'

class ClassesView(generic.ListView):
    model = Classes
    template_name = 'memberships/classes.html'

def detail(request,type_id):
    return HttpResponse("you are looking at %s." % type_id)


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit = False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username,password = password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('memberships:index')

            return render(request,self.template_name,{'form':form})

