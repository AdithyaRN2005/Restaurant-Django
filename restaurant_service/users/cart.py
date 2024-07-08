from django.conf import settings
from .models import Item

class Cart(object):
    def __init__(self,request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session.get(settings.CART_SESSION_ID, {})

        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['item'] = Item.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = int(item['item'].price*item['quantity'])
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())        
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    def add(self, item_id, quantity=1, update_quantity=False):
        item_id = str(item_id)

        if item_id not in self.cart:
            self.cart[item_id] = {'quantity':quantity, 'id':item_id}

        if update_quantity:
            self.cart[item_id]['quantity']+= int(quantity)
            print(self.cart[item_id]['quantity'])
            if self.cart[item_id]['quantity']==0:
                self.remove(item_id)
        self.save()

    def remove(self, item_id):
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()
    
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified=True
        

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['item'] = Item.objects.get(pk=p)
        return int(sum(item['item'].price * item['quantity'] for item in self.cart.values()))
    
    def get_cart_items_id(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(pk__in=item_ids)
        return item_ids