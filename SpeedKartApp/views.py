import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

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
        return render(request, 'Registration.html')
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
                    f.LOGIN_ID = LoginTable_model.objects.create(username=request.POST['Name'], password=request.POST['password'], type='Tailor')
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
        return HttpResponse('''<script> alert('Accept Successfully');window.location="/VerifyShop" </script>''')
    
class reject_shop(View):
    def get(self, request, s_id):
        obj = LoginTable_model.objects.get(id=s_id)
        obj.type = 'Rejected'
        obj.save()
        return HttpResponse('''<script> alert('Reject Successfully');window.location="/VerifyShop" </script>''')
    
class approve_deliveryService(View):
    def get(self, request, d_id):
        obj = LoginTable_model.objects.get(id=d_id)
        obj.type = 'DeliveryAgent'
        obj.save()
        return HttpResponse('''<script> alert('Approve Successfully');window.location="/VerifyDeliveryService" </script>''')
    
class reject_deliveryService(View):
    def get(Self, request, d_id):
        obj = LoginTable_model.objects.get(id=d_id)
        obj.type = 'Rejected'
        obj.save()
        return HttpResponse('''<script> alert('Rejected Successfully');window.location="/VerifyDeliveryService" </script>''')


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
        notifications = Notification_Table.objects.select_related('orderdata', 'ASSIGN').all()
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
        obj1 = Order_Table.objects.get(id=obj.Order.id)
        status1 = request.POST['status']
        obj1.Order_Status = status1
        obj1.save()
        obj.Order_Status = status1
        obj.save()

        print("Updated Order Status:", status1)
        if str(status1) == "notavailable":
            print("%%%%%%%%%%%%%%%%%5----inside")
            print("Status is 'notavailable'. Processing email notification.")
            email = obj1.User.Email  # Replace `User.Email` with the actual field name
            print("Recipient email:", email)

            if email:
                try:
                    send_mail(
                        'User Not Available',  # Subject
                        'The delivery agent reported the user as not available.',  # Message
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
        obj1.Request_status=status
        obj1.save()
        obj.Request_status=status
        obj.save()
        return HttpResponse('''<script>alert('Updated Successfully.');window.location="/DeliveryViewOrder"</script>''')




class DeliveryViewOrder(View):
    def get(self, request):
        obj=Assign_Table.objects.filter(delivery_agent__LOGIN_ID=request.session['login_id'])
        obj1=TailorAssign_Table.objects.filter(deliveryboy__LOGIN_ID=request.session['login_id'])
        return render(request, 'DeliveryService/DeliveryViewOrder.html',{'val':obj , 'val1':obj1})
    
class DeliveryReply(View):
    def get(self, request):
        return render(request, 'DeliveryService/DeliveryReply.html')
    



    

#//////////////////////////////// SELLER  /////////////////////////////////////

class SellerDelivery(View):
    def get(self, request, o_id):
        request.session['o_id']=o_id
        obj = Delivery_Agent_Table.objects.all()
        obj1 = Order_Table.objects.get(id=o_id)
        return render(request, 'seller/assigndelivery_seller.html', {'obj': obj, 'obj1' :obj1})

class AssignDelivery(View):
    def post(self, request):
        form=Assign_Tableform(request.POST)
        if form.is_valid():
            obj1 = Order_Table.objects.get(id=request.session['o_id'])
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
        return HttpResponse('''<script>alert('deleted successfully');window.location="/selleroffer"</script>''')

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
            return HttpResponse('''<script>alert("updated successfullyy");window.location='/selleroffer'</script>''')


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
        c = Offer_Table.objects.get(pk=pk)
        return render(request, 'seller/viewOffer.html', {'obj': c})
    
class SellerAddProduct(View):
    def get(self, request):
        obj=Category_Table.objects.all()
        return render(request, 'seller/addproduct_seller.html',{'obj':obj})
    def post(self, request):
        c=Product_form(request.POST, request.FILES)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>window.location="/sellerproduct"</script>''')

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
        obj=Order_Table.objects.filter(PRODUCT_ID__SELLER_ID__LOGIN_ID_id=request.session['login_id'])
        print(request.session['login_id'])
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


    
    
    
