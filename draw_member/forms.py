# draw_member/forms.py
from django import forms
from draw_member.models import Member

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset

class UploadMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'addmember-form'
        self.helper.form_method = 'post'

        self.fields['name'].label ='抽獎者姓名'
        self.fields['photo'].label = '上傳一張照片'
        self.helper.add_input(Submit('submit', '新增'))
