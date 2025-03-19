from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from main.models.Oformit import OformitProducts, OformitProductItem
from main.serializers.OformitSR import OformitProductsSerializer


class OformitProductsView(APIView):
    def post(self, request):
        serializer = OformitProductsSerializer(data=request.data)

        if serializer.is_valid():
            oformit_products = serializer.save()

            subject = "Oformit products"
            message = f"""
            Name: {oformit_products.name}
            Phone: {oformit_products.phone_number}
            Email: {oformit_products.email}
            Address: {oformit_products.address}

            Ordered Products:
            """
            ordered_items = OformitProductItem.objects.filter(oformit=oformit_products)
            for item in ordered_items:
                message +=  f"\n" \
                            f"\t\tArticle: {item.product.article_number}\n" \
                            f"\t\tQuantity: {item.quantity}\n" \
                            f"\t\tType: {item.product.type}\n" \
                            f"\t\tFirm: {item.product.firm}\n"
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ["daniil0571x@gmail.com"],
                fail_silently=False,
            )

            return Response({
                'success': True,
                'message': 'Request submitted successfully!',
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        oformit_products = OformitProducts.objects.all()
        serializer = OformitProductsSerializer(oformit_products, many=True)
        return Response({
            'success': True,
            'message': 'Oformit Products retrieved successfully!',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
