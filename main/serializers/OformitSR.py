from rest_framework import serializers
from main.models.Oformit import OformitProducts, OformitProductItem
from main.models.product import Products


class ProductSerializer(serializers.ModelSerializer):

    firm = serializers.StringRelatedField()
    type = serializers.StringRelatedField()

    class Meta:
        model = Products
        fields = ['article_number', 'firm', 'type']


class OformitProductItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OformitProductItem
        fields = ['product', 'quantity']


class OformitProductsSerializer(serializers.ModelSerializer):
    products = serializers.ListField(write_only=True)
    ordered_products = OformitProductItemSerializer(source='oformitproductitem_set', many=True, read_only=True)

    class Meta:
        model = OformitProducts
        fields = ['name', 'phone_number', 'email', 'address', 'products', 'ordered_products']

    def create(self, validated_data):
        products_data = validated_data.pop('products', [])
        oformit_products = OformitProducts.objects.create(**validated_data)

        for product_data in products_data:
            article_number = product_data.get('article_number')
            quantity = product_data.get('quantity', 1)

            try:
                product = Products.objects.get(article_number=article_number)
                OformitProductItem.objects.create(
                    oformit=oformit_products,
                    product=product,
                    quantity=quantity
                )
            except Products.DoesNotExist:
                raise serializers.ValidationError(
                    {"error": f"Product with article_number {article_number} not found"}
                )
        return oformit_products
