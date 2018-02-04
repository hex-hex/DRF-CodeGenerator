from Structrues import EntityCode

if __name__ == '__main__':
    code = """
class Address(EntityBase):
    nation = models.ForeignKey('Nation', on_delete=models.CASCADE)
    city = models.CharField(max_length=192)
    street = models.CharField(max_length=512)
    post_code = models.IntegerField(null=True, blank=True) 
    """

    code = EntityCode(code)
