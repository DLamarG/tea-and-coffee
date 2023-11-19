from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tea
from .serializers import TeaSerializer

class TeaListView(APIView):
    def get(self, request):
        coffees = Tea.objects.all()
        serializer = TeaSerializer(coffees, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        coffee = request.data
        serializer = TeaSerializer(data=coffee)
        if serializer.is_valid(raise_exception=True):
            coffee_saved = serializer.save()
        return Response({"result": f"{coffee_saved.name} saved"})