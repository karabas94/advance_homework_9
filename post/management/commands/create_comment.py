from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from post.models import Comment, Post
from random import randint, choice
from django.utils import timezone
from datetime import timedelta

from faker import Faker

fake = Faker()

User = get_user_model()


class Command(BaseCommand):
    help = 'Create comments'  # noqa: A003

    def handle(self, *args, **options):
        # create 2000 comments
        comment = []
        for _ in range(2000):
            comment.append(Comment(
                author=choice(User.objects.all()),
                message=fake.sentence(nb_words=10),
                created_at=timezone.now() - timedelta(days=randint(0, 499)),
                is_reviewed=True,
                post=choice(Post.objects.all())
            ))
        Comment.objects.bulk_create(comment)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(comment)} comment(s)'))
