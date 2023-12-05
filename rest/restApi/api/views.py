from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Users
from .serializers import UserSerializer

@api_view(['GET'])
def getData(request):
    # Dummy 'data'
    # person = {'name':'jonny','age':29}
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)