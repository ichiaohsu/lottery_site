# draw_member/views.py
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from draw_member.models import Member

from django.forms.models import modelform_factory

# Create your views here.
def home(request):
    #return HttpResponse("<p>Home</p>")
    return render(request, 'draw_member/home.html')

def add_member(request):
    #return HttpResponse("<p>Add</p>")
    members = Member.objects.all()
    MemberForm = modelform_factory(Member,fields=('name',))
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect('/add/')
    else:
        form = MemberForm()
    return render(request, 'draw_member/add.html', {'members':members, 'form':form})

def draw(request):
    valid_members = Member.objects.filter(drawed=False)

    if not valid_members.exists():
        raise Http404("No valid member!")

    winner = random.choice(valid_members)
    winner.drawed = True
    winner.save()
    return render(request, 'draw_member/draw.html', {'winner':winner})
    #return HttpResponse('<p>Congratulations!{0.name}</p>'.format(winner))
