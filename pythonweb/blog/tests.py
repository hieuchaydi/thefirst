from django.test import TestCase
from .models import Post

class BlogTest(TestCase):
    def setUp(self):
        Post.objects.create(
            title='myTitle',
            body='just a test'
        )
    
    def test_string(self):
        post = Post(title='my enpty title')
        self.assertEqual(str(post), post.title)
    
    def test_post(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'blog/blog.html')
    
    def test_post_view(self):
        self.test_post()
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'blog/post.html')
