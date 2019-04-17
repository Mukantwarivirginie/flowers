# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .permissions import IsAdminOrReadOnly
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Project,Profile
from .forms import SignUpForm,ProfileForm,ProjectForm
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import BouquetsSerializer,ProfileSerializer




@login_required(login_url='/accounts/login/')
def bouquets_today(request):
    date = dt.date.today()
    bouquets = Article.todays_news()
    form = bouquetsLetterForm()
    return render(request, 'all-photo/today-project.html', {"date": date, "news": news, "letterForm": form})



@login_required(login_url='/accounts/login/')
def flowers(request):
    bouquets = Bouquet.objects.all()
    return render(request, 'photos/todays-projects.html', {"projects":projects})


def bouquets_of_day(request):
    bouquets = Bouquets.todays_bouquets()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['your_title']
            description = form.cleaned_data['description']
            link = form.cleaned_data['link']
            recipient = SignUpRecipients(title = title,description = description,link = link)
            recipient.save()
            HttpResponseRedirect('projectsToday')
    else:
        form = SignUpForm()
    return render(request, 'all-projects/todays-projects.html',{"projects":projects,"signupForm":form})

    def project(request,project_id):
        try:
            project = Project.objects.get(id = project_id)
        except DoesNotExist:
            raise Http404()
        return render(request,"all-photo/todays-projects.html")






def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('new-profile')

    else:
        form = ProfileForm()
    return render(request, 'new-profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def view_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id=current_user.id)
    print(profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_form = form.save(commit=False)
            profile_form.editor = current_user
            profile_form.save()

        return redirect('view-profile')

    else:
        form = ProfileForm()
    return render(request, 'view-profile.html', {"form": form,"profile":profile})


@login_required(login_url='/accounts/login/')
def addimage(request):

    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
   
        return redirect('flowers')

    else:
        form = ImageForm()
    return render(request, 'addimage.html', {"form": form})

@login_required(login_url='/accounts/login/')
def postbouquets(request):
    current_user = request.user
    if request.method == 'POST':
        form =  ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('flowers')

    else:
        form =  ProjectForm()
    return render(request, 'photo/postproject.html', {"form": form})




def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photo/search.html',{"message":message, "projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photo/search.html',{"message":message})








def projectletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = ProjectLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)



class ProjectList(APIView):
    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers = ProjectSerializer(all_merch, many=True)
        permission_classes = (IsAdminOrReadOnly,)
        return Response(serializers.data)



    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        permission_classes = (IsAdminOrReadOnly,)
        return Response(serializers.data)













