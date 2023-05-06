from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from loans.models import Loan, Payment


class LoanPaymentTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='user1', password='test123')
        self.user2 = User.objects.create_user(username='user2', password='test123')

        self.loan1 = Loan.objects.create(client=self.user1, amount=1000, interest_rate=0.05,
                                         requested_at="2023-05-06T10:00:00Z", bank="Itau", ip_address="101045")
        self.payment1 = Payment.objects.create(loan=self.loan1, amount=200, date="2023-05-06")
        self.payment2 = Payment.objects.create(loan=self.loan1, amount=300, date="2023-05-06")

    def test_create_loan(self):
        url = reverse('loans:create_loan')
        data = {'client': self.user1.id, 'amount': 2000, 'interest_rate': 0.03, "requested_at": "2023-05-06T10:00:00Z",
                "bank": "Itau", "ip_address": "101045"}
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_payment(self):
        url = reverse('loans:create_payment')
        data = {'loan': self.loan1.id, 'amount': 500, 'date': '2023-05-06'}
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_loan_balance(self):
        url = reverse('loans:loan_balance', args=[self.loan1.id])
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], 500.5)
