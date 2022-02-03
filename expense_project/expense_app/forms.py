from django import forms
from .models import Expense

class ExpenseCreateForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = ("expense_date", "expense_amount", "VAT_amount", "currency", "catagory", "persons_seen", "information")

class ApprovalForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = ("status", "manager_comment")
