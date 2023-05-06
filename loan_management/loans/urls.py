from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LoanList


app_name = 'loans'

urlpatterns = [
    # Autenticação
    path('api-token-auth/', obtain_auth_token),

    path('loans/', LoanList.as_view(), name='loan-list'),
    path('loans/create/', LoanList.create_loan, name='create_loan'),
    path('payments/create/', LoanList.create_payment, name='create_payment'),
    path('loan_balance/<int:loan_id>/', LoanList.loan_balance, name='loan_balance'),

]