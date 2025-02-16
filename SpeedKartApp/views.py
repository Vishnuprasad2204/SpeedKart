import datetime
import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from SpeedKartApp.serializer import *

from .forms import *
from SpeedKartApp.models import *

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_obj = LoginTable_model.objects.get(username=username, password=password)
        request.session['login_id']=login_obj.id
        if login_obj.type == 'Admin':
            return HttpResponse('''<script> alert('Welcome to Home');window.location="/AdminDashBoard"</script>''')
        
        #elif login_obj.type == 'User':
        #   return HttpResponse('''<script> alert('Welcome to Home');window.location="/UserDashBoard" </script> ''')

        elif login_obj.type == 'Seller':
            return HttpResponse('''<script> alert('Welcome to Home');window.location="/sellerdashboard" </script> ''')
        elif login_obj.type == 'DeliveryAgent':
            return HttpResponse('''<script> alert('Welcome to Home');window.location="/deliverydash" </script>''')
        elif login_obj.type == 'Tailor':
            return HttpResponse('''<script> alert('Welcome to Home');window.location="/TailorDashBoard" </script> ''')
        else:
            return HttpResponse('''<script> alert('Invalid Credentials');window.location="/login" </script>''')
        

class Logout(View):
    def get(self, request):
            return HttpResponse('''<script> alert('Logout Successfully');window.location="/" </script> ''')


    #//////////////////////////////////REGISTRATION///////////////////////////////

def generate_otp():
    """Generate a 4-digit OTP."""
    return str(random.randint(1000, 9999)) 

from django.core.mail import send_mail
from django.contrib import messages



class Registration(View):
    def get(self, request):
        return redirect('DetectApi')
        # return render(request, 'Registration.html')
    def post(self, request):
        type = request.POST['type']

        if type == "Seller":
            form = SellerRegistrationForm(request.POST)
            if form.is_valid():
                try:
                    f = form.save(commit=False)
                    f.LOGIN_ID = LoginTable_model.objects.create(username=request.POST['Name'], password=request.POST['password'], type='pending')
                    f.LOGIN_ID.save()
                    f.save()
                    return redirect('/')  
                except LoginTable_model.DoesNotExist:
                    form.add_error(None, "FAILED")
        if type == "Tailor":
            form = TailorProfile_form(request.POST)
            if form.is_valid():
                try:
                    f = form.save(commit=False)
                    f.LOGIN_ID = LoginTable_model.objects.create(username=request.POST['Name'], password=request.POST['password'], type='pending')
                    f.LOGIN_ID.save()
                    f.save()
                    return redirect('/')  
                except LoginTable_model.DoesNotExist:
                    form.add_error(None, "FAILED")
        if type == "DeliveryAgent":
            form = DeliveryRegistrationForm(request.POST)
            if form.is_valid():
                try:
                    f = form.save(commit=False)
                    f.LOGIN_ID = LoginTable_model.objects.create(username=request.POST['Name'], password=request.POST['password'], type='pending')
                    f.LOGIN_ID.save()
                    f.save()
                    return redirect('/')  
                except LoginTable_model.DoesNotExist:
                    form.add_error(None, "FAILED")

    #//////////////////////////////////////FORGOT PASSWORD/////////////////////////////

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from .models import Tailor_Table, Seller_Table, Delivery_Agent_Table, LoginTable_model

class ForgetPassword(View):
    def get(self, request):
        return render(request, 'Forgotpassword.html')

    def post(self, request):
        user_name = request.POST.get('Name')
        email = request.POST.get('Email')

        if not user_name or not email:
            messages.error(request, "Both Name and Email are required.")
            return redirect('/Forgotpassword')

        # List of user tables to check
        user_tables = [Tailor_Table, Seller_Table, Delivery_Agent_Table]

        for table in user_tables:
            try:
                user = table.objects.get(Email=email, Name=user_name)
                login_obj = get_object_or_404(LoginTable_model, id=user.LOGIN_ID.id)

                # Send email (Consider replacing this with a password reset link)
                send_mail(
                    'Password Recovery',
                    f'Your Account Password is: {login_obj.password}',
                    'vishnuprasad2204@gmail.com',
                    [email],
                )

                messages.success(request, f'Password sent to {email}.')
                return HttpResponse(
                    '''<script>alert('Mail sent successfully'); window.location="/";</script>'''
                )

            except table.DoesNotExist:
                continue  # Check the next table

        messages.error(request, "Invalid Email or Name. Please try again.")
        return HttpResponse('''<script>alert('Email not found'); window.location="/"</script>''')
                    
    
    # ///////////////////////////////////// ADMIN/////////////////////////////////////
    
class ViewCategory(View):
    def get(self, request):
        c=Category_Table.objects.all()
        return render(request, 'Admin/Add&ViewCategory.html', {'s':c})

class DeleteCategory(View):
    def get(self, request, c_id):
        obj = Category_Table.objects.get(id=c_id)
        obj.delete()
        return HttpResponse('''<script> alert('Delete Successfully');window.location="/Add_ViewCategory" </script>''')

class accept_shop(View):
    def get(self, request, s_id):
        obj = LoginTable_model.objects.get(id=s_id)
        obj.type = 'Seller'
        obj.save()
        obj1 = Seller_Table.objects.get(LOGIN_ID_id=obj.id)
        print("Status is 'notavailable'. Processing email notification.")
        email = obj1.Email  # Replace `User.Email` with the actual field name
        print("Recipient email:", email)

        if email:
            try:
                send_mail(
                    'Successfully Approved',  # Subject
                    'Your registration in Modistra as Seller has Successfully approved.',  # Message
                    'vishnuprasad2204@gmail.com',  # From email
                    [email],  # Recipient list (should be a list)
                )
                messages.success(request, f'Email sent to {email}.')
                return redirect('Verify_otp')  # Adjust redirection as needed
            except Exception as e:
                messages.error(request, f'Failed to send email: {e}')
        else:
            messages.error(request, 'Invalid email address.')
        return HttpResponse('''<script> alert('Accept Successfully');window.location="/VerifyShop" </script>''')
    
class reject_shop(View):
    def get(self, request, s_id):
        obj = LoginTable_model.objects.get(id=s_id)
        obj.type = 'Rejected'
        obj.save()
        obj1 = Seller_Table.objects.get(LOGIN_ID_id=obj.id)
        print("Status is 'notavailable'. Processing email notification.")
        email = obj1.Email  # Replace `User.Email` with the actual field name
        print("Recipient email:", email)

        if email:
            try:
                send_mail(
                    'You are Rejected',  # Subject
                    'Your registration in Modistra as Seller has Rejected.',  # Message
                    'vishnuprasad2204@gmail.com',  # From email
                    [email],  # Recipient list (should be a list)
                )
                messages.success(request, f'Email sent to {email}.')
                return redirect('Verify_otp')  # Adjust redirection as needed
            except Exception as e:
                messages.error(request, f'Failed to send email: {e}')
        else:
            messages.error(request, 'Invalid email address.')
        return HttpResponse('''<script> alert('Reject Successfully');window.location="/VerifyShop" </script>''')
    
class approve_deliveryService(View):
    def get(self, request, d_id):
        obj = LoginTable_model.objects.get(id=d_id)
        obj.type = 'DeliveryAgent'
        obj.save()
        obj1 = Delivery_Agent_Table.objects.get(LOGIN_ID_id=obj.id)
        print("Status is 'notavailable'. Processing email notification.")
        email = obj1.Email  # Replace `User.Email` with the actual field name
        print("Recipient email:", email)

        if email:
            try:
                send_mail(
                    'Successfully Approved',  # Subject
                    'Your registration in Modistra as Delivery Service has Successfully approved.',  # Message
                    'vishnuprasad2204@gmail.com',  # From email
                    [email],  # Recipient list (should be a list)
                )
                messages.success(request, f'Email sent to {email}.')
                return redirect('Verify_otp')  # Adjust redirection as needed
            except Exception as e:
                messages.error(request, f'Failed to send email: {e}')
        else:
            messages.error(request, 'Invalid email address.')
        return HttpResponse('''<script> alert('Approve Successfully');window.location="/VerifyDeliveryService" </script>''')
    
class reject_deliveryService(View):
    def get(Self, request, d_id):
        obj = LoginTable_model.objects.get(id=d_id)
        obj.type = 'Rejected'
        obj.save()
        obj1 = Delivery_Agent_Table.objects.get(LOGIN_ID_id=obj.id)
        print("Status is 'notavailable'. Processing email notification.")
        email = obj1.Email  # Replace `User.Email` with the actual field name
        print("Recipient email:", email)

        if email:
            try:
                send_mail(
                    'You are Rejected',  # Subject
                    'Your registration in Modistra as Delivery Service has Rejected.',  # Message
                    'vishnuprasad2204@gmail.com',  # From email
                    [email],  # Recipient list (should be a list)
                )
                messages.success(request, f'Email sent to {email}.')
                return redirect('Verify_otp')  # Adjust redirection as needed
            except Exception as e:
                messages.error(request, f'Failed to send email: {e}')
        else:
            messages.error(request, 'Invalid email address.')
        return HttpResponse('''<script> alert('Rejected Successfully');window.location="/VerifyDeliveryService" </script>''')

class VerifyTailor(View):
    def get(self, request):
        obj = Tailor_Table.objects.all()
        return render(request, 'Admin/ViewTailor&ApproveorReject.html', {'val':obj})

class approveTailor(View):
    def get(self, request, t_id):
        obj=LoginTable_model.objects.get(id=t_id)
        obj.type = 'Tailor'
        obj.save()
        obj1 = Tailor_Table.objects.get(LOGIN_ID_id=obj.id)
        print("Status is 'notavailable'. Processing email notification.")
        email = obj1.Email  # Replace `User.Email` with the actual field name
        print("Recipient email:", email)

        if email:
            try:
                send_mail(
                    'Successfully Approved',  # Subject
                    'Your registration in Modistra as Tailor has Successfully approved.',  # Message
                    'vishnuprasad2204@gmail.com',  # From email
                    [email],  # Recipient list (should be a list)
                )
                messages.success(request, f'Email sent to {email}.')
                return redirect('Verify_otp')  # Adjust redirection as needed
            except Exception as e:
                messages.error(request, f'Failed to send email: {e}')
        else:
            messages.error(request, 'Invalid email address.')
        return HttpResponse('''<script> alert('Approved Successfully');window.location="/VerifyTailor" </script>''')






       
class rejectTailor(View):
    def get(self, request, t_id):
        obj=LoginTable_model.objects.get(id=t_id)
        obj.type = 'Rejected'
        obj.save()
        obj1 = Tailor_Table.objects.get(LOGIN_ID_id=obj.id)
        print("Status is 'notavailable'. Processing email notification.")
        email = obj1.Email  # Replace `User.Email` with the actual field name
        print("Recipient email:", email)

        if email:
            try:
                send_mail(
                    'You are Rejected',  # Subject
                    'Your registration in Modistra as Tailor has Rejected.',  # Message
                    'vishnuprasad2204@gmail.com',  # From email
                    [email],  # Recipient list (should be a list)
                )
                messages.success(request, f'Email sent to {email}.')
                return redirect('Verify_otp')  # Adjust redirection as needed
            except Exception as e:
                messages.error(request, f'Failed to send email: {e}')
        else:
            messages.error(request, 'Invalid email address.')
        return HttpResponse('''<script> alert('Rejected Successfully');window.location="/VerifyTailor" </script>''')
       

class NewCategory(View):
    def get(self, request):
        return render(request, 'Admin/AddNewCategory.html')
    def post(self, request):
        c=NewCategory_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('Add_ViewCategory')
    
class Dashboard(View):
    def get(self, request):
        return render(request, 'Admin/AdminDashBoard.html')
    
class Password(View):
    def get(self, request):
        return render(request, 'Admin/AdminChangePassword.html')
    
class ForgotPassword(View):
    def get(self, request):
        return render(request, 'Admin/AdminForgotPassword.html')

class BlockAndUnblock(View):
    def get(self, request):
        return render(request, 'Admin/Block&Unblockshop.html')

class VerifyShop(View):
    def get(self, request):
        obj = Seller_Table.objects.all()
        return render(request, 'Admin/Verify_shop.html', {'val':obj})

class CompAndSentReplay(View):
    def get(self, request):
        obj = Complaints_Reply_Table.objects.all()
        return render(request, 'Admin/ViewComplaints&sentReplay.html',{'val':obj})

class AdminDeliveryService(View):
    def get(self, request):
        obj = Delivery_Agent_Table.objects.all()
        return render(request, 'Admin/ViewDeliveryService&ApproveorReject.html', {'val':obj})

class AdminReviewRating(View):
    def get(self, request):
        obj = Review_Table.objects.all()
        return render(request, 'Admin/ViewReview&Rating.html', {'val':obj})

class AdminReply(View):
    def get(self, request,id):
        obj = Complaints_Reply_Table.objects.get(id=id)
        return render(request, 'Admin/admin_reply.html',{'obj':obj})
    def post(self, request, id):
        
        obj = Complaints_Reply_Table.objects.get(id=id)
        form = reply_form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('VerifyComplaint')
    




#/////////////////////////////////// DELIVERY BOY ////////////////////////////////


class DeliveryComp(View):
    def get(self, request):
        print(request.session['login_id'])
        obj=Delivery_Agent_Table.objects.get(LOGIN_ID_id=request.session['login_id'])
        return render(request, 'DeliveryService/DeliveryComplaint.html',{'obj': obj})
    def post(self,request):
        print("hhhhhh")
        c=DevComp(request.POST)  
        if c.is_valid():
            f=c.save(commit=False)
            obj=Delivery_Agent_Table.objects.get(LOGIN_ID_id=request.session['login_id'])
            f.DELIVERY=obj
            f.Reply="pending"
            f.save()
            return HttpResponse('''<script>alert('complaint sent successfully');window.location="/DeliveryViewComplaint"</script>''')        

class DeliveryDashBoard(View):
    def get(self, request):
        return render(request, 'DeliveryService/DeliveryDashBoard.html')

class DeliveryViewComp(View):
    def get(self, request):
        obj=Complaints_Reply_Table.objects.filter(DELIVERY__LOGIN_ID_id=request.session['login_id'])
        return render(request, 'DeliveryService/DeliverySentComplaint&ViewReplay.html',{'obj':obj})

class DeliveryReviewRating(View):
    def get(self, request):
        obj = ReviewDelivery.objects.all()
        return render(request, 'DeliveryService/DeliveryReviewRating.html',{'val':obj})
    
class DeliveryUserNotification(View):
    def get(self, request):
        # Ensure session contains 'login_id'
        if 'login_id' not in request.session:
            return HttpResponse('''<script>alert('Session expired. Please log in again.');window.location="/login"</script>''')
        id = request.session['login_id']
        try:
            # Fetch the logged-in delivery agent
            delid = Delivery_Agent_Table.objects.get(LOGIN_ID=id)
        except Delivery_Agent_Table.DoesNotExist:
            return HttpResponse('''<script>alert('Delivery agent not found.');window.location="/login"</script>''')

        # Fetch assignments related to the logged-in delivery agent
        obj = Assign_Table.objects.filter(delivery_agent=delid.id).select_related('Order')
        return render(request, 'DeliveryService/DeliveryUserNotification.html', {'val': obj, 'obj': delid})

    def post(self, request):
        assign_id = request.POST.get('select')  # Fetch the selected assign ID
        notification_text = request.POST.get('Complaint')  # Fetch the notification text

        if assign_id and notification_text:
            try:
                # Fetch the corresponding Assign_Table object
                assign_obj = Assign_Table.objects.get(id=assign_id)
                
                # Fetch the related Order_Table object
                order_obj = assign_obj.Order

                # Create a new notification, including the orderdata field
                Notification_Table.objects.create(
                    ASSIGN=assign_obj,
                    orderdata=order_obj,
                    Notification=notification_text,
                    status='Pending'
                )
                return HttpResponse('''<script>alert('Notification sent successfully');window.location="/DeliveryNotification"</script>''')
            except Assign_Table.DoesNotExist:
                return HttpResponse('''<script>alert('Invalid assignment ID.');window.location="/DeliveryNotification"</script>''')
        else:
            return HttpResponse('''<script>alert('All fields are required.');window.location="/DeliveryNotification"</script>''')
    
class DeliveryNotification(View):
    def get(self, request):
        # Fetch all notifications from the Notification_Table
        notifications = Notification_Table.objects.filter(ASSIGN__delivery_agent__LOGIN_ID=request.session['login_id'])
        print("^^^^^^^^^^^^^^^", notifications)
        return render(request, 'DeliveryService/DeliverySentNotification.html', {'notifications': notifications})

from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

class DeliveryUpdateOrder(View):
    def get(self, request, a_id):
        obj = Assign_Table.objects.get(id=a_id)
        return render(request, 'DeliveryService/DeliveryUpdateOrder.html', {'obj': obj})

    def post(self, request, a_id):
        obj = Assign_Table.objects.get(id=a_id)
        obj1 = orderitem.objects.get(id=obj.Order.id)
        status1 = request.POST['status']
        print(status1,"fffffffffffff")
        obj1.Order_Status = status1
        obj1.save()
        obj.Order_Status = status1
        obj.save()
        c="notavailable"
        print("Updated Order Status:", status1)
        if status1.strip() == c.strip():

            print("%%%%%%%%%%%%%%%%%5----inside")
            print("Status is 'notavailable'. Processing email notification.")
            email = obj1.User.Email  # Replace `User.Email` with the actual field name
            print("Recipient email:", email)

            if email:
                try:
                    send_mail(
                        'User Not Available',  # Subject
                        'The delivery agent reported the user as not available. Please contact the user to confirm the delivery.',  # Message
                        'vishnuprasad2204@gmail.com',  # From email
                        [email],  # Recipient list (should be a list)
                    )
                    messages.success(request, f'Email sent to {email}.')
                    return redirect('Verify_otp')  # Adjust redirection as needed
                except Exception as e:
                    messages.error(request, f'Failed to send email: {e}')
            else:
                messages.error(request, 'Invalid email address.')
        else:
            print("Order status updated successfully.")
            return HttpResponse(
                '''<script>alert('Updated Successfully.');window.location="/DeliveryViewOrder"</script>'''
            )

        return HttpResponse(
            '''<script>alert('Updated Successfully.');window.location="/DeliveryViewOrder"</script>'''
        )
class DeliveryUpdateRequest(View):
    def get(self, request,ta_id):
        obj = TailorAssign_Table.objects.get(id=ta_id)
        return render(request, 'DeliveryService/DeliveryUpdateRequest.html', {'obj': obj})
    def post(self, request, ta_id):
        obj = TailorAssign_Table.objects.get(id=ta_id)
        obj1 = Request_Table.objects.get(id=obj.Request.id)
        status = request.POST['status']
        print(status,"ffffffgggggggff")
        obj1.Request_status=status
        obj1.save()
        obj.Request_status=status
        obj.save()
        c="notavailable"
        print("Updated Request Status:", status)
        if status.strip() == c.strip():

            print("%%%%%%%%%%%%%%%%%5----inside")
            print("Status is 'notavailable'. Processing email notification.")
            email = obj1.USER_ID.Email  # Replace `User.Email` with the actual field name
            print("Recipient email:", email)

            if email:
                try:
                    send_mail(
                        'User Not Available',  # Subject
                        'The delivery agent reported the user as not available. Please contact the user to confirm the delivery.',  # Message
                        'vishnuprasad2204@gmail.com',  # From email
                        [email],  # Recipient list (should be a list)
                    )
                    messages.success(request, f'Email sent to {email}.')
                    return redirect('Verify_otp')  # Adjust redirection as needed
                except Exception as e:
                    messages.error(request, f'Failed to send email: {e}')
            else:
                messages.error(request, 'Invalid email address.')
        return HttpResponse('''<script>alert('Updated Successfully.');window.location="/DeliveryViewOrder"</script>''')




class DeliveryViewOrder(View):
    def get(self, request):
        obj=Assign_Table.objects.filter(delivery_agent__LOGIN_ID=request.session['login_id'])
        obj1=TailorAssign_Table.objects.filter(deliveryboy__LOGIN_ID=request.session['login_id'])
        return render(request, 'DeliveryService/DeliveryViewOrder.html',{'val':obj , 'val1':obj1})
    
class DeliveryReply(View):
    def get(self, request):
        return render(request, 'DeliveryService/DeliveryReply.html')
    

class DeliveryProfile(View):
    def get(self, request):
        obj=Delivery_Agent_Table.objects.get(LOGIN_ID_id=request.session['login_id'])
        return render(request, 'DeliveryService/manageprofile_delivery.html', {'obj': obj})
    def post(self, request):
        obj=Delivery_Agent_Table.objects.get(LOGIN_ID_id=request.session['login_id'])
        obj=DeliveryProfile_form(request.POST, instance=obj)
        if obj.is_valid():
            obj.save()
            return HttpResponse('''<script>alert('updated successfully');window.location="/deliveryprofile"</script>''')   



    

#//////////////////////////////// SELLER  /////////////////////////////////////

class SellerDelivery(View):
    def get(self, request, o_id):
        request.session['o_id']=o_id
        obj = Delivery_Agent_Table.objects.all()
        obj1 = orderitem.objects.get(id=o_id)
        return render(request, 'seller/assigndelivery_seller.html', {'obj': obj, 'obj1' :obj1})

class AssignDelivery(View):
    def post(self, request):
        form=Assign_Tableform(request.POST)
        if form.is_valid():
            obj1 = orderitem.objects.get(id=request.session['o_id'])
            obj1.Order_Status="assigned"
            obj1.save()
            form.save()
            return redirect('sellerorder')

class SellerChangePassword(View):
    def get(self, request):
        return render(request, 'seller/changepassword_seller.html')
        
class SellerConfirmPassword(View):
    def get(self, request):
        return render(request, 'seller/confirmpassword_seller.html')
    
class SellerOffer(View):
    def get(self, request):
        c=Offer_Table.objects.all()
        return render(request, 'seller/manageoffer_seller.html',{'obj': c})
    
class Deleteoffer(View):
    def get(self, request,pk):
        c = Offer_Table.objects.get(pk=pk)
        c.delete()
        return HttpResponse('''<script>alert('deleted successfully');window.location="/sellerproduct"</script>''')

class Editoffer(View):
    def get(self,request,pk):
        c=Offer_Table.objects.get(pk=pk)
        d = Product_Table.objects.all()
        return render(request, 'seller/editoffer.html',{'o': c, 'obj':d})
    def post(self, request, pk):
        c=Offer_Table.objects.get(pk=pk)
        d=AddOffer_form(request.POST, instance=c)
        if d.is_valid():
            d.save()
            return HttpResponse('''<script>alert("updated successfullyy");window.location='/sellerproduct'</script>''')


class SellerAddOffer(View):
    def get(self,request,pk):
        c = Product_Table.objects.get(pk=pk)
        print(c)
        return render(request, 'seller/addoffer_seller.html', {'obj': c})
    
    def post(self, request, pk):
        form= AddOffer_form(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.PRODUCT_ID=Product_Table.objects.get(id=pk)
            f.save()
            return redirect('sellerproduct')
    
class SellerProduct(View):
    def get(self, request):
        x=Product_Table.objects.all()
        return render(request, 'seller/manageproduct_seller.html', {'obj' : x})
    
class ViewOffer(View):
    def get(self, request, pk):
        c = Offer_Table.objects.get(PRODUCT_ID__id=pk)
        return render(request, 'seller/viewOffer.html', {'obj': c})
    
class SellerAddProduct(View):
    def get(self, request):
        obj=Category_Table.objects.all()
        return render(request, 'seller/addproduct_seller.html',{'obj':obj})
    def post(self, request):
        c=Product_form(request.POST, request.FILES)
        seller = Seller_Table.objects.get(LOGIN_ID__id=request.session['login_id'])
        print('-------',seller)
        if c.is_valid():
            f= c.save(commit=False)
            f.SELLER_ID=seller
            f.save()
            return HttpResponse('''<script>window.location="/sellerproduct"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid form");window.location="/sellerproduct"</script>''')

class DeleteProduct(View):
    def get(self, request, pk):
        c = Product_Table.objects.get(pk=pk)
        c.delete()
        return HttpResponse('''<script>alert('deleted successfully');window.location="/sellerproduct"</script>''')

class EditProduct(View):
    def get(self, request, pk):
        c = Product_Table.objects.get(pk=pk)
        return render(request, 'seller/editproduct_seller.html', {'obj': c})
    def post(self, request, pk):
        c = Product_Table.objects.get(pk=pk)
        c=Product_form(request.POST, request.FILES, instance=c)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>window.location="/sellerproduct"</script>''')


       

    
class SellerProfile(View):
    def get(self, request):
        obj=Seller_Table.objects.get(LOGIN_ID_id=request.session['login_id'])
        return render(request, 'seller/manageprofile_seller.html', {'obj': obj})
    def post(self, request):
        obj=Seller_Table.objects.get(LOGIN_ID_id=request.session['login_id'])
        obj=Profile_form(request.POST, instance=obj)
        if obj.is_valid():
            obj.save()
            return HttpResponse('''<script>alert('updated successfully');window.location="/sellerprofile"</script>''')
    
class SellerNewPassword(View):
    def get(self, request):
        return render(request, 'seller/newpassword_seller.html')
    

class SellerReview(View):
    def get(self, request):
        c=Productrate_Table.objects.all()
        return render(request, 'seller/review_seller.html',{'o':c})
    
class SellerDashBoard(View):
    def get(self, request):
        return render(request, 'seller/SellerDashBoard.html')
    
class SellerSendReply(View):
    def get(self, request,pk):
        c=Productrate_Table.objects.get(pk=pk)
        return render(request, 'seller/sendreply_seller.html',{'o':c})
    def post(self, request, pk):
        c=Productrate_Table.objects.get(pk=pk)
        d=Prorep(request.POST, instance=c)
        if d.is_valid():
            d.save()
        return HttpResponse('''<script>alert('replied successfully');window.location="/sellercomp"</script>''')
    

class SellerComp(View):
    def get(self, request):
        c=Productrate_Table.objects.all()
        return render(request, 'seller/viewcomplaint_seller.html',{'o':c})
    
class SellerSendComp(View):
    def get(self, request):
        obj=Seller_Table.objects.get(LOGIN_ID_id=request.session['login_id'])
        return render(request, 'seller/sendcomplaint_seller.html', {'obj': obj})
    def post(self,request):
        print("hhhhhh")
        c=Compadmin(request.POST)  
        if c.is_valid():
            c.save(commit=False)
            c.Reply="pending"
            c.save()
            return HttpResponse('''<script>alert('complaint sent successfully');window.location="/sellerviewreply"</script>''')


class SellerViewReply(View):
    def get(self, request):
        obj1=Complaints_Reply_Table.objects.filter(SELLER_ID__LOGIN_ID_id=request.session['login_id'])

        return render(request, 'seller/viewreply_seller.html',{'obj1':obj1})


    
class sellercompdash(View):
    def get(self, request):
        return render(request, 'seller/complaintdashboard_seller.html')
    
class SellerOrder(View):
    def get(self, request):
        obj=orderitem.objects.filter(product__SELLER_ID__LOGIN_ID_id=request.session['login_id'], status='order')
        print('------------>',request.session['login_id'])
        print('----------->',obj)
        return render(request, 'seller/vieworder_seller.html', {'obj': obj})
    
class SellerOtp(View):
    def get(self, request):
        return render(request, 'seller/otp_seller.html')



#////////////////////////////  TAILOR /////////////////////////////////////////////////////////

class TailorDeliveryService(View):
    def get(self, request, req_id):
        obj = Delivery_Agent_Table.objects.all()
        request.session['req_id']=req_id
        return render(request, 'Tailor/DeliveryServiceDropdown.html',{'val' : obj})
    def post(self,request, req_id):
        d_id=request.POST['d_id']
        req_id=request.session['req_id']
        obj=Delivery_Agent_Table.objects.get(id=d_id)
        obj1=Request_Table.objects.get(id=req_id)
        obj2=TailorAssign_Table()
        obj2.deliveryboy=obj
        obj2.Request=obj1
        obj2.Request_status="assigned"
        obj2.save()
        return HttpResponse('''<script>alert('Delivery Service assigned successfully');window.location="/TailorRequestAssign"</script>''')
    
class TailorDesign(View):
    def get(self, request):
        x=Design_Table.objects.all()
        return render(request, 'Tailor/Manage_Design.html',{'obj' : x})
    
class TailorAddDesign(View):
    def get(self, request):
        return render(request, 'Tailor/AddDesign_Tailor.html.')
    def post(self, request):
        c=Design_form(request.POST, request.FILES)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>window.location="/TailorDesign"</script>''')

class DeleteDesign(View):
    def get(self, request, pk):
        c = Design_Table.objects.get(pk=pk)
        c.delete()
        return HttpResponse('''<script>alert('deleted successfully');window.location="/TailorDesign"</script>''')
    
class EditDesign(View):
    def get(self, request, pk):
        c = Design_Table.objects.get(pk=pk)
        return render(request, 'Tailor/editdesign_tailor.html', {'obj': c})
    def post(self, request, pk):
        c = Design_Table.objects.get(pk=pk)
        c=Design_form(request.POST, request.FILES, instance=c)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>window.location="/TailorDesign"</script>''')

    
class TailorProfile(View):
    def get(self, request):
        obj=Tailor_Table.objects.get(LOGIN_ID_id=request.session['login_id'])
        return render(request, 'Tailor/Manage_profile.html',{'obj' : obj})
    def post(self, request):
        obj=Tailor_Table.objects.get(LOGIN_ID_id=request.session['login_id'])
        obj=TailorProfile_form(request.POST, instance=obj)
        if obj.is_valid():
            obj.save()
            return HttpResponse('''<script>alert('updated successfully');window.location="/TailorProfile"</script>''')
    
        
class TailorDashboard(View):
    def get(self, request):
        return render(request, 'Tailor/TailorDashBoard.html')
        
class TailorRequestAndAssign(View):
    def get(self, request):
        obj=Request_Table.objects.filter(TAILOR_ID__LOGIN_ID_id=request.session['login_id'])
        return render(request, 'Tailor/view_request_and_assign_delivery_Service.html', {'obj': obj})
           
class Accept_Request(View):
    def get(self, request, r_id):
        obj = Request_Table.objects.get(id=r_id)
        obj.Request_status = 'Accepted'
        obj.save()
        return HttpResponse('''<script> alert('Accept Successfully');window.location="/TailorRequestAssign" </script>''')
    
class Reject_Request(View):
    def get(Self, request, r_id):
        obj = Request_Table.objects.get(id=r_id)
        obj.Request_status= 'Rejected'
        obj.save()
        return HttpResponse('''<script> alert('Rejected Successfully');window.location="/TailorRequestAssign" </script>''')


# ////////////////////////////////////////// API /////////////////////////////////////////////
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.status import *

class UserReg(APIView):
    def post(self, request):
        print("#########",request.data)
        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            print("&&&&&&&&&&&&&&&")
            password = request.data['password']
            login_profile = login_serial.save(type='USER',password=password)
            user_serial.save(LOGIN_ID=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error':login_serial.errors if not login_valid else None,
                         'user_error':user_serial.errors if not data_valid else None}, status=status.HTTP_400_BAD_REQUEST)

class LoginPage(APIView):
    def post(self, request):
        print("---------------->")
        response_dict = {}
        print("------------>", request.data)
      # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")
        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)
        # Fetch the user from LoginTable
        t_user = LoginTable_model.objects.filter(username=username,password=password).first()
        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)
        # # Check password using check_password
        # if not check_password(password, t_user.password):
        #     response_dict["message"] = "failed"
        #     return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id

        return Response(response_dict, status=HTTP_200_OK)


class ViewProfileApi(APIView):
    def get(self, request, lid):
        obj = UserTable_model.objects.filter(LOGIN_ID_id=lid)
        serializer = UserSerializer(obj, many=True)
    
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, lid):
        obj = get_object_or_404(UserTable_model, LOGIN_ID_id=lid)
        user_serial = UserSerializer(obj, data=request.data, partial=True)  # Enable partial updates

        if user_serial.is_valid():
            user_serial.save()
            return Response(user_serial.data, status=status.HTTP_200_OK)
        
        return Response(user_serial.errors, status=status.HTTP_400_BAD_REQUEST)
 
class ViewShopApi(APIView):
    def get(self, request):
        seller = Seller_Table.objects.all()
        seller_serializer = SellerSerializer(seller, many=True)
        return Response(seller_serializer.data)
 
class ViewProductApi(APIView):
    def get(self, request):
        product = Product_Table.objects.all()
        product_serializer = ProductSerializer(product, many=True)
        return Response(product_serializer.data)
 
class ShopProductApi(APIView):
    def get(self, request, s_id):
        products = Product_Table.objects.filter(SELLER_ID_id=s_id)
        product_data = []
        for product in products:
            offer = Offer_Table.objects.filter(PRODUCT_ID=product).first()  # Get the first offer if available
            product_info = {
                "id": product.id,
                "Product_name": product.Product_name,
                "Product_image": product.Product_image.url if product.Product_image else None,
                "Description": product.Description,
                "Price": product.Price,
                "Quantity": product.Quantity,
                "Offer": {
                    "Offer_name": offer.Offer_name if offer else None,
                    "Offer_details": offer.Offer_details if offer else None,
                    "Discount": offer.discount if offer else None,
                } if offer else None,
            } 
            product_data.append(product_info)
        return Response(product_data)
  
class ViewCategoryApi(APIView):
    def get(self, request):
        obj = Category_Table.objects.all() 
        obj_serializer = CategorySerializer(obj, many=True)
        print('----->', obj_serializer.data)
        return Response(obj_serializer.data, status=status.HTTP_200_OK)
 
class AddToCartApi(APIView):
    def get(self, request, lid):
        order_details = orderitem.objects.filter(order__user__LOGIN_ID_id=lid, status='cart')
        order_serializer = OrderSerializer(order_details, many=True)
        print('--------->', order_serializer.data)
        return Response(order_serializer.data)
    def post(self, request, lid):
        qty = request.data.get('quantity')
        pro_id = request.data.get('product_id')
        ob = Product_Table.objects.get(id=pro_id)
        tt = int(ob.Price) * int(qty)
        stock = ob.Quantity
        nstk = int(stock) - int(qty)
        if stock >= int(qty):
            up = Product_Table.objects.get(id=pro_id)
            up.Quantity = nstk
            up.save()
            q = order.objects.filter(user__LOGIN_ID__id=lid)
            if len(q) == 0:
                obe = order()
                obe.totalamount = tt
                obe.status = 'cart'
                obe.date = datetime.datetime.now().strftime("%Y-%m-%d")
                obe.user = UserTable_model.objects.get(LOGIN_ID__id=lid)
                obe.save()
                obe1 = orderitem()
                obe1.quantity = qty
                obe1.order = obe
                obe1.status = 'cart'
                obe1.product = up
                obe1.save()
                return Response(status=status.HTTP_200_OK)
            else:
                total = int(ob.Price) + int(tt)
                print(total, "KKKKKKKKKKKKKKKK")
                obr = order.objects.get(id=q[0].id)
                obr.totalamount= total
                obr.status = 'cart'
                obr.save()
                obr1 = orderitem()
                obr1.quantity = qty
                obr1.order = obr
                obr1.status = 'cart'
                obr1.product = up
                obr1.save()
                return Response(status=status.HTTP_200_OK)
        else:
            data = {"task": "out of stock"}
            return Response(data, status=status.HTTP_200_OK)
    
class OrderHistoryApi(APIView):
    def get(self, request, lid):
        order = orderitem.objects.filter(order__user__LOGIN_ID_id=lid, status='delivered')
        order_serializer = OrderSerializer(order, many=True)
        return Response(order_serializer.data, status=status.HTTP_200_OK)
class OrderApi(APIView):
    def get(self, request, lid):
        order = orderitem.objects.filter(order__user__LOGIN_ID_id=lid, status='order')
        order_serializer = OrderSerializer(order, many=True)
        return Response(order_serializer.data, status=status.HTTP_200_OK)
    def post(self, request, lid):
        item_id = request.data.get('id')
        print('------------>', request.data)
        obj = orderitem.objects.get(id=item_id)
        obj.status='order'
        obj.save()
        return Response(status=status.HTTP_200_OK)

class ComplaintApi(APIView):  # Class names should typically be in CamelCase
    def get(self, request, lid):
        try:
            # Fetch complaints related to the provided login_id (lid)
            valu = Complaints_Reply_Table.objects.filter(USER_ID__LOGIN_ID_id=lid)
            print("vallllllllll", valu)
            # Check if there are any complaints
            if not valu.exists():
                return Response({"detail": "No complaint and reply."}, status=status.HTTP_204_NO_CONTENT)
            # Serialize the queryset with many=True to handle multiple objects
            complaints = Complaintserializer1(valu, many=True)
            print("cccccc", complaints.data)
            # Return the serialized data
            return Response(complaints.data, status=status.HTTP_200_OK)

        except Exception as e:
            # In case of any error, return a 500 Internal Server Error with the error message
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, lid):
        try:
            complaint = request.data.get('complaint')
            obj = Complaints_Reply_Table()
            obj.USER_ID = UserTable_model.objects.get(LOGIN_ID_id=lid)
            obj.Complaint = complaint
            obj.Reply='pending'
            obj.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ViewReview(APIView):
    def get(self, request, productid):
        product_id=productid
        review = Productrate_Table.objects.filter(PRODUCT_ID_id=product_id)
        review_serializer = ReviewSerializer(review, many=True)
        print('----------->', review_serializer.data)
        return Response(review_serializer.data)
    def post(self, request, productid):
        product_id=productid
        lid=request.data.get('lid')
        rating=request.data.get('rating')
        review=request.data.get('review')
        complaint=request.data.get('complaint')
        
        obj = Productrate_Table()   
        obj.USER_ID = UserTable_model.objects.get(LOGIN_ID_id=lid)
        obj.PRODUCT_ID = Product_Table.objects.get(id=product_id)
        obj.Ratings = rating
        obj.Review = review
        obj.Complaint= complaint
        obj.Reply ="pending"
        obj.save()
        return Response(status=status.HTTP_200_OK)
        

class ReturnNotificationApi(APIView):
    def get(self, request, lid):
        try:
            return_notification = Notification_Table.objects.filter(orderdata__order__user__LOGIN_ID_id=lid, status="pending")
            return_notification_serializer = ReturnNotificationSerializer(return_notification, many=True)
            print(return_notification_serializer.data)
            return Response(return_notification_serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
class AcceptReturnApi(APIView):        
    def post(self, request):
        try:
            item_id = request.data.get('id')
            return_notification = Notification_Table.objects.get(id=item_id)
            return_notification.status = 'accept'
            return_notification.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RejectReturnApi(APIView):        
    def post(self, request):
        try:
            item_id = request.data.get('id')
            return_notification = Notification_Table.objects.get(id=item_id)
            return_notification.status = 'reject'
            return_notification.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ViewDesignApi(APIView):
    def get(self, request):
        design = Design_Table.objects.all()
        design_serializer = DesignSerializer(design, many=True)
        return Response(design_serializer.data)
    def post(self, request):
        try:
            lid = request.data.get('lid')
            d_id = request.data.get('d_id')
            Measurements = request.data.get('Measurements')
            Quantity = request.data.get('Quantity')
            lid = request.data.get('lid')
            obj = Request_Table()
            obj.USER_ID = UserTable_model.objects.get(LOGIN_ID_id=lid)
            obj.Design = Design_Table.objects.get(id=d_id)
            obj.Measurements = Measurements
            obj.Quantity = Quantity
            obj.Request_status = 'pending'
            obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class SendRequestDesignApi(APIView):
    def post(self, request, lid):
        Design_id = request.data.get('Design_id')
        Measurements = request.data.get('Measurements')
        Quantity = request.data.get('Quantity')
        obj = Request_Table()
        obj.USER_ID = UserTable_model.objects.get(LOGIN_ID_id=lid)
        obj.Design = Design_Table.objects.get(id=Design_id)
        obj.Measurements = Measurements
        obj.Quantity = Quantity
        obj.Request_status = 'pending'
        obj.save()
        return Response(status=status.HTTP_200_OK)




from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import numpy as np
import cv2
from ultralytics import YOLO

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import numpy as np
import cv2
from ultralytics import YOLO

class DetectApi(APIView):
    def post(self, request):
        data_list = []

        # Load the model
        model = YOLO("D:/Sk/SpeedKart/last.pt")

        # Get the uploaded image
        file_obj = request.FILES.get('image')
        if not file_obj:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Convert the image file to a NumPy array
        image_bytes = file_obj.read()
        image_array = np.asarray(bytearray(image_bytes), dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        # Check if the image was loaded properly
        if image is None:
            return Response({"error": "Invalid image file"}, status=status.HTTP_400_BAD_REQUEST)

        # Perform object detection
        results = model.predict(image)

        # Check if results contain valid detections
        if results:
            first_result = results[0]  # Get the first result
            if hasattr(first_result, "boxes") and first_result.boxes is not None:
                for result in first_result.boxes.data.tolist():
                    x1, y1, x2, y2, score, class_id = result
                    if score > 0.5:
                        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                        cv2.putText(image, first_result.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
                        data_list.append(first_result.names[int(class_id)])
        print("------------------->", data_list)
        p_list = []
        for i in data_list:
            print("-----",i)
        product_obj = Product_Table.objects.filter(CATEGORY__Category_name__in=data_list)
        print('-----product obj---->', product_obj)    
        product_serializer = ProductSerializer(product_obj, many=True)
        print('-----serial---->', product_serializer.data)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
