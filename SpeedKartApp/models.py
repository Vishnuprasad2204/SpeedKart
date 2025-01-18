from django.db import models

# Create your models here.
class LoginTable_model(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)

class UserTable_model(models.Model):
    LOGIN_ID = models.ForeignKey(LoginTable_model, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Phone_no = models.IntegerField(null= True, blank= True)
    Address = models.CharField(max_length=200, null=True, blank=True)

class Seller_Table(models.Model):
    LOGIN_ID = models.ForeignKey(LoginTable_model, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    Phone_no = models.IntegerField(null= True, blank= True)
    Email = models.CharField(max_length=100, null=True, blank=True)



# review to app -user to admin
class Review_Table(models.Model):
    USER_ID = models.ForeignKey(UserTable_model, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add= True, null=True, blank=True)
    updated_at = models.DateField(auto_now= True, null=True, blank=True)
    Review = models.CharField(max_length= 200, null= True, blank= True)
    Ratings = models.IntegerField(null= True, blank= True)


class Delivery_Agent_Table(models.Model):
    LOGIN_ID = models.ForeignKey(LoginTable_model, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    Phone_no = models.IntegerField(null= True, blank= True)
    Email = models.CharField(max_length=100, null=True, blank=True)

# complaint to admin
class Complaints_Reply_Table(models.Model):
    USER_ID = models.ForeignKey(UserTable_model, on_delete=models.CASCADE, null=True, blank=True)
    SELLER_ID = models.ForeignKey(Seller_Table, on_delete=models.CASCADE, null=True, blank=True)
    DELIVERY = models.ForeignKey(Delivery_Agent_Table, on_delete=models.CASCADE, null=True, blank=True)
    Complaint = models.CharField(max_length= 200,null= True,blank= True)
    created_at = models.DateField(auto_now_add= True, null=True, blank=True)
    updated_at = models.DateField(auto_now= True, null=True, blank=True)
    Reply = models.CharField(max_length= 200,null= True,blank= True)


class Category_Table(models.Model):
    Category_name = models.CharField(max_length= 100, null= True, blank= True)
    Description =  models.CharField(max_length= 100, null= True, blank= True)
    created_at = models.DateField(auto_now_add= True, null=True, blank=True)
    updated_at = models.DateField(auto_now= True, null=True, blank=True)



class Product_Table(models.Model):
    SELLER_ID = models.ForeignKey(Seller_Table, on_delete=models.CASCADE, null=True, blank=True)
    CATEGORY= models.ForeignKey(Category_Table, on_delete=models.CASCADE, null=True, blank=True)
    Product_name = models.CharField(max_length=100, null=True, blank=True)
    Product_image = models.FileField(upload_to='product/',null= True,blank=True)
    Description =  models.CharField(max_length= 100, null= True, blank= True)
    Price = models.IntegerField(null= True, blank= True)
    Quantity = models.IntegerField(null= True, blank= True)



# product complaint and rating
class Productrate_Table(models.Model):
    USER_ID = models.ForeignKey(UserTable_model, on_delete=models.CASCADE, null=True, blank=True)
    PRODUCT_ID = models.ForeignKey(Product_Table, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add= True, null=True, blank=True)
    updated_at = models.DateField(auto_now= True, null=True, blank=True)
    Review = models.CharField(max_length= 200, null= True, blank= True)
    Ratings = models.IntegerField(null= True, blank= True)
    Complaint = models.CharField(max_length= 200,null= True,blank= True)
    Reply = models.CharField(max_length= 200,null= True,blank= True)



class Tailor_Table(models.Model):
    LOGIN_ID = models.ForeignKey(LoginTable_model, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    Phone_no = models.IntegerField(null= True, blank= True)
    Email = models.CharField(max_length=100, null=True, blank=True)




# uploading by tailor
class Design_Table(models.Model):
    Design_name = models.CharField(max_length=100, null=True, blank=True)
    Design_image = models.FileField(upload_to='tailordesign/', null=True, blank=True)
    Price = models.IntegerField(null= True, blank= True)
    TAILOR_ID = models.ForeignKey(Tailor_Table, on_delete=models.CASCADE, null= True, blank=True)


class Request_Table(models.Model):
    TAILOR_ID = models.ForeignKey(Tailor_Table, on_delete=models.CASCADE, null=True, blank=True)
    USER_ID = models.ForeignKey(UserTable_model, on_delete=models.CASCADE, null=True, blank=True)
    Design = models.ForeignKey(Design_Table,on_delete=models.CASCADE, null=True, blank=True)
    Measurements = models.CharField(max_length=100, null= True, blank= True)
    Quantity = models.IntegerField(null= True, blank= True)
    Request_status = models.CharField(max_length=100, null=True, blank=True)
    Date=models.DateField(auto_now_add=True,null=True,blank=True)


class Offer_Table(models.Model):
    Offer_name = models.CharField(max_length=100, null=True, blank=True)
    PRODUCT_ID = models.ForeignKey(Product_Table, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add= True, null=True, blank=True)
    updated_at = models.DateField(auto_now= True, null=True, blank=True)
    Offer_details = models.CharField(max_length=100, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)

class Order_Table(models.Model):
    #created_at = models.DateField(auto_now_add= True)
    #updated_at = models.DateField(auto_now= True)
    Date_Time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Order_details = models.CharField(max_length=100, null=True, blank=True)
    PRODUCT_ID = models.ForeignKey(Product_Table,on_delete=models.CASCADE, null= True, blank= True)
    User = models.ForeignKey(UserTable_model, on_delete=models.CASCADE, null=True, blank=True)
    Quantity = models.IntegerField(null= True, blank= True)
    Order_Status = models.CharField(max_length=100, null=True, blank=True)


class Cart_Table(models.Model):
    User_id = models.ForeignKey(LoginTable_model, on_delete=models.CASCADE, null=True, blank=True)
    PRODUCT_ID = models.ForeignKey(Product_Table, on_delete=models.CASCADE, null=True, blank=True)
    Quantity = models.IntegerField(null= True, blank= True)

class Payment_Table(models.Model):
    User_id = models.ForeignKey(LoginTable_model, on_delete=models.CASCADE, null=True, blank=True)
    CART_ID = models.ForeignKey(Cart_Table, on_delete=models.CASCADE, null=True, blank=True)





    
class Notification_Table(models.Model):
    ORDER_ID = models.ForeignKey(Order_Table,  on_delete= models.CASCADE, null= True, blank= True) 
    Order_name = models.CharField(max_length=100, null=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now= True, null=True, blank=True)
    Notification = models.CharField(max_length=100, null=True, blank=True)

class Assign_Table(models.Model):
    deliveryboy = models.ForeignKey(Delivery_Agent_Table, on_delete= models.CASCADE, null=True, blank=True)
    Order = models.ForeignKey(Order_Table,on_delete= models.CASCADE, null= True, blank= True)
    Order_Status = models.CharField(max_length=100, null=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now= True, null=True, blank=True)

class TailorAssign_Table(models.Model):
    deliveryboy = models.ForeignKey(Delivery_Agent_Table, on_delete= models.CASCADE, null=True, blank=True)
    Request= models.ForeignKey(Request_Table,on_delete= models.CASCADE, null= True, blank= True)
    Request_status = models.CharField(max_length=100, null=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now= True, null=True, blank=True)
