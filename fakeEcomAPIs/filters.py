from django_filters import FilterSet,filters
from api.models import Product

class FiltersWhichAreNotProvidedByLibrary(FilterSet):
    id = filters.NumberFilter(field_name='id',lookup_expr='exact')
    product_name = filters.CharFilter('product_name')
    product_price = filters.CharFilter('product_price')
    search = filters.CharFilter(field_name='product_name',lookup_expr='icontains')
    min = filters.NumberFilter(field_name='product_price', lookup_expr='gte')
    max = filters.NumberFilter(field_name='product_price',lookup_expr='lte')
    rating_min = filters.NumberFilter(field_name='product_rating', lookup_expr='gte')
    rating_max = filters.NumberFilter(field_name='product_rating', lookup_expr='lte')
    product_category = filters.CharFilter(method='get_category_wise_data')
    limit = filters.NumberFilter(method='get_data_limitwise')
    class Meta:
        model = Product
        fields = ['product_name','product_price']

    def get_category_wise_data(self,queryset,name,value):
        queryset = queryset.filter(product_category__category_id=value.lower())
        return queryset

    def get_data_limitwise(self,queryset,name,value):
        queryset = queryset[int(value) :]
        return queryset