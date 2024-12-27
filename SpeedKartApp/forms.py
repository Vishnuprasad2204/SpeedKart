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

class Product_form(ModelForm):
    class Meta:
        model = Product_Table
        fields = ['Product_name', 'Product_image', 'Description', 'Price', 'Quantity']

class Profile_form(ModelForm):
    class Meta:
        model = Seller_Table
        fields = ['Name', 'Address', 'Phone_no', 'Email']

