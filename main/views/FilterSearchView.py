from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.core.mail import send_mail
# from django.conf import settings
from main.models.FilterSearch import FilterRequest
from main.serializers.FilterSearchSR import FilterRequestSerializer


class FilterRequestView(APIView):
    def post(self, request):
        serializer = FilterRequestSerializer(data=request.data)
        if serializer.is_valid():
            filter_request = serializer.save()

            subject = "New Filter Request"
            message = f"""
            Name: {filter_request.name}
            Phone: {filter_request.phone_number}
            Email: {filter_request.email}
            Message: {filter_request.message}
            """
            # send_mail(
            #     subject,
            #     message,
            #     settings.DEFAULT_FROM_EMAIL,
            #     ["daniil0571x@gmail.com"],
            #     fail_silently=False,
            # )

            return Response({
                'success': True,
                'message': 'Request submitted successfully!'
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        filter_requests = FilterRequest.objects.all()
        serializer = FilterRequestSerializer(filter_requests, many=True, context={'request': request})
        return Response({
            'success': True,
            'message': 'Filter requests retrieved successfully!',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
