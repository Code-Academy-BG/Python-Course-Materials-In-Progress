import json
import os

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class OrdersAPI(APIView):
    def get(self, request):
        """
        You will receive date parameter, and if not received you should a bad request status.
        For statuses use the imported "status" module
        """

        if "date" not in request.query_params:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        with open(os.path.join(settings.BASE_DIR, "test_data", "Orders_09_15_2021.json")) as orders_data:
            data_loaded = json.load(orders_data)

        # Add OrdersGrouperData class that should return
        # Orders data with grouped products by "location".
        # It also should return information on bad tolocations, where bad tolocations are those used
        # across multiple Orders.
        # You may, or you may not use several additional grouping and / or error collecting classes

        # By default, the Response status return status 200 which is totally fine.
        return Response(data_loaded)
