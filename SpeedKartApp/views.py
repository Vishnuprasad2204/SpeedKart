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

    #//////////////////////////////////REGISTRATION///////////////////////////////

class Registration(View):
    def get(self, request):
        return render(request, 'Registration.html')
    
    
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
    
class approve_deliveryagent(View):
    def get(self, request, d_id):
        obj = LoginTable_model.objects.get(id=d_id)
        obj.type = 'DeliveryAgent'
        obj.save()
        return HttpResponse('''<script> alert('Approve Successfully');window.location="/VerifyDeliveryAgent" </script>''')
    
class reject_deliveryagent(View):
    def get(Self, request, d_id):
        obj = LoginTable_model.objects.get(id=d_id)
        obj.type = 'Rejected'
        obj.save()
        return HttpResponse('''<script> alert('Rejected Successfully');window.location="/VerifyDeliveryAgent" </script>''')


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
        obj = ShopTable_model.objects.all()
        return render(request, 'Admin/Verify_shop.html', {'val':obj})

class CompAndSentReplay(View):
    def get(self, request):
        obj = Complaints_Reply_Table.objects.all()
        return render(request, 'Admin/ViewComplaints&sentReplay.html',{'val':obj})

class AdminDeliveryAgent(View):
    def get(self, request):
        obj = Delivery_Agent_Table.objects.all()
        return render(request, 'Admin/ViewDeliveryAgent&ApproveorReject.html', {'val':obj})

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
        return render(request, 'Delivery boy/DeliveryBoyComplaint.html')

class DeliveryDashBoard(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyDashBoard.html')

class DeliveryViewComp(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoySentComplaint&ViewReplay.html')

class DeliveryReviewRating(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyReviewRating.html')
    
class DeliveryNotification(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoySentNotification.html')

class DeliveryUpdateOrder(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyUpdateOrder.html')
    
class DeliveryViewOrder(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyViewOrder.html')
    
class DeliveryBoyReply(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyReply.html')
    

#//////////////////////////////// SELLER  /////////////////////////////////////

class SellerDeliveryBoy(View):
    def get(self, request):
        return render(request, 'seller/assigndeliveryboy_seller.html')

class SellerChangePassword(View):
    def get(self, request):
        return render(request, 'seller/changepassword_seller.html')
        
class SellerConfirmPassword(View):
    def get(self, request):
        return render(request, 'seller/confirmpassword_seller.html')
    
class SellerOffer(View):
    def get(self, request):
        return render(request, 'seller/manageoffer_seller.html')
    
class SellerProduct(View):
    def get(self, request):
        return render(request, 'seller/manageproduct_seller.html')
    
class SellerProfile(View):
    def get(self, request):
        return render(request, 'seller/manageprofile_seller.html')
    
class SellerNewPassword(View):
    def get(self, request):
        return render(request, 'seller/newpassword_seller.html')
    

class SellerReview(View):
    def get(self, request):
        return render(request, 'seller/review_seller.html')
    
class SellerDashBoard(View):
    def get(self, request):
        return render(request, 'seller/SellerDashBoard.html')
    
class SellerSendReply(View):
    def get(self, request):
        return render(request, 'seller/sendreply_seller.html')

class SellerComp(View):
    def get(self, request):
        return render(request, 'seller/viewcomplaint_seller.html')
    
class SellerOrder(View):
    def get(self, request):
        return render(request, 'seller/vieworder_seller.html')
    
class SellerOtp(View):
    def get(self, request):
        return render(request, 'seller/otp_seller.html')
    

#////////////////////////////  TAILOR /////////////////////////////////////////////////////////

class TailorDeliveryAgent(View):
    def get(self, request):
        return render(request, 'Tailor/Delivery_Agent_Dropdown.html')
    
class TailorDesign(View):
    def get(self, request):
        return render(request, 'Tailor/Manage_Design.html')
    
class TailorProfile(View):
    def get(self, request):
        return render(request, 'Tailor/Manage_profile.html')
        
class TailorDashboard(View):
    def get(self, request):
        return render(request, 'Tailor/TailorDashBoard.html')
        
class TailorRequestAndAssign(View):
    def get(self, request):
        return render(request, 'Tailor/view_request_and_assign_delivery_agent.html')
           

    
    
    
