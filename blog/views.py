from django.views.genric.edit import CreateView
from .models import blog

class PostCreateView(CreateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)