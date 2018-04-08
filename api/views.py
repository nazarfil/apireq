from django.conf import settings
import requests
##Import models, serializers
from contact.models import ResearchRequest
from contact.serializers import ResearchRequestSerializer, UserDataSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from contact.serializers import ContactSerializer

class ResearchRequestList(generics.ListCreateAPIView):
    queryset = ResearchRequest.objects.all()
    serializer_class = ResearchRequestSerializer
    def post(self, request, format=None):        
        serializer = ResearchRequestSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryRequestList(generics.ListCreateAPIView):
    #queryset = ResearchRequest.objects.all()
    serializer_class = ResearchRequestSerializer

    def get_queryset(self):
            """
            This view should return a list of all the purchases for
            the user as determined by the username portion of the URL.
            """
            cat = self.kwargs['category']
            return ResearchRequest.objects.filter(category=cat)

class UserDataList(APIView):
    def post(self, request, format=None):
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResearchRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResearchRequest.objects.all()
    serializer_class = ResearchRequestSerializer

class ContactList(APIView):
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            if grecaptcha_verify(request):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def grecaptcha_verify(request):
        captcha_rs = request.data.get('g-recaptcha-response')
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': captcha_rs,
            'remoteip': get_client_ip(request)
        }
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()
        print(verify_rs.get('error-codes', None) or "Unspecified error.")
        return verify_rs.get("success", False)