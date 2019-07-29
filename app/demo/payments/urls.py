from django.urls import path

from demo.payments.views import PaymentView, charge

urlpatterns = [
    path('charge/', charge, name='charge'),
    path('', PaymentView.as_view(), name='index'),
]
