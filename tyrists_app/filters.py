import django_filters
from .models import Tyrs


class TyrsFilter(django_filters.FilterSet):

    class Meta:
        model=Tyrs
        fields=["TyrPoint"]

        git
        commit - a