# from django.contrib.auth import authenticate
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from main.serializers.register_loginSR import RegisterSerializer, LoginSerializer
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.tokens import RefreshToken
#
#
# User = get_user_model()
#
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "Регистрация успешна!"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data["email"]
#             password = serializer.validated_data["password"]
#             user = authenticate(email=email, password=password)
#
#             if user:
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     "token": {
#                         "access": str(refresh.access_token),
#                         "refresh": str(refresh)
#                     }
#                 }, status=status.HTTP_200_OK)
#
#             return Response({"error": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
