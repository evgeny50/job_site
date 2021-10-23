from rest_framework import serializers

from vacancy.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = (
            'title', 'specialty', 'company', 'skills',
            'description', 'salary_min', 'salary_max'
        )