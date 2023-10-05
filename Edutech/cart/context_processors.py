from cart.models import Cart
def counter(request):
    item_counts = 0
    if request.user.is_authenticated:

        user=request.user

        try:
            carts=Cart.objects.filter(user=user)
            for i in carts:
                item_counts+=i.quantity
        except Cart.DoesNotExist:
            item_counts=0
    return {'item_count':item_counts}