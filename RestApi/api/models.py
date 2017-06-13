from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=254,
    )
    username = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    money = models.FloatField(default=1000)

    USERNAME_FIELD = 'username'

    objects = UserManager()

class Event(models.Model):
    text = models.CharField(max_length=100, default='')
    Team_1 = models.CharField(max_length=100, default='')
    Team_2 = models.CharField(max_length=100, default='')
    coef = models.FloatField(default='1')
    Team_1_bets = models.FloatField(default='1')
    Team_2_bets = models.FloatField(default='1')

    def __str__(self):
        return self.text

class Bet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    coef = models.FloatField(default='1')
    selected_team = models.CharField(max_length=100, default='')
    size_of_bet = models.FloatField(default='1')
    owner = models.ForeignKey(User, related_name='bets', on_delete=models.CASCADE)
    event = models.ForeignKey(Event)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)
