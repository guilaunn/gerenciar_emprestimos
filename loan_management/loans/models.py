from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta


class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
    ip_address = models.CharField(max_length=100)
    requested_at = models.DateTimeField(auto_now_add=True)
    bank = models.CharField(max_length=100)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def balance(self):
        payments = Payment.objects.filter(loan=self)
        if not payments:
            return self.amount
        last_payment_date = max(payment.date for payment in payments)
        days_since_last_payment = (date.today() - last_payment_date).days
        balance = self.amount


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
