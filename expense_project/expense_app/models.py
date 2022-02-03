from multiprocessing import Manager
from django.db import models
import datetime
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Expense(models.Model):

    # reduces stored data in table to two letters these might be changed to their own tables later
    #status
    Approved = "AP"
    Rejected = "RE"
    Draft = "DR"
    Pending = "PE"
    #expense categories
    Accommodation = "AC"
    Subsistence = "SU"
    Mileage = "MI"
    Staff_entertainment = "SE"
    Client_entertainment = "CE"
    Other = "OT"
    Flights = "FL"
    Other_travel = "OT"
    #currencies
    Euro = "EU"
    GBP = "GB"
    USD = "US"
    SGD = "SG"
    AUD = "AU"
    CHF = "CH"
    HKD = "HK"

    # Defines drop down list for use later on the form and when defining columns
    Status_Type = [(Approved, "Approved"), (Rejected, "Rejected"), (Draft, "Draft"), (Pending, "Pending")]

    Claim_Type = [(Accommodation, "Accommodation"), (Client_entertainment, "Client entertainment (Incl VAT)"), (Flights, "Flights"), (Mileage, "Mileage"), (Other, "Other"), (Other_travel, "Other travel"), (Staff_entertainment, "Staff entertainment"), (Subsistence, "Subsistence")]

    Currency_Type = [(Euro, "Euro"), (GBP, "Pound Sterling"), (USD, "US Dollar"), (SGD, "Singaporean Dollar"), (AUD, "Australian Dollar"), (CHF, "Swiss Franc"), (HKD, "Hong Kong Dollar")]

    # Define each table column and their rules
    time = models.DateTimeField(auto_now = True)

    expense_amount = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    VAT_amount = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, default = id(User))
    catagory = models.CharField(max_length = 2, choices= Claim_Type, default = "OT")
    persons_seen = models.CharField(max_length = 50, blank=False, default = "Provide the name(s) of the person you saw.")
    information = models.TextField(max_length = 500, default = "Explaination of expense, including names for entertaining expenses and postcodes for mileage claims.")
    status = models.CharField(max_length = 2, choices= Status_Type, default = "PE")
    manager_comment = models.TextField(max_length = 500, null= True)
    expense_date = models.CharField(max_length = 25, blank=False, default = 'Provide date DD/MM/YY or date range DD/MM/YY-DD/MM/YY')
    currency = models.CharField(max_length = 2, choices = Currency_Type, default = "GB")

    class Meta:
        ordering = ["time"]
        