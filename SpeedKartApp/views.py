from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from SpeedKartApp.models import LoginTable_model

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


    
    # ///////////////////////////////////// ADMIN/////////////////////////////////////
    
class ViewCategory(View):
    def get(self, request):
        return render(request, 'Admin/Add&ViewCategory.html')
    
class NewCategory(View):
    def get(self, request):
        return render(request, 'Admin/AddNewCategory.html')
    
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
        return render(request, 'Admin/Verify_shop.html')

class ViewApRjDelAgent(View):
    def get(self, request):
        return render(request, 'Admin/ViewApproved&RejectedDeliveryAgent.html')

class CompAndSentReplay(View):
    def get(self, request):
        return render(request, 'Admin/ViewComplaints&sentReplay.html')

class AdminDeliveryAgent(View):
    def get(self, request):
        return render(request, 'Admin/ViewDeliveryAgent&ApproveorReject.html')

class AdminReviewRating(View):
    def get(self, request):
        return render(request, 'Admin/ViewReview&Rating.html')


#/////////////////////////////////// DELIVERY BOY ////////////////////////////////


class DeliveryComp(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyComplaint.html')

class DeliveryDashBoard(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyDashBoard.html')

class DeliveryReg(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyRegistration.html')

class DeliveryViewComp(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoySentComplaint&ViewReplay.html')
    
class DeliveryNotification(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoySentNotification.html')

class DeliveryUpdateOrder(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyUpdateOrder.html')
    
class DeliveryViewOrder(View):
    def get(self, request):
        return render(request, 'Delivery boy/DeliveryBoyViewOrder.html')
    

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
    
class SellerRegistration(View):
    def get(self, request):
        return render(request, 'seller/registration_seller.html')

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
       
class TailorReg(View):
    def get(self, request):
        return render(request, 'Tailor/Registration.html')
        
class TailorDashboard(View):
    def get(self, request):
        return render(request, 'Tailor/TailorDashBoard.html')
        
class TailorRequestAndAssign(View):
    def get(self, request):
        return render(request, 'Tailor/view_request_and_assign_delivery_agent.html')
           

    
    
    
