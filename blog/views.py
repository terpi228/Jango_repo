from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Показываем только опубликованные записи
        return BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()


        if obj.views_count == 100:
            send_mail(
                subject='🎉 Статья достигла 100 просмотров!',
                message=f'Поздравляем! Ваша статья "{obj.title}" набрала 100 просмотров.',
                from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else None,
                recipient_list=['mcrussai223@gmail.com'],
                fail_silently=False,
            )
        return obj


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        # После редактирования перенаправляем на детальную страницу
        return reverse('blog:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')