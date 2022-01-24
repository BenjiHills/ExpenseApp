from django.db import models
import datetime
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Expense(models.Model):

    # reduces stored data in table to two letters these might be changed to their own tables later
    Approved = "AP"
    Rejected = "RE"
    Draft = "DR"
    Pending = "PE"

    Food = "FO"
    Mileage = "MI"
    Equipment = "EQ"
    Other = "OT"

    # Defines drop down list for use later on the form and when defining columns
    Status_Type = [(Approved, "Approved"), (Rejected, "Rejected"), (Draft, "Draft"), (Pending, "Pending")]

    Claim_Type = [(Food, "Food"), (Mileage, "Mileage"), (Equipment, "Equipment"), (Other, "Other")]

    # Define each table column and their rules
    time = models.DateTimeField(auto_now = True)

    expense_amount = models.FloatField(validators=[MinValueValidator(0.0)])
    employee = models.ForeignKey(User, on_delete=models.CASCADE, default = id(User))
    reason = models.CharField(max_length = 2, choices= Claim_Type, default = "OT")
    evidence = models.TextField(max_length = 500)
    status = models.CharField(max_length = 2, choices= Status_Type, default = "PE")
    manager_comment = models.TextField(max_length = 500, null= True)

    class Meta:
        ordering = ["time"]
        
   
   
 


