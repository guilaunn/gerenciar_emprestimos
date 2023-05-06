from django.db.models import Sum
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Loan, Payment
from .serializers import LoanSerializer, PaymentSerializer


class LoanList(generics.GenericAPIView):
    def get(self, request):
        loans = Loan.objects.filter(client=self.request.user)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)


    @api_view(['POST'])
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def create_loan(request):
        user = request.user
        request.data['client'] = user.id
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def create_payment(request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def loan_balance(request, loan_id):
        try:
            loan = Loan.objects.get(id=loan_id, client=request.user)
        except Loan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        total_payments = Payment.objects.filter(loan=loan).aggregate(Sum('amount'))['amount__sum'] or 0
        interest = (loan.amount * loan.interest_rate) / 100
        balance = loan.amount + interest - total_payments

        return Response({'balance': balance})
