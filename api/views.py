from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, CompanySerializer
from .models import Company

# Create your views here.
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        # Do something with the uploaded file
        return render(request, 'upload_file.html', {'file_name': uploaded_file.name})
    else:
        return render(request, 'upload_file.html')

def query_builder(request):
    base_query = Company.objects.all()
    total_count = base_query.count()
    filters = {}
    if filters:
        base_query = base_query.filter(**filters)
        filtered_count = base_query.count()
    else:
        filtered_count = total_count
    serializer = CompanySerializer(base_query, many=True)
    company_data = serializer.data
    context = {'total_count': total_count, 'filtered_count': filtered_count, 'company_data': company_data}
    return render(request, 'query_builder.html', context)

def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    context = {'users': serializer.data}
    return render(request, 'users.html', context)

# class UserView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 user = User.objects.get(pk=pk)
#             except User.DoesNotExist:
#                 return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
#             serializer = UserSerializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             users = User.objects.all()
#             serializer = UserSerializer(users, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
