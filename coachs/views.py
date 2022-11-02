from rest_framework.generics import ListCreateAPIView,UpdateAPIView,DestroyAPIView,ListAPIView
from .serializers import CoachSerializer
from .models import Coach

class CreateListCoachView(ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer



class GetUpdateDeleteCoachView(ListAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class = CoachSerializer
    def get_queryset(self):
        queryset = Coach.objects.all()
        coach_id = self.kwargs['pk']
        queryset = queryset.filter(id=coach_id)
        return queryset






