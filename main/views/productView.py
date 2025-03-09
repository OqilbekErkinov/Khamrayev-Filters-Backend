from rest_framework.views import APIView
from main import models
from main.serializers.productSR import ProductsSerializer, Filter_typeSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductView(APIView):
    def get(self, request):
        slug = request.query_params.get('slug')  # URL parametrdan olish
        if slug:
            try:
                product = models.Products.objects.get(slug=slug)
                productSR = ProductsSerializer(product, context={'request': request})
            except models.Products.DoesNotExist:
                return Response({'success': False, 'message': 'Mahsulot topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        else:
            products = models.Products.objects.all()
            productSR = ProductsSerializer(products, many=True, context={'request': request})

        data = {
            'success': True,
            'message': 'Ishladi',
            'data': productSR.data
        }
        return Response(data)

    def post(self,request):
        serializer = Filter_typeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class ProductDetailView(APIView):
    def get(self, request, product_id):
        try:
            product = models.Products.objects.get(id=product_id)
            productSR = ProductsSerializer(product, context={'request': request})
            return Response({
                'success': True,
                'message': 'Mahsulot topildi',
                'data': productSR.data
            }, status=status.HTTP_200_OK)
        except models.Products.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Mahsulot topilmadi'
            }, status=status.HTTP_404_NOT_FOUND)










    









