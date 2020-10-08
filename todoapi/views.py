from datetime import datetime

from rest_framework import viewsets, mixins

from todoapi.models import Boards, Todos
from todoapi.serializers import BoardSerializer, BoardDetailSerializer, TodoSerializer


# Create your views here.
# created separate viewsets for board list and board detail
# since they show different fields and use different serializers
class BoardViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    """
    List all boards with the todo_count field.
    """
    queryset = Boards.objects.all()
    serializer_class = BoardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BoardDetailViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    """
    List boards detail with todos listed
    """
    queryset = Boards.objects.all()
    serializer_class = BoardDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TodoViewSet(viewsets.ModelViewSet):
    """
    List all todos, or create a new todos.
    """
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.validated_data['updated'] = datetime.now()
            serializer.save()


# added an extra viewset to filter todos based on done status
class TodoNotDoneViewSet(viewsets.ModelViewSet):
    """
    Filter all Todos that has the done flag set to false
    """
    serializer_class = TodoSerializer

    def get_queryset(self):
        status = False
        return Todos.objects.filter(done=status)
