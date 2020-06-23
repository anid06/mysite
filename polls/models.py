from django.db import models

# Pytanie:
# -treść
# -data publikacji
#

class Question(models.Model):
    question_text = models.CharField(max_length=200) #varchar
    pub_date = models.DateTimeField(verbose_name='Date published') #timestamp, datetime

    def __str__(self):
        return f'"{self.question_text}"'

# Odpowiedź:
# -treść
# -na jakie pytanie odpowiada (relacja bazodanowa)
# -ile głosów zebrała

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'"{self.choice_text}"'
