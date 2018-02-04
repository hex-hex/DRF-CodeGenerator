from Structrues import EntityCode

if __name__ == '__main__':
    code = """
class Company(EntityBase):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE)  # Enum
    address = models.ForeignKey('Address', on_delete=models.CASCADE)  # Nested
    scale = models.ForeignKey('CompanyScaleSection', on_delete=models.CASCADE)  # Enum
    establish_on = models.DateTimeField(null=True, blank=True)
    website = models.CharField(max_length=128, null=True, blank=True)
    main_business = models.CharField(max_length=128, null=True, blank=True)
    slogan = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    is_verified = models.BooleanField(default=False)  # invisible
    company_img = models.ManyToManyField('UserFile', blank=True)
 
    """

    code = EntityCode(code)
