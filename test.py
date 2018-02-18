from Structrues import EntityCode

if __name__ == '__main__':
    code = """

class OrderHeader(EntityBase):
    ORDER_STATUS = (
        (0, 'QUOTE'),
        (1, 'DRAFT'),
        (2, 'BUYER_CONFIRMED'),
        (3, 'SELLER_CONFIRMED'),
        (4, 'BOTH_CONFIRMED'),
        (5, 'SHIPPING'),
        (6, 'EXPIRED'),
        (7, 'DELETED'),
        (8, 'COMPLETED'),
    )
    order_status = models.IntegerField(choices=ORDER_STATUS, default=0)
    order_number = models.CharField(max_length=16, null=True, blank=True)
    order_from = models.ForeignKey('Company', related_name='order_from_company', null=True, blank=True)
    order_to = models.ForeignKey('Company', related_name='order_to_company', null=True, blank=True)
    bill_to = models.ForeignKey('Company', related_name='bill_to_company', null=True, blank=True)
    pay_to = models.ForeignKey('Company', related_name='pay_to_company', null=True, blank=True)
    date_order = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    
"""
    code = EntityCode(code)
