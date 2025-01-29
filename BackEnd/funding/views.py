from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Funding
from .serializers import FundingSerializer

class FundingViewSet(viewsets.ViewSet):
    """
    A ViewSet for listing, retrieving, creating, updating, and deleting funding instances.
    """

    def list(self, request):
        """
        List all funding instances.
        """
        fundings = Funding.objects.all()
        serializer = FundingSerializer(fundings, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new funding instance.
        """
        serializer = FundingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a single funding instance.
        """
        try:
            funding = Funding.objects.get(pk=pk)
        except Funding.DoesNotExist:
            return Response({'error': 'Funding not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FundingSerializer(funding)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update an existing funding instance.
        """
        try:
            funding = Funding.objects.get(pk=pk)
        except Funding.DoesNotExist:
            return Response({'error': 'Funding not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FundingSerializer(funding, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a funding instance.
        """
        try:
            funding = Funding.objects.get(pk=pk)
        except Funding.DoesNotExist:
            return Response({'error': 'Funding not found.'}, status=status.HTTP_404_NOT_FOUND)
        funding.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
