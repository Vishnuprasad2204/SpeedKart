from django.forms import ModelForm

from .models import *


class NewCategory_form(ModelForm):
    class Meta:
        model = Category_Table
        fields = ['Category_name','Description']

#class Registration_form(ModelForm):
 #  class Meta:
  #     model = 

class reply_form(ModelForm):
    class Meta:
        model = Complaints_Reply_Table
        fields = ['Reply']