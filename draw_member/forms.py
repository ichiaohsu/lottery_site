# draw_member/forms.py
from django import forms
from draw_member.models import Member

class UploadMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'photo']
