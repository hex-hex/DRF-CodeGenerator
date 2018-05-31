from Structrues import EntityCode

if __name__ == '__main__':
    code = """

class ArticleTag(EntityBase):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

"""
    code = EntityCode(code)
