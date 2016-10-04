from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 
from django.http import JsonResponse

# class Get_listList(generics.ListCreateAPIView):
#  queryset = Ticket.objects.all()
#  serializer_class = Get_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    # add more status code according to your need
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)



def get_queryset(request):

  from push_notifications.models import APNSDevice, GCMDevice

  # device = GCMDevice.objects.get(registration_id=gcm_reg_id)
  # device.send_message("You've got mail")
  # device.send_message(None, extra={"foo": "bar"})

  # APNSDevice.objects.all().delete();
  # APNSDevice.objects.create(name="uzma",registration_id="22c5f99004c65b813a3d3e43bffdf88dbffbba83e251d61561fdc6d769961ae9",device_id="918775655fe541759f2bd24704df0b74",active="true");

  apns_token="22c5f99004c65b813a3d3e43bffdf88dbffbba83e251d61561fdc6d769961ae9";
  device = APNSDevice.objects.get(registration_id=apns_token)
  device.send_message("You've got mail") # Alert message may only be sent as text.
  device.send_message(None, badge=5) # No alerts but with badge.
  device.send_message(None, badge=1, extra={"foo": "bar"}) # Silent message with badge and added custom data.

  # from push_notifications.models import APNSDevice, GCMDevice

  # devices = GCMDevice.objects.filter(user__first_name="James")
  # devices.send_message("Happy name day!")

  fields=[];
  # fields=({
  #   'apns_devices':APNSDevice.objects.all()
  #   })
  

  return JsonResponse((list(fields)),safe=False)

  
  # import sys


  # from django.db import connection, transaction
  # cursor = connection.cursor()
  
  # cursor.execute("SELECT * FROM tbl_department")
  # row = cursor.fetchall()

  # print >> sys.stderr,row
  
  # fields = []
  # fields.append(
  #         {
  #          'feeds':row,
  #          }
  #       )
    
  
 
  # return JsonResponse((list(fields)),safe=False)
  