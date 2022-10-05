from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import google_get_access_token, google_get_user_info
from django.contrib.auth.models import User

# Create your views here.
class GoogleCallbackHandler(APIView):
    def post(self, request):
        auth_code = request.data.get('auth_code', False)

        if(auth_code):
            access_token = google_get_access_token(auth_code)
            userdata = google_get_user_info(access_token)

            data = {
                'auth_code': auth_code,
                'access_token': access_token
            }

            user_email = userdata['email']
            # now check if this user exists. if exists, use simplejwt to return an access and refresh token for his account
            # if user does not exist, create a user with that email, and take him to profile completion page
            # try:
            #     User.objects.get(email=email)
            #     # create tokens and send
            # except:
            #     User.objects.create()


            
            return Response(userdata)
        else:
            return Response({'msg':'no code'}, status=status.htt)
        
