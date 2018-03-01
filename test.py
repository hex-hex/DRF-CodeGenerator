from Structrues import EntityCode

if __name__ == '__main__':
    code = """
class OrderDetail(EntityBase):
    order_header = models.ForeignKey('OrderHeader', on_delete=models.CASCADE)
    product_case = models.ForeignKey('ProductCase', null=True, blank=True, on_delete=models.CASCADE)
    unit_price = models.ForeignKey('Price', on_delete=models.SET_NULL, blank=True, null=True)
    trade_mode = models.IntegerField(default=0, choices=ProductLaunch.TRADE_MODE)
    quantity = models.PositiveIntegerField(default=1)
    fulfill_quantity = models.PositiveIntegerField(default=1)
    tax_percentage = models.FloatField(default=0)

    def __str__(self):
        return '{} {}'.format(self.quantity, self.product_case.__str__())
"""
    code = EntityCode(code)
