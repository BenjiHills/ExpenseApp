from django import forms
from .models import Expense

class ExpenseCreateForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = ("expense_amount", "reason", "evidence")

class ApprovalForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = ("status", "manager_comment")
