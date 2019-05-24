from .models import Post
from .serializers import PostSerializers
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .permission import IsAuthorOrReadonly
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [
        IsAuthorOrReadonly,
    ]
    filter_backends = [SearchFilter]
    search_field = ['message']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else:
            qs = qs.none()
        return qs
