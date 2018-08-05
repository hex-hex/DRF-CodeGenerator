class {{modelFields.entity_name}}Filter(FilterSet):
    {% for var in modelFields.child_vars[3]%}{{var[0]}} = RelatedFilter({{var[1][0]}}Filter, name='{{var[0]}}', queryset={{var[1][0]}}.objects.all())
    {% endfor %}{% for var in modelFields.child_vars[4]%}{{var[0]}} = RelatedFilter({{var[1][0]}}Filter, name='{{var[0]}}', queryset={{var[1][0]}}.objects.all())
    {% endfor %}{% if modelFields.has_base() %}date_create = DateFromToRangeFilter()
    date_update = DateFromToRangeFilter(){% endif %}
    class Meta:
        model = {{modelFields.entity_name}}
        fields = { {% for var in modelFields.child_vars[1]%}
            '{{var[0]}}': ['exact', 'in', 'startswith', 'contains'], {% endfor %}{% for var in modelFields.child_vars[2]%}
            '{{var[0]}}': ['exact', 'lt', 'gt'], {% endfor %}
        }



class {{modelFields.entity_name}}Serializer({% if modelFields.child_vars[3].__len__() + modelFields.child_vars[4].__len__() > 0  %}NestedFieldsMixin, WritableNestedModelSerializer{% else %}ModelSerializer{% endif %}):
    {% for var in modelFields.child_vars[3]%}{{var[0]}} = {{var[1][0]}}Serializer()
    {% endfor %}{% for var in modelFields.child_vars[4]%}{{var[0]}} = {{var[1][0]}}Serializer(many=True){% endfor %}{% if modelFields.has_base() %}
    user_create = HiddenField(default=CreateOnlyDefault(CurrentUserDefault()))
    user_update = HiddenField(default=CurrentUserDefault()){% endif %}
    class Meta:
        model = {{modelFields.entity_name}}
        {% if modelFields.has_base() %}read_only_fields = ('pk', 'date_create', 'date_update', 'user_create', 'user_update'){% endif %}
        fields = ('pk', {% for var in modelFields.child_vars[1]%}'{{var[0]}}', {% endfor %}{% for var in modelFields.child_vars[2]%}'{{var[0]}}',
            {% endfor %}{% for var in modelFields.child_vars[3]%}'{{var[0]}}', {% endfor %}{% for var in modelFields.child_vars[4]%}'{{var[0]}}', {% endfor %}
            {% if modelFields.has_base() %}'date_create', 'date_update', 'user_create', 'user_update'{% endif %})



class {{modelFields.entity_name}}ModelViewSet(ModelViewSet):
    queryset = {{modelFields.entity_name}}.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_class = {{modelFields.entity_name}}Filter
    serializer_class = {{modelFields.entity_name}}Serializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderFilter,)
    search_fields = ({% for var in modelFields.child_vars[1]%}'@{{var[0]}}', '${{var[0]}}', {% endfor %}{% for var in modelFields.child_vars[2]%}'={{var[0]}}', '@{{var[0]}}', {% endfor %})
    ordering_fields = '__all__'
