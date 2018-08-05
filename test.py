from Structrues import EntityCode

if __name__ == '__main__':
    code = """

class Task(EntityBase):
    TASK_STATUS = (
        (0, 'DRAFT'),
        (1, 'PUBLISHED'),
        (2, 'EXPIRED'),
    )
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.SET_NULL)
    task_code = models.CharField(max_length=15, null=True, blank=True)
    task_title = models.CharField(max_length=64)
    status = models.IntegerField(default=0, choices=TASK_STATUS)
    description = models.CharField(max_length=1023, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    task_file = models.ManyToManyField('UserFile', blank=True)  # log it
    reward = models.ForeignKey('Price', null=True, blank=True, on_delete=models.CASCADE)
    link = models.CharField(max_length=64, default='#')

"""
    code = EntityCode(code)
