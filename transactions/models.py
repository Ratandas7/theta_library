from django.db import models
from accounts.models import UserAccount
from transactions.constants import TRANSACTION_TYPES
# Create your models here.

class Transaction(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    balance_after_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    # borrowing = models.ForeignKey('book.Borrow', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.amount} - {self.account.user.username}"

