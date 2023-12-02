from userProfile.serializers import UserProfileSerializer
from rest_framework import generics, permissions
from userProfile.models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404



class UserProfileCreateView(APIView):
    def post(self, request, *args, **kwargs):
        
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        about_me = request.data.get('about_me')
        picture = request.data.get('picture')

        user = request.user

        try:
            user_profile = UserProfile.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                about_me=about_me,
                picture=picture
            )
            serializer = UserProfileSerializer(user_profile)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except :
            return Response({'message': "Your request could not be processed."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


    def get(self, request):
        user = request.user
        user_profile = get_object_or_404(UserProfile, user=user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def delete(self, request):
        user = request.user
        user_profile = get_object_or_404(UserProfile, user=user)
        user_profile.delete()
        return Response({'message': 'UserProfile deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    
    def put(self, request):
        user = request.user
        user_profile = get_object_or_404(UserProfile, user=user)

        # Extract data from the request
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        about_me = request.data.get('about_me')
        picture = request.data.get('picture')

        # Update UserProfile instance
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.about_me = about_me
        user_profile.picture = picture
        user_profile.save()

        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)