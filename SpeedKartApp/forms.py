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

class Assign_Tableform(ModelForm):
    class Meta:
        model = Assign_Table
        fields = ['deliveryboy', 'Order']

class AddOffer_form(ModelForm):
    class Meta:
        model = Offer_Table
        fields = ['Offer_name', 'Offer_details','PRODUCT_ID','discount']


class Prorep(ModelForm):
    class Meta:
        model = Productrate_Table
        fields = ['Reply']

class Compadmin(ModelForm):
    class Meta:
        model = Complaints_Reply_Table
        fields = ['SELLER_ID', 'Complaint']

class DevComp(ModelForm):
    class Meta:
        model = Complaints_Reply_Table
        fields = ['DELIVERY', 'Complaint']

class Design_form(ModelForm):
    class Meta:
        model = Design_Table
        fields = ['Design_name', 'Design_image','Price']

class TailorProfile_form(ModelForm):
    class Meta:
        model = Tailor_Table
        fields = ['Name', 'Address','Phone_no', 'Email']



