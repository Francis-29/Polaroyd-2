from django.db import models
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to='posts/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self) -> str:
        return self.user.user_id + ' -- ' + self.caption[:20]
    

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        unique_together = ('post', 'user')

    def __str__(self):
        return self.user.user_id + ' -- ' + self.post.caption[:20]
    