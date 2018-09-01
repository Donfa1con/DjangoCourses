from django.db import models


class QuestionManager(models.Manager):
    def new(self):
        return Question.objects.all().order_by('-pk')

    def popular(self):
        return Question.objects.all().order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(default='', max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey('auth.User', null=True)
    likes = models.ManyToManyField('auth.User', related_name='q_to_likes')

    def __str__(self):
        return self.title

    def get_url(self):
        return "/question/{}/".format(self.id)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    question = models.ForeignKey(Question, null=True, related_name='answer')
    author = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.text
