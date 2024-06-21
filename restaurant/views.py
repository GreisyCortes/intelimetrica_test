import numpy as np
from django.db import connection
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantAllView(APIView):
    def get(self, request, *args, **kwargs):
        result = Restaurant.objects.all()
        serializers = RestaurantSerializer(result, many=True)
        return Response({'status': 'success', "data": serializers.data}, status=200)


class RestaurantCreateView(APIView):
    def post(self, request, **kwargs):
        serializer = RestaurantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "created", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class RestaurantUpdateView(APIView):
    def put(self, request, **kwargs):
        print(request.data['id'])
        rst = Restaurant.objects.get(id=request.data['id'])
        if rst:
            rst.rating = request.data['rating']
            rst.name = request.data['name']
            rst.site = request.data['site']
            rst.email = request.data['email']
            rst.phone = request.data['phone']
            rst.street = request.data['street']
            rst.city = request.data['city']
            rst.state = request.data['state']
            rst.lat = request.data['lat']
            rst.lng = request.data['lng']
            rst.save()
            return Response({"status": "updated", "data": request.data['id']}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": None}, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDeleteView(APIView):
    def delete(self, request, **kwargs):
        rest = Restaurant.objects.get(id=self.kwargs['id'])
        if rest:
            rest.delete()
            return Response({"status": "deleted", "data": None}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": None}, status=status.HTTP_400_BAD_REQUEST)


class RestaurantStatisticsView(APIView):
    def validate_coordinates(self, lat, lon):
        if not (-90 <= lat <= 90):
            raise ValueError("Latitud fuera de rango. Debe estar entre -90 y 90.")
        if not (-180 <= lon <= 180):
            raise ValueError("Longitud fuera de rango. Debe estar entre -180 y 180.")

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        """
        Calcula la distancia Haversine entre dos puntos en kilómetros.
        """
        self.validate_coordinates(lat1, lon1)
        self.validate_coordinates(lat2, lon2)

        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT
                6371 * 2 * ASIN(SQRT(
                    POWER(SIN(RADIANS(%s - %s) / 2), 2) +
                    COS(RADIANS(%s)) * COS(RADIANS(%s)) *
                    POWER(SIN(RADIANS(%s - %s) / 2), 2)
                )) AS distance
        """, [lat1, lat2, lon2, lon1, lat1, lat2])
            result = cursor.fetchone()
        return result[0]

    def get(self, request, **kwargs):
        latitude = float(request.query_params.get('latitude'))
        longitude = float(request.query_params.get('longitude'))
        radius = float(request.query_params.get('radius'))
        # center = Point(float(longitude), float(latitude), srid=4326)

        result = Restaurant.objects.all()
        rating = []
        for res in result:
            if self.haversine_distance(latitude, longitude, res.lat, res.lng) < radius:
                print(res.id)
                rating.append(res.rating)
        print(len(rating))
        return Response({"count": len(rating), "avg": np.average(rating), "std": np.std(rating)}, status=status.HTTP_200_OK)

