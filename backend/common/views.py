from rest_framework import generics, permissions
from .models import Region, District, StaticPage, Setting
from .serializers import RegionSerializer, DistrictSerializer, StaticPageSerializer, SettingSerializer


class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DistrictListView(generics.ListAPIView):
    serializer_class = DistrictSerializer


    def get_queryset(self):
        region_id = self.request.query_params.gegt('region_id')
        if region_id:
            return District.objects.filter(region_id=region_id)
        return District.objects.all()


class StaticPageDetailView(generics.RetrieveAPIView):
    queryset = StaticPage.objects.filter(is_active=True)
    serializer_class = StaticPageSerializer
    lookup_field = 'slug'


class SettingView(generics.RetrieveAPIView):
    serializer_class = SettingSerializer

    def get_object(self):
        return Setting.get_settings()
