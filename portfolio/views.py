from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Portfolio, Education
from .serializers import PortfolioSerializer, EducationSerializer

@api_view(['GET'])
def portfolio_list(request):
    portfolio_items = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolio_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def education_list(request):
    education_items = Education.objects.all()
    serializer = EducationSerializer(education_items, many=True)
    return Response(serializer.data)
