from rest_framework import serializers

from SpeedKartApp.models import *

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoginTable_model
        fields=['username','password']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable_model
        fields = ['id', 'Name','Email','Phone_no','Address']

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller_Table
        fields = ['id', 'Name','Address','Phone_no','Email']
            
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Table
        fields = ['id','SELLER_ID','CATEGORY','Product_name','Product_image','Description','Price','Quantity']

class Complaintserializer(serializers.ModelSerializer):
    class Meta:
        model=Complaints_Reply_Table
        fields=['login_id','Complaint','Reply']

class Complaintserializer1(serializers.ModelSerializer):
    class Meta:
        model=Complaints_Reply_Table
        fields=['Complaint','Reply']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Table
        fields = ['id','Category_name']
            
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer_Table
        fields = ['Offer_name','PRODUCT_ID','created_at','Offer_details','discount']
            
class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.Product_name', read_only=True)
    product_image = serializers.FileField(source='product.Product_image' , read_only=True)
    Price = serializers.IntegerField(source='product.Price', read_only=True)

    class Meta:
        model = orderitem
        fields = ['id','status','quantity','product','order', 'product_name', 'product_image', 'Price']
            
class ReviewSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='PRODUCT_ID.Product_name')
    product_image = serializers.FileField(source='PRODUCT_ID.Product_name')
    name = serializers.CharField(source='USER_ID.Name')
    class Meta:
        model = Productrate_Table
        fields = ['Review','Ratings','Complaint','Reply', 'product_name', 'product_image', 'name']
            
class DesignSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='TAILOR_ID.Name', read_only=True)
    Phone_no = serializers.IntegerField(source='TAILOR_ID.Phone_no', read_only=True)
    class Meta:
        model = Design_Table
        fields = ['id','Design_name','Design_image','Price','name', 'Phone_no']

class ReturnNotificationSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='orderdata.product.Product_name')
    Image = serializers.FileField(source='orderdata.product.Product_image')
    Price = serializers.CharField(source='orderdata.product.Price')
    Quandity = serializers.IntegerField(source='orderdata.quantity')
    class Meta:
        model = Notification_Table
        fields = ['id','Notification','status','updated_at','Quandity','Price','Image', 'product']
