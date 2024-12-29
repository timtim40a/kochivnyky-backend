from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PerfTitle
from .serializer import PerfTitleSerializer

@api_view(['GET'])
def get_titles(request):
    titles = PerfTitle.objects.all()
    serializedData = PerfTitleSerializer(titles, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_title(request):
    data = request.data
    serializer = PerfTitleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def title_details(request, pk):
    try:
        title = PerfTitle.objects.get(pk=pk)
    except PerfTitle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        title.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        data = request.data
        serializer = PerfTitleSerializer(title, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)