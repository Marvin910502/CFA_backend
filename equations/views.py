import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

from equations.models import Parking, Vehicle
from equations.serializers import VehicleSerializer, ParkingSerializer

# Create your views here.


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def add_vehicle(request):

    """Example of request"""
    # request headers => {
    #     "Authorization": "123"
    # }
    # request body => {
    #     "car_registration": "<VALUE>",
    #     "color": "<VALUE>",
    #     "size": "<VALUE>",
    #     "KMs_for_liters": "<VALUE>",
    # }

    success = False
    status_code = status.HTTP_401_UNAUTHORIZED
    message = 'The vehicle was not saved'
    if request.method == 'POST':
        if request.headers.get('Authorization', '123'):
            request_body = json.loads(request.body)
            Vehicle.objects.create(
                car_registration=request_body.get('car_registration'),
                color=request_body.get('color'),
                size=request_body.get('size'),
                KMs_for_liter=request_body.get('KMs_for_liters'),
            )
            message = 'The Vehicle was saved with success'
            status_code = status.HTTP_201_CREATED
            success = True
        else:
            message = "You don't have authorization for this action"

        response = {
            "success": success,
            "status_code": status_code,
            "message": message,
        }
        return Response(response, status=status_code)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def view_vehicles(request):

    """Example of request"""
    # request headers => {
    #     "Authorization": "123"
    # }

    success = False
    status_code = status.HTTP_401_UNAUTHORIZED
    message = 'Vehicle not found'
    vehicles_list = []
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        message = 'The list vehicles was founded with success'
        status_code = status.HTTP_201_CREATED
        success = True

        for vehicle in vehicles:
            vehicles_list.append(
                {
                    'id': vehicle.id,
                    'car_registration': vehicle.car_registration,
                    'color': vehicle.color,
                    'size': vehicle.size,
                    'KMs_for_liter': vehicle.KMs_for_liter,
                }
            )

    else:
        message = "You don't have authorization for this action"

    return Response(vehicles_list, status=status_code)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def delete_vehicle(request, vehicle_id):

    """Example of request"""
    # request headers => {
    #     "Authorization": "123",
    #     "vehicle_id": "<VALUE>"
    # }

    success = False
    status_code = status.HTTP_401_UNAUTHORIZED
    message = 'The vehicle was not saved'
    if request.method == 'DELETE':
        if request.headers.get('Authorization', '123'):
            vehicle = Vehicle.objects.get(id=vehicle_id)
            vehicle.delete()
            message = 'The Vehicle was saved with success'
            status_code = status.HTTP_201_CREATED
            success = True
        else:
            message = "You don't have authorization for this action"

        response = {
            "success": success,
            "status_code": status_code,
            "message": message,
        }
        return Response(response, status=status_code)


@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))
def edit_vehicle(request, vehicle_id):

    """Example of request"""
    # request headers => {
    #     "Authorization": "123"
    # }
    # request body => {
    #     "car_registration": "<VALUE>",
    #     "color": "<VALUE>",
    #     "size": "<VALUE>",
    #     "KMs_for_liters": "<VALUE>",
    # }

    success = False
    status_code = status.HTTP_401_UNAUTHORIZED
    message = 'The vehicle was not update'
    if request.method == 'POST':
        if request.headers.get('Authorization', '123'):
            request_body = json.loads(request.body)
            vehicle = Vehicle.objects.get(id=vehicle_id)
            vehicle.car_registration = request_body.get('car_registration')
            vehicle.color = request_body.get('color')
            vehicle.size = request_body.get('size')
            vehicle.KMs_for_liter = request_body.get('KMs_for_liters')
            vehicle.save()
            message = 'The Vehicle was updated with success'
            status_code = status.HTTP_201_CREATED
            success = True
        else:
            message = "You don't have authorization for this action"

        response = {
            "success": success,
            "status_code": status_code,
            "message": message,
        }
        return Response(response, status=status_code)

    if request.method == 'GET':
        vehicle_data = {}
        if request.headers.get('Authorization', '123'):
            vehicle = Vehicle.objects.get(id=vehicle_id)

            vehicle_data = {
                    'id': vehicle.id,
                    'car_registration': vehicle.car_registration,
                    'color': vehicle.color,
                    'size': vehicle.size,
                    'KMs_for_liter': vehicle.KMs_for_liter,
                }

            message = 'The Vehicle was updated with success'
            status_code = status.HTTP_201_CREATED
            success = True
        else:
            message = "You don't have authorization for this action"

        response = {
            "success": success,
            "status_code": status_code,
            "message": message,
            "vehicle": vehicle_data
        }
        return Response(response, status=status_code)