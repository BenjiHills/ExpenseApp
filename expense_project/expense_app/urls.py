from django.urls import path, include
from . import views


# Sets up the url to appear on the correct page
urlpatterns = [
  path('', views.home, name = 'home'),
  path("accounts/", include("django.contrib.auth.urls"), name="login"), 
  path("logout/", views.LogoutView, name="logout"),
  path('submission/', views.CreateExpense.as_view(), name = "submission"),
  path('review/', views.ExpenseReview.as_view(), name = "review"),
  path('history/', views.ExpenseHistory.as_view(), name = "history"),
  path("expense/<pk>", views.ExpenseView.as_view(), name = "expenseview"),
  path("claim/<pk>", views.ManagerView.as_view(), name = "claim"),
  path("signup/", views.SignUp.as_view(), name="signup"),
  path("drafts/", views.DraftsViews.as_view(), name = "drafts"),
  path("updatedraft/<pk>", views.UpdateDraft.as_view(), name = "updatedraft"),
  path("accepted/", views.AdminView.as_view(), name = "accepted")
]