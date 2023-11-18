from django.test import TestCase
from .models import Comment
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_comment_form(self):
        form = CommentForm()
        self.assertEqual(form.Meta.model, Comment)
        self.assertEqual(form.Meta.fields, ('body',)) 
        