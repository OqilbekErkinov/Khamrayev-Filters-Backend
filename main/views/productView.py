from rest_framework.views import APIView
from main import models
from main.serializers.productSR import ProductsSerializer, Filter_typeSerializer, \
    ManafacturerSerializer, Brands_of_equipmentSerializer, EquipmentSerializer, SubCategorySerializer
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

    # def post(self,request):
    #     serializer = Filter_typeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)


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


class SubCategoryView(APIView):
    def get(self, request):
        slug = request.query_params.get('slug')
        if slug:
            try:
                subcategory = models.SubCategory.objects.get(slug=slug)
                subcategorySR = SubCategorySerializer(subcategory, context={'request': request})
            except models.SubCategory.DoesNotExist:
                return Response({'success': False, 'message': 'Subkategoriya topilmadi'},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            subcategories = models.SubCategory.objects.all()
            subcategorySR = SubCategorySerializer(subcategories, many=True, context={'request': request})

        data = {
            'success': True,
            'message': 'Ishladi',
            'data': subcategorySR.data
        }
        return Response(data, status=status.HTTP_200_OK)


class Filter_typeView(APIView):
    def get(self, request):
        slug = request.query_params.get('slug')
        if slug:
            try:
                filter_types = models.Filter_types.objects.get(slug=slug)
                filter_typeSR = Filter_typeSerializer(filter_types, context={'request': request})
            except models.Filter_types.DoesNotExist:
                return Response({'success': False, 'message': 'Mahsulot topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        else:
            filter_types = models.Filter_types.objects.all()
            filter_typeSR = Filter_typeSerializer(filter_types, many=True, context={'request': request})
        data = {
            'success': True,
            'message': 'Ishladi',
            'data': filter_typeSR.data
        }
        return Response(data)


class ManafacturerView(APIView):
    def get(self, request):
        slug = request.query_params.get('slug')
        if slug:
            try:
                manafacturers = models.Manafacturers.objects.get(slug=slug)
                manafacturerSR = ManafacturerSerializer(manafacturers, context={'request': request})
            except models.Manafacturers.DoesNotExist:
                return Response({'success': False, 'message': 'Mahsulot topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        else:
            manafacturers = models.Manafacturers.objects.all()
            manafacturerSR = ManafacturerSerializer(manafacturers, many=True, context={'request': request})
        data = {
            'success': True,
            'message': 'Ishladi',
            'data': manafacturerSR.data
        }
        return Response(data)


class Brands_of_equipmentView(APIView):
    def get(self, request):
        slug = request.query_params.get('slug')
        if slug:
            try:
                brands_of_equipments = models.Brands_of_equipments.objects.get(slug=slug)
                brands_of_equipmentsSR = Brands_of_equipmentSerializer(brands_of_equipments, context={'request': request})
            except models.Brands_of_equipments.DoesNotExist:
                return Response({'success': False, 'message': 'Mahsulot topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        else:
            brands_of_equipments = models.Brands_of_equipments.objects.all()
            brands_of_equipmentsSR = Brands_of_equipmentSerializer(brands_of_equipments, many=True, context={'request': request})
        data = {
            'success': True,
            'message': 'Ishladi',
            'data': brands_of_equipmentsSR.data
        }
        return Response(data)


class EquipmentView(APIView):
    def get(self, request):
        slug = request.query_params.get('slug')
        if slug:
            try:
                equipments = models.Equipments.objects.get(slug=slug)
                equipmentSR = EquipmentSerializer(equipments, context={'request': request})
            except models.Equipments.DoesNotExist:
                return Response({'success': False, 'message': 'Mahsulot topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        else:
            equipments = models.Equipments.objects.all()
            equipmentSR = EquipmentSerializer(equipments, many=True, context={'request': request})
        data = {
            'success': True,
            'message': 'Ishladi',
            'data': equipmentSR.data
        }
        return Response(data)