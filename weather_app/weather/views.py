"""
weather.views
-------------
Weather API Views
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from weather.constants import ApiViewConstants
from weather.open_weather_utils import OpenWeather


class WeatherAPI(APIView):
    """
    API view for retrieve Weather data for a specific city
    """

    def get(self, request, *args, **kwargs):

        city_name = request.GET.get('city')
        country_slug = request.GET.get('country')

        if city_name is None or country_slug is None:
            message_error = f"The request must be made with country slug " \
                f"and city slug, current are city {city_name} and country " \
                f"{country_slug}"
            return Response(
                data={"message_error": message_error},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            open_weather = OpenWeather(
                city_name=city_name,
                country_slug=country_slug
            )

            data_response = open_weather.retrieve_weather_data()
            if data_response.get(ApiViewConstants.ERROR_MESSAGE.value):
                return Response(
                    data=data_response,
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response(data=data_response, status=status.HTTP_200_OK)

        except:
            import traceback
            bad_response_data = dict(
                message_error=f"The API crashed due {traceback.format_exc()}",
            )
            return Response(
                data=bad_response_data,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class WeatherLogAPI(APIView):
    """
    API view for retrieve Weather data for a specific city
    """

    def get(self, request, *args, **kwargs):

        city_name = request.GET.get('city')
        country_slug = request.GET.get('country')

        if city_name is None or country_slug is None:
            message_error = f"The request must be made with country slug " \
                f"and city slug, current are city {city_name} and country " \
                f"{country_slug}"
            return Response(
                data={"message_error": message_error},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            open_weather = OpenWeather(
                city_name=city_name,
                country_slug=country_slug
            )

            data_response = open_weather.retrieve_weather_data()
            if data_response.get(ApiViewConstants.ERROR_MESSAGE.value):
                return Response(
                    data=data_response,
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response(data=data_response, status=status.HTTP_200_OK)

        except:
            import traceback
            bad_response_data = dict(
                message_error=f"The API crashed due {traceback.format_exc()}",
            )
            return Response(
                data=bad_response_data,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
