"""
URL configuration for SpeedKart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from SpeedKartApp.views import *

urlpatterns = [
    path('', Login.as_view(), name="Login"),
    
    path('Registration', Registration.as_view(), name="Registration"),

    # ///////////////////////////////// ADMIN ///////////////////////////////////////////


    path('Add_ViewCategory', ViewCategory.as_view(), name="Add_ViewCategory"),
    path('Add_NewCategory', NewCategory.as_view(), name="Add_NewCategory"),
    path('AdminDashBoard', Dashboard.as_view(), name="AdminDashBoard"),
    path('Changepassword', Password.as_view(), name="Changepassword"),
    path('Forgotpassword', ForgotPassword.as_view(), name="Forgotpassword"),
    path('BlockAndUnblockShop', BlockAndUnblock.as_view(), name="BlockAndUnblockShop"),
    path('VerifyShop', VerifyShop.as_view(), name="VerifyShop"),
    path('VerifyComplaint', CompAndSentReplay.as_view(), name="VerifyComplaint"),
    path('VerifyDeliveryAgent', AdminDeliveryAgent.as_view(), name="ViewDeliveryAgent"),
    path('AdminReviewRating', AdminReviewRating.as_view(), name="AdminReviewRating"),


    # ///////////////////////////////// DELIVERY BOY ///////////////////////////////////////////


    path('DeliveryComplaint', DeliveryComp.as_view(), name="DeliveryComplaint"),
    path('deliverydash', DeliveryDashBoard.as_view(), name="DeliveryDashBoard"),
    path('DeliveryViewComplaint', DeliveryViewComp.as_view(), name="DeliveryViewComplaint"),
    path('DeliveryBoyReviewRating', DeliveryReviewRating.as_view(), name="DeliveryBoyReviewRating"),
    path('DeliveryNotification', DeliveryNotification.as_view(), name="DeliveryNotification"),
    path('DeliveryBoyUpdateOrder', DeliveryUpdateOrder.as_view(), name="DeliveryBoyUpdateOrder"),
    path('DeliveryBoyViewOrder', DeliveryViewOrder.as_view(), name="DeliveryBoyViewOrder"),


#//////////////////////////////// SELLER ///////////////////////////////////////////

    path('assigndeliveryboyseller', SellerDeliveryBoy.as_view(), name="assigndeliveryboyseller"),
    path('sellerchangepassword', SellerChangePassword.as_view(), name="sellerchangepassword"),
    path('sellerconfirmpassword', SellerConfirmPassword.as_view(), name="sellerconfirmpassword"),
    path('selleroffer', SellerOffer.as_view(), name="selleroffer"),
    path('sellerproduct', SellerProduct.as_view(), name="sellerproduct"),
    path('sellerprofile', SellerProfile.as_view(), name="sellerprofile"),
    path('sellernewpassword', SellerNewPassword.as_view(), name="sellernewpassword"),
    path('sellerreview', SellerReview.as_view(), name="sellerreview"),
    path('sellerdashboard', SellerDashBoard.as_view(), name="sellerdashboard"),
    path('sellersendreply', SellerSendReply.as_view(), name="sellersendreply"),
    path('sellercomp', SellerComp.as_view(), name="sellercomp"),
    path('sellerorder', SellerOrder.as_view(), name="sellerorder"),


#//////////////////////////////// TAILOR ///////////////////////////////////////////

    path('TailorDeliveryAgent', TailorDeliveryAgent.as_view(), name="TailorDeliveryAgent"),
    path('TailorDesign', TailorDesign.as_view(), name="TailorDesign"),
    path('TailorProfile', TailorProfile.as_view(), name="TailorProfile"),
    path('TailorDashBoard', TailorDashboard.as_view(), name="TailorDashBoard"),
    path('TailorRequestAssign', TailorRequestAndAssign.as_view(), name="TailorRequestAssign"),


]
