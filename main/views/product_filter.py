from rest_framework.views import APIView
from main import models
from main.serializers.productSR import ProductsSerializer, Filter_typeSerializer, \
    ManafacturerSerializer, Brands_of_equipmentSerializer, EquipmentSerializer
from rest_framework.response import Response
from rest_framework import status


class TypeFilter(APIView):
    def get(self, request):
        type_id = request.query_params.get('type_id')
        if not type_id:
            return Response({
                'success': False,
                'message': 'type_id parametri talab qilinadi',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)
        products = models.Products.objects.filter(type=type_id)
        context = {'request': request}
        productsr = ProductsSerializer(products, many=True, context=context)
        return Response({
            'success': True,
            'message': 'Ma’lumotlar olindi',
            'data': productsr.data
        }, status=status.HTTP_200_OK)


class FirmFilter(APIView):
    def get(self, request):
        firm_id = request.query_params.get('firm_id')
        if not firm_id:
            return Response({
                'success': False,
                'message': 'firm_id parametri talab qilinadi',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)
        products = models.Products.objects.filter(firm=firm_id)
        context = {'request': request}
        productSR = ProductsSerializer(products, many=True, context=context)
        return Response({
            'success': True,
            'message': 'Ma’lumotlar olindi',
            'data': productSR.data
        }, status=status.HTTP_200_OK)