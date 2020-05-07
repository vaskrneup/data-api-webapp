from django.contrib import admin

from .models import (ShareCompanyName, ShareCompanyDetail, ShareCompanyAggregate, ApiKeys)


class ShareCompanyNameAdmin(admin.ModelAdmin):
    list_display = ("company_full_name", "company_short_name")


class ShareCompanyDetailAdmin(admin.ModelAdmin):
    list_display = ("company_transaction_date", "company_name", "company_closing_price")


class ShareCompanyAggregateAdmin(admin.ModelAdmin):
    list_display = ("total_transaction_date", "total_quantity", "total_num_of_transactions")


admin.site.register(ShareCompanyName, ShareCompanyNameAdmin)
admin.site.register(ShareCompanyDetail, ShareCompanyDetailAdmin)
admin.site.register(ShareCompanyAggregate, ShareCompanyAggregateAdmin)
admin.site.register(ApiKeys)
