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
    path('logout',Logout.as_view()),
    
    path('Registration', Registration.as_view(), name="Registration"),
    path('ForgetPassword',ForgetPassword.as_view(),name="ForgetPassword"),

    # ///////////////////////////////// ADMIN ///////////////////////////////////////////


    path('Add_ViewCategory', ViewCategory.as_view(), name="Add_ViewCategory"),
    path('delete_catagory/<int:c_id>', DeleteCategory.as_view(), name="delete_catagory"),
    path('Add_NewCategory', NewCategory.as_view(), name="Add_NewCategory"),
    path('AdminDashBoard', Dashboard.as_view(), name="AdminDashBoard"),
    path('Changepassword', Password.as_view(), name="Changepassword"),
    path('Forgotpassword', ForgotPassword.as_view(), name="Forgotpassword"),
    path('BlockAndUnblockShop', BlockAndUnblock.as_view(), name="BlockAndUnblockShop"),
    path('VerifyShop', VerifyShop.as_view(), name="VerifyShop"),
    path('accept_shop/<int:s_id>', accept_shop.as_view(), name="accept_shop"),
    path('reject_shop/<int:s_id>', reject_shop.as_view(), name="reject_shop"),
    path('VerifyComplaint', CompAndSentReplay.as_view(), name="VerifyComplaint"),
    path('VerifyDeliveryService', AdminDeliveryService.as_view(), name="ViewDeliveryService"),
    path('approve_deliveryService/<int:d_id>', approve_deliveryService.as_view(), name="approve_deliveryService"),
    path('reject_deliveryService/<int:d_id>', reject_deliveryService.as_view(), name="reject_deliveryService"),
    path('AdminReviewRating', AdminReviewRating.as_view(), name="AdminReviewRating"),
    path('AdminReply/<int:id>', AdminReply.as_view(), name="AdminReply"),
    path('VerifyTailor', VerifyTailor.as_view(), name="VerifyTailor"),
    path('approveTailor/<int:t_id>', approveTailor.as_view(), name="approveTailor"),
    path('rejectTailor/<int:t_id>', rejectTailor.as_view(), name="rejectTailor"),

    # ///////////////////////////////// DELIVERY Service ///////////////////////////////////////////


    path('DeliveryComplaint', DeliveryComp.as_view(), name="DeliveryComplaint"),
    path('deliverydash', DeliveryDashBoard.as_view(), name="DeliveryDashBoard"),
    path('DeliveryViewComplaint', DeliveryViewComp.as_view(), name="DeliveryViewComplaint"),
    path('DeliveryReviewRating', DeliveryReviewRating.as_view(), name="DeliveryReviewRating"),
    path('DeliveryNotification', DeliveryNotification.as_view(), name="DeliveryNotification"),
    path('DeliveryUpdateOrder/<int:a_id>', DeliveryUpdateOrder.as_view(), name="DeliveryUpdateOrder"),
    path('DeliveryUpdateRequest/<int:ta_id>',DeliveryUpdateRequest.as_view(),name="DeliveryUpdateRequest"),
    path('DeliveryViewOrder', DeliveryViewOrder.as_view(), name="DeliveryViewOrder"),
    path('DeliveryReply', DeliveryReply.as_view(),name="DeliveryReply"),
    path('DeliveryUserNotification' , DeliveryUserNotification.as_view(), name="DeliveryUserNotification"),
    path('deliveryprofile', DeliveryProfile.as_view(), name="deliveryprofile"),

#//////////////////////////////// SELLER ///////////////////////////////////////////

    path('assigndeliveryseller/<int:o_id>', SellerDelivery.as_view(), name="assigndeliveryseller"),
    path('sellerchangepassword', SellerChangePassword.as_view(), name="sellerchangepassword"),
    path('sellerconfirmpassword', SellerConfirmPassword.as_view(), name="sellerconfirmpassword"),
    path('selleroffer', SellerOffer.as_view(), name="selleroffer"),
    path('viewoffer/<int:pk>', ViewOffer.as_view(), name="viewoffer"),
    path('editoffer/<int:pk>',Editoffer.as_view(), name="editoffer"), 
    path('deleteoff/<int:pk>', Deleteoffer.as_view(), name="deleteoff"),
    path('selleraddoffer/<int:pk>', SellerAddOffer.as_view(), name="selleraddoffer"),
    path('sellerproduct', SellerProduct.as_view(), name="sellerproduct"),
    path('selleraddproduct', SellerAddProduct.as_view(), name="selleraddproduct"),
    path('deletepro/<int:pk>', DeleteProduct.as_view(), name="deletepro"),
    path('editpro/<int:pk>', EditProduct.as_view(), name="editpro"),
    path('sellerprofile', SellerProfile.as_view(), name="sellerprofile"),
    path('sellernewpassword', SellerNewPassword.as_view(), name="sellernewpassword"),
    path('sellerreview', SellerReview.as_view(), name="sellerreview"),
    path('sellerdashboard', SellerDashBoard.as_view(), name="sellerdashboard"),
    path('sellersendcomp', SellerSendComp.as_view(), name="sellersendcomp"),
    path('sellerviewreply', SellerViewReply.as_view(), name="sellerviewreply"),
    path('sellersendreply/<int:pk>/', SellerSendReply.as_view(), name="sellersendreply"),
    path('sellercomp', SellerComp.as_view(), name="sellercomp"),
    path('sellercompdash', sellercompdash.as_view(), name="sellercompdash"),
    path('sellerorder', SellerOrder.as_view(), name="sellerorder"),
    path('sellerotp', SellerOtp.as_view(), name="sellerotp"),
    path('AssignDelivery',AssignDelivery.as_view(),name='AssignDelivery'),


#//////////////////////////////// TAILOR ///////////////////////////////////////////

    path('TailorDeliveryService/<int:req_id>', TailorDeliveryService.as_view(), name="TailorDeliveryService"),
    path('TailorDesign', TailorDesign.as_view(), name="TailorDesign"),
    path('TailorAddDesign', TailorAddDesign.as_view(), name="TailorAddDesign"),
    path('TailorProfile', TailorProfile.as_view(), name="TailorProfile"),
    path('TailorDashBoard', TailorDashboard.as_view(), name="TailorDashBoard"),
    path('TailorRequestAssign', TailorRequestAndAssign.as_view(), name="TailorRequestAssign"),
    path('deletedes/<int:pk>', DeleteDesign.as_view(), name="deletedes"),
    path('editdes/<int:pk>', EditDesign.as_view(), name="editdes"),
    path('Accept_Request/<int:r_id>', Accept_Request.as_view(), name="Accept_Request"),
    path('Reject_Request/<int:r_id>', Reject_Request.as_view(), name="Reject_Request"),




#/////////////////////////////////////API/////////////////////////////////////////////


    path('LoginPage', LoginPage.as_view(), name="LoginPage"),   
    path('UserReg', UserReg.as_view(), name="UserReg"),   
    path('ViewProfileApi/<int:lid>', ViewProfileApi.as_view(), name="ViewProfileApi"),   
    path('ViewShopApi', ViewShopApi.as_view(), name="ViewShopApi"),   
    path('ViewCategoryApi', ViewCategoryApi.as_view(), name="ViewCategoryApi"),   
    path('ShopProductApi/<int:s_id>', ShopProductApi.as_view(), name="ShopProductApi"),   
    path('ViewProductApi', ViewProductApi.as_view(), name="ViewProductApi"),   
    path('AddToCartApi/<int:lid>', AddToCartApi.as_view(), name="AddToCartApi"),
    path('OrderApi/<int:lid>', OrderApi.as_view(), name="OrderApi"),   
    path('OrderHistoryApi/<int:lid>', OrderHistoryApi.as_view(), name="OrderHistoryApi"),   
    path('ViewComplaintApi/<int:lid>', ComplaintApi.as_view(), name="ComplaintApi"),   
    path('ViewReview/<int:productid>', ViewReview.as_view(), name="ViewReview"),   
    path('ReturnNotificationApi/<int:lid>', ReturnNotificationApi.as_view(), name="ReturnNotificationApi"),   
    path('AcceptReturnApi', AcceptReturnApi.as_view(), name="AcceptReturnApi"),   
    path('RejectReturnApi', RejectReturnApi.as_view(), name="RejectReturnApi"),   
    path('ViewDesignApi', ViewDesignApi.as_view(), name="ViewDesignApi"),   
    path('SendRequestDesignApi/<int:lid>', SendRequestDesignApi.as_view(), name="SendRequestDesignApi"),   
    path('DetectApi', DetectApi.as_view(), name="DetectApi"),   
]
