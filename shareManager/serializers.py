from rest_framework import serializers

from . import models as share_manager_models


class ShareCompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = share_manager_models.ShareCompanyDetail
        fields = (
            "company_full_name", "company_short_name",
            "company_transaction_date", "company_transaction_time",
            "company_sn", "company_num_of_transaction", "company_max_price", "company_min_price",
            "company_closing_price", "company_traded_shares", "company_total_amount",
            "company_previous_closing", "company_difference",
        )


class ShareTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = share_manager_models.ShareCompanyAggregate
        fields = (
            "total_transaction_date", "total_transaction_time",
            "total_amount", "total_quantity", "total_num_of_transactions",
        )
