from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Like
from coffee_api.models import Coffee
from .serializers import LikeSerializer




class CoffeeLikesNewAPIView(APIView):
    def post(self, request, coffee_id):
        user_name = request.user  # Accessing the username from the request
        coffee_id = coffee_id
        # print(user_name, 'user name')
        # print("Type of var_str:", type(coffee_id))
        print(request)
        try:
            coffee = Coffee.objects.get(id=coffee_id)
            if not coffee.coffee_likes.filter(user_name=user_name).exists():
                # User has not liked the coffee, create a new Like instance
                like = Like.objects.create(user_name=user_name)
                coffee.coffee_likes.add(like)
                serializer = LikeSerializer(like)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'You already like this coffee.'}, status=status.HTTP_400_BAD_REQUEST)

        except Coffee.DoesNotExist:
            return Response({'message': 'Coffee not found.'}, status=status.HTTP_404_NOT_FOUND)

















# class CoffeeLikesAPIView(APIView):
#     def post(self, request, coffee_id):
#         # coffee_instance = get_object_or_404(Coffee, pk=coffee_id)
#         # user = request.user

#         # # Check if the user has already liked the coffee
#         # if not Like.objects.filter(user_name=user, coffee=coffee_instance).exists():
#         #     # User has not liked the coffee, create a new Like instance
#         #     like = Like.objects.create(user_name=user, coffee=coffee_instance)
#         #     coffee_instance.coffee_likes.add(like)
#         #     serializer = LikeSerializer(like)
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # else:
#         #     return Response({'message': 'User has already liked this coffee.'}, status=status.HTTP_400_BAD_REQUEST)
        



#         user_name = request.user
#         coffee_id = coffee_id



#         try:
#             coffee = Coffee.objects.get(coffeeid=coffee_id)
#             if not Coffee.coffee_likes.filter(user_name=user_name).exists():
#                 like = Like.objects.create(user_name)
#                 coffee.coffee_likes.add(like)
#                 return Response({'message': 'Like added.'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'You already like this coffee.'}, status=status.HTTP_200_OK)

#         except Coffee.DoesNotExist:
#             return Response({'message': 'Coffee not found.'}, status=status.HTTP_404_NOT_FOUND)