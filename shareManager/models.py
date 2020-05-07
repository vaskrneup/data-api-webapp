from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ShareCompanyName(models.Model):
    company_full_name = models.CharField("Full Name", max_length=256, null=False, blank=False, unique=True)
    company_short_name = models.CharField("Short Name", max_length=20, null=True, blank=True, unique=True)

    def __str__(self):
        return self.company_full_name


class ShareCompanyAggregate(models.Model):
    total_transaction_date = models.DateField("Share Date", null=False, blank=False)
    total_transaction_time = models.TimeField("share Time", null=False, blank=False)

    total_amount = models.FloatField("Total Amount Rs.")
    total_quantity = models.IntegerField("Total Quantity")
    total_num_of_transactions = models.IntegerField("Total Number of Transactions")

    def __str__(self):
        return str(self.total_transaction_date)


class ShareCompanyDetail(models.Model):
    company_name = models.ForeignKey(ShareCompanyName, on_delete=models.CASCADE)

    company_transaction_date = models.DateField("Share Date", null=False, blank=False)
    company_transaction_time = models.TimeField("share Time", null=False, blank=False)

    company_sn = models.IntegerField("Daily ID", null=False, blank=False)
    company_num_of_transaction = models.IntegerField("Total Number of Transaction", null=False, blank=False)
    company_max_price = models.FloatField("Company Max Price", null=False, blank=False)
    company_min_price = models.FloatField("Company Min Price", null=False, blank=False)
    company_closing_price = models.FloatField("Company Closing Price", null=False, blank=False)
    company_traded_shares = models.IntegerField("Company Traded Shares", null=False, blank=False)
    company_total_amount = models.FloatField("Company Total Transaction Amount", null=False, blank=False)
    company_previous_closing = models.FloatField("Company Closing Price", null=False, blank=False)
    company_difference = models.FloatField("Company Difference", null=False, blank=False)

    @property
    def company_full_name(self):
        return self.company_name.company_full_name

    @property
    def company_short_name(self):
        return self.company_name.company_short_name

    def __str__(self):
        return str(self.company_transaction_date)


class ApiKeys(models.Model):
    key = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return self.key

