from Structrues import EntityCode

if __name__ == '__main__':
    code = """

class Industry(models.Model):
    name = models.CharField(max_length=128)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    """

    code = EntityCode(code)
