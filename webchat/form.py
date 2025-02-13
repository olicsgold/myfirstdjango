from django import forms
from .models import ChatTopic

class NewChatTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 7, 'placeholder': 'What are you thinking'}
        ),
        max_length=5000,
        help_text='The max length of the text is 5000.'
    )

    class Meta:
        model = ChatTopic
        fields = ['subject', 'message']

