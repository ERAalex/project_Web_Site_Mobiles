from decimal import Decimal
from django.conf import settings
from mobiles.models import all_products, Top_Models



class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart



    # перебираем товары в корзине
    def __iter__(self):
        products_ids = self.cart.keys()
        # получаем товары и добавляем их в корзину
        products = all_products.objects.filter(id__in=products_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item



    # считаем сколько товаров в корзине
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())





    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        # тут идет сериализация в json, поэтому цену передаем в str т.к json принимает только строку
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()



    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True



    # удаляем товар
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()




    # получение общей стоимости
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())



    # полная очистка корзины в сессии
    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True