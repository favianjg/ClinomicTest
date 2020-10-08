from rest_framework import viewsets

from reminder.models import Reminders
from reminder.serializers import ReminderSerializer


# Create your views here.
class ReminderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = Reminders.objects.all()
    serializer_class = ReminderSerializer
