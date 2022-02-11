from django import forms
from .models import Expense

class DateInput(forms.DateInput):
    input_type = 'date'

class ExpenseCreateForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = ("expense_date", "expense_amount", "VAT_amount", "currency", "catagory", "persons_seen", "information", "document")
    widgets = {
            'expense_date': DateInput(),
            'persons_seen': forms.TextInput(attrs={'placeholder': "Provide the name(s) of the person you saw."}),
            'information': forms.Textarea(attrs={'placeholder': "Explanation of expense, including names for entertaining expenses and postcodes for mileage claims."})
        }

class ApprovalForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = ("manager_comment",)

class DraftForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = ("expense_date", "expense_amount", "VAT_amount", "currency", "catagory", "persons_seen", "information", "document")

