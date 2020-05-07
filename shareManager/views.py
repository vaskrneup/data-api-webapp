from django.http.response import JsonResponse
from django.http import HttpResponse
from dateutil.parser import parse as parse_datetime
from django.db.models import Q

from DataAPI import settings

from shareManager.NepalStockAPI import web_scraper as nepse_web_scraper
from . import models as share_manager_models
from . import serializers as share_manager_serializers


def __is_valid_api_key(key):
    return True if share_manager_models.ApiKeys.objects.filter(key=key).exists() else False


def __validate_api_key(request):
    if request.method == "GET":
        if not __is_valid_api_key(request.GET.get("api-key")):
            return JsonResponse({"error": "Invalid api key"})
    else:
        return HttpResponse("<h1>This method is not allowed !</h1><br><h3>Please select any other method !</h3>")


def __check_error(request):
    if request.method == "GET":
        return HttpResponse("<h1>Page not found !</h1>")
    else:
        return JsonResponse({"error": "internal error"})


def share_daily_price(request, start_date, end_date=None):
    api_confirm_data = __validate_api_key(request)
    if api_confirm_data:
        return api_confirm_data

    # check for setting to do scraping !
    if settings.MY_SETTINGS.get("use_scraper"):
        errors: list = []

        # try to scrap data, validate date !
        try:
            from_date: str = str(parse_datetime(start_date).date())

            if end_date:
                to_date: str = str(parse_datetime(end_date).date())
                # api call for grabbing data for range of dates !
                share_data = nepse_web_scraper.get_nepse_data(start_date=from_date, end_date=to_date)
            else:
                # api call for grabbing data for single date !
                share_data = nepse_web_scraper.get_nepse_data_for_date(date=from_date)

            # return json !
            return JsonResponse(share_data, encoder="utf-8")
        except Exception as e:
            # handle error !
            print(e)
            errors.append("Invalid start or end date")
        return JsonResponse({"errors": errors})
    else:
        # grab data from db and render !
        from_date: str = str(parse_datetime(start_date).date())

        company_transaction_cache = share_manager_models.ShareCompanyDetail.objects.all().select_related("company_name")
        errors: list = []

        try:
            if end_date:
                try:
                    to_date: str = str(parse_datetime(end_date).date())

                    company_transaction = company_transaction_cache.filter(
                        Q(company_transaction_date__gte=from_date) & Q(company_transaction_date__lte=to_date)
                    )
                except Exception as e:
                    print(e)
                    errors.append("invalid date")
                    return JsonResponse({"errors": errors})
            else:
                company_transaction = company_transaction_cache.filter(
                    company_transaction_date=from_date
                )

            company_transaction_serializer = share_manager_serializers.ShareCompanyDetailSerializer(
                company_transaction,
                many=True,
            )

            return JsonResponse({"data": company_transaction_serializer.data})
        except Exception as e:
            print(e)
            errors.append("value has an invalid date format. It must be in YYYY-MM-DD format.")
            return JsonResponse({"errors": errors})


def share_daily_final_data(request, start_date, end_date=None):
    api_confirm_data = __validate_api_key(request)
    if api_confirm_data:
        return api_confirm_data

    if settings.MY_SETTINGS.get("use_scraper"):
        pass
    else:
        # grab data from db and render !
        from_date: str = str(parse_datetime(start_date).date())

        total_transaction_cache = share_manager_models.ShareCompanyAggregate.objects.all()
        errors: list = []

        try:
            if end_date:
                try:
                    to_date: str = str(parse_datetime(end_date).date())

                    total_transaction = total_transaction_cache.filter(
                        Q(total_transaction_date__gte=from_date) & Q(total_transaction_date__lte=to_date)
                    )
                except Exception as e:
                    print(e)
                    errors.append("invalid date")
                    return JsonResponse({"errors": errors})
            else:
                total_transaction = total_transaction_cache.filter(
                    total_transaction_date=from_date
                )

            total_transaction_serializer = share_manager_serializers.ShareTransactionSerializer(
                total_transaction,
                many=True,
            )

            return JsonResponse({"data": total_transaction_serializer.data})
        except Exception as e:
            print(e)
            errors.append("value has an invalid date format. It must be in YYYY-MM-DD format.")
            return JsonResponse({"errors": errors})


def get_company_names(request):
    api_confirm_data = __validate_api_key(request)
    if api_confirm_data:
        return api_confirm_data

    return JsonResponse({"data": [{"full_name": comp.company_full_name, "short_name": comp.company_short_name} for comp
                                  in share_manager_models.ShareCompanyName.objects.all()]})
