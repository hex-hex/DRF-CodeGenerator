class {{modelFields.entity_name[0]}}Filter(FilterSet):
    class Meta:
        model = {{modelFields.entity_name[0]}}
        fields = { {% for var in modelFields.child_vars[1]%}
            '{{var}}': ['exact', 'in', 'startswith'], {% endfor %}{% for var in modelFields.child_vars[2]%}
            '{{var}}': ['exact', 'lt', 'gt'], {% endfor %}}


class {{modelFields.entity_name[0]}}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {{modelFields.entity_name[0]}}
        fields = ('pk', {% for var in modelFields.child_vars[1]%}'{{var}}', {% endfor %}{% for var in modelFields.child_vars[2]%}'{{var}}', {% endfor %})


class {{modelFields.entity_name[0]}}ViewSet(viewsets.ModelViewSet)}:
    queryset = {{modelFields.entity_name[0]}}.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'options', 'post', 'put']
    filter_class = {{modelFields.entity_name[0]}}Filter
    serializer_class = {{modelFields.entity_name[0]}}Serializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ({% for var in modelFields.child_vars[1]%}'@{{var}}', {% endfor %}{% for var in modelFields.child_vars[2]%}'={{var}}', {% endfor %})
    ordering_fields = '__all__'
