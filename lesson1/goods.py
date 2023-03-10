import datetime as dt


class Product:
    def __init__(self, price, name, valid_till,
                 category, edible=True):
        self.price = price
        self.name = name
        self.valid_till = valid_till
        self.category = category
        self.edible = edible


class Cart:
    def __init__(self, goods_list):
        self.goods_list = goods_list

    def _thursday_discount(self):
        today = dt.date.today().isoweekday()
        if today == 4:
            return 0.9
        return 1

    def calculate_total(self):
        """
        goods_list = [(item1(Product), qty), (item2, qty)]
        :return:
        """
        return sum([itm.price * qty for itm, qty in self.goods_list]) * self._thursday_discount()

"""
 [(bread, 2), (water, 1)] -> [x for x in self.goods_list] -> x = (bread, 2) |> x = (water, 1)
                             [x, y for x, y in self.goods_list] -> x = bread(Product), y = 2
                             |> bread.price * 2, |> 
"""

if __name__ == '__main__':
    water = Product(price=15, name='Blue water', valid_till='31/12/2023', category='water')
    eggs = Product(price=75, name='Chicken Eggs', valid_till='31/12/2023', category='eggs')
    bread = Product(price=25, name='White bread', valid_till='20/2/2023', category='bakery')

    cart = Cart([(water, 1), (eggs, 2), (bread, 1)])
    cart2 = Cart([(water, 3), (eggs, 1), (bread, 5)])

    print(cart.calculate_total())
    # print(cart.__thursday_discount())
    print(cart2.calculate_total())
