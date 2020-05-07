from django.urls import path

from shareManager import views as nepalstock_view

app_name = "shareManager"

urlpatterns = [
    path(
        "daily-price/<str:start_date>/<str:end_date>/",
        view=nepalstock_view.share_daily_price,
        name="daily-share-value-range"
    ),
    path(
        "daily-price/<str:start_date>/",
        view=nepalstock_view.share_daily_price,
        name="daily-share-value"
    ),
    path(
        "daily-total-transaction/<str:start_date>/<str:end_date>/",
        view=nepalstock_view.share_daily_final_data,
        name="daily-share-total-value-range"
    ),
    path(
        "daily-total-transaction/<str:start_date>/",
        view=nepalstock_view.share_daily_final_data,
        name="daily-share-total-value"
    ),
    path(
        "company-names/",
        view=nepalstock_view.get_company_names,
        name="daily-share-total-value"
    ),
    path(
        "company-names/",
        view=nepalstock_view.get_company_names,
        name="daily-share-total-value"
    ),
]
