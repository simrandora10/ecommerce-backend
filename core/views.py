from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .models import Product, Cart, CartItem, Order, OrderItem
from .serializers import (
    ProductSerializer,
    CartSerializer,
    OrderSerializer
)


# ---------------------- PRODUCT LIST ----------------------
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# ---------------------- PRODUCT DETAIL ----------------------
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


# ---------------------- REGISTER ----------------------
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'User registered successfully'}, status=201)


# ---------------------- CART VIEW ----------------------
class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


# ---------------------- ADD TO CART ----------------------
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        cart, created = Cart.objects.get_or_create(user=request.user)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        item.quantity += int(quantity)
        item.save()

        return Response({"message": "Added to cart successfully"})


# ---------------------- PLACE ORDER ----------------------
class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)

        if cart.items.count() == 0:
            return Response({"error": "Cart is empty"}, status=400)

        total = 0
        for item in cart.items.all():
            price = item.product.discount_price or item.product.price
            total += price * item.quantity

        order = Order.objects.create(
            user=user,
            total_price=total
        )

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.discount_price or item.product.price
            )

            # reduce stock
            item.product.stock -= item.quantity
            item.product.save()

        cart.items.all().delete()

        return Response({"message": "Order placed successfully"})


# ---------------------- ORDER HISTORY ----------------------
class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
