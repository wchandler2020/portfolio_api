from rest_framework import serializers
from .models import Portfolio, Education

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('title', 'category', 'description', 'image', 'git_hub_link', 'project_link')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('category', 'year', 'title', 'description',)

    

