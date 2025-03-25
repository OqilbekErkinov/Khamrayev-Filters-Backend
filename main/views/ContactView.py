from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from main.models.Contact import ContactForm
from main.serializers.ContactSR import ContactFormSerializer



class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            contact_form = serializer.save()

            subject = "New Contact"
            message = f"""
            Name: {contact_form.name}
            Phone: {contact_form.phone_number}
            Email: {contact_form.email}
            Message: {contact_form.message}
            """
            # send_mail(
            #     subject,
            #     message,
            #     settings.DEFAULT_FROM_EMAIL,
            #     ["daniil0571x@gmail.com"],
            #     fail_silently=False,
            # )

            send_mail(
                "Test Subject",
                "This is a test email.",
                "info@filters.divspan.uz",
                ["daniil0571x@gmail.com"],
                fail_silently=False,
            )

            return Response({
                'success': True,
                'message': 'Request submitted successfully!'
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        contact_form = ContactForm.objects.all()
        serializer = ContactFormSerializer(contact_form, many=True, context={'request': request})
        return Response({
            'success': True,
            'message': 'Contact forms was successfully!',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
