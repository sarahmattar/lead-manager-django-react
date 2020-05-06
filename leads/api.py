from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset

class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated, ]
    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.leads.all() 
    
    def perform_create(self, serializer):
        # this allows us to save the lead owner when we create the lead.
        serializer.save(owner=self.request.user)
    