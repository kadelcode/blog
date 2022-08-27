from turtle import title
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

# The get_user_model is used to reference the active user

# Create your tests here.
class BlogTest(TestCase):
    def setUp(self):
        #create a user
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@gmail.com',
            password = 'testpwd123',
            )
        
        #create a post
        self.post = Post.objects.create(
            title = 'My Post Title',
            body = 'My Post content',
            author = self.user,
        )

    #check if the post title is actually the title
    def test_string_rep(self):
        post = Post(title = 'Post title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'My Post Title')
        self.assertEqual(f'{self.post.body}', 'My Post content')
        self.assertEqual(f'{self.post.author}', f'{self.user}')

    # test for post list pages
    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))#get the page for post lists
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{self.post.body}')
        self.assertTemplateUsed(response, 'index.html')

    #test for post detail pages for 404
    def test_post_detail_view(self):
        response_page = self.client.get('/posts/1/')
        no_response_page = self.client.get('/posts/1000000000000/')
        self.assertEqual(response_page.status_code, 404)
        self.assertEqual(no_response_page.status_code, 404)
        #check if the response page contains "My Post Title"
        #self.assertContains(response_page, 'My Post Title')
        #self.assertTemplateUsed(response_page, 'blog/post_detail.html')