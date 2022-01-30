from django.shortcuts import render, HttpResponseRedirect
from .models import Expense
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import Http404
from .forms import ExpenseCreateForm, ApprovalForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import logout

class SignUp(CreateView):
  template_name = "registration/signup.html"
  form_class = UserCreationForm
  success_url = reverse_lazy("login")

def LogoutView(request):
  logout(request)
  return HttpResponseRedirect("/")

# Renders the html template and acts as the backend fot that page
@login_required
def home(request):
  context = {"name": request.user}
  return render(request, "expense_app/home.html",context)

def form_valid(self, form):
  form.instance.user = self.request.user
  return form_valid(form)

class ExpenseReview(LoginRequiredMixin, PermissionRequiredMixin, ListView):
  permission_required = "expense_app.view_expense"
  raise_exception = True
  model = Expense
  template_name = "expense_app/review.html"



class CreateExpense(LoginRequiredMixin, CreateView):
  model = Expense
  template_name = "expense_app/submission.html"
  form_class = ExpenseCreateForm
  success_url = "/history"


  def form_valid(self, form):
    form.instance.employee = self.request.user
    return super().form_valid(form)

class ExpenseHistory(LoginRequiredMixin, ListView):
  model = Expense
  queryset = Expense.objects.order_by('-time')
  template_name = "expense_app/history.html"
 

class ExpenseView(LoginRequiredMixin, DetailView):
  model = Expense
  template_name = "expense_app/expenseview.html"

class ManagerView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
  permission_required = "expense_app.change_expense"
  model = Expense
  template_name = "expense_app/claim.html"
  form_class = ApprovalForm 
  success_url = "/review"

