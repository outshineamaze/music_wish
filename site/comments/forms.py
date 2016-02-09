from django import forms
from .models import Comments,Replay



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
    fields = ('name', 'contents','like' )

class ReplaycommentForm(forms.ModelForm):
    class Mete:
        model=Replay
    fields=('name','contents','replayobj')

