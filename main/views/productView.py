from rest_framework.views import APIView
from main import models
from main.serializers.productSR import Oil_filterSerializer, Filter_typeSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductView(APIView):
    def get(self, request):
        slug = request.query_params.get('slug')  # URL parametrdan olish
        if slug:
            try:
                oil_filter = models.Oil_filter.objects.get(slug=slug)
                oil_filterSR = Oil_filterSerializer(oil_filter, context={'request': request})
            except models.Oil_filter.DoesNotExist:
                return Response({'success': False, 'message': 'Mahsulot topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        else:
            oil_filters = models.Oil_filter.objects.all()
            oil_filterSR = Oil_filterSerializer(oil_filters, many=True, context={'request': request})

        data = {
            'success': True,
            'message': 'Ishladi',
            'data': oil_filterSR.data
        }
        return Response(data)

    def post(self,request):
        serializer = Filter_typeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)









    









