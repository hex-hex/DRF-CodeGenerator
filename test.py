from Structrues import EntityCode

if __name__ == '__main__':
    code = """
class Inventory(EntityBase):
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    product_case = models.ForeignKey('ProductCase', on_delete=models.CASCADE)
    adjustment_time = models.DateTimeField(default=now, blank=True) 
    quantity = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    inventory_type = models.IntegerField(default=1, choices=INVENTORY_TYPE)
"""
    code = EntityCode(code)
