# draw_member/views.py
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from draw_member.models import Member

from draw_member.forms import UploadMemberForm

# Create your views here.
def home(request):
    return render(request, 'draw_member/home.html')

def add_member(request):

    members = Member.objects.filter(drawed=False)

    if request.method == 'POST':

        form = UploadMemberForm(request.POST,request.FILES)
        if form.is_valid():
            member = form.save()
            return redirect('/add/')
    else:
        form = UploadMemberForm()
    return render(request, 'draw_member/add.html', {'members':members, 'form':form})

def draw(request):
    valid_members = Member.objects.filter(drawed=False)

    if not valid_members.exists():
        raise Http404("No valid member!")

    winner = random.choice(valid_members)
    winner.drawed = True
    winner.save()

    return render(request, 'draw_member/draw.html', {'winner':winner})
