from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Products
from main.serializers.productSR import ProductsSerializer


class SearchProducts(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')

        if not query:
            return Response({
                'success': False,
                'message': 'Qidiruv so‘rovi talab qilinadi',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        products = Products.objects.filter(
            firm__name__icontains=query
        ) | Products.objects.filter(
            type__name__icontains=query
        ) | Products.objects.filter(
            article_number__icontains=query
        ) | Products.objects.filter(
            slug__icontains=query
        )

        context = {'request': request}
        products_serializer = ProductsSerializer(products, many=True, context=context)

        return Response({
            'success': True,
            'message': 'Ma’lumotlar olindi',
            'data': products_serializer.data
        }, status=status.HTTP_200_OK)

