from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ChatBoard, ChatTopic, Post
from .form import NewChatTopicForm  # Ensure this is correctly named
from django.contrib.auth.decorators import login_required

# Function to render the home page
def home(request):
    chat_boards = ChatBoard.objects.all()  # Fetch all chat boards
    return render(request, 'webchat/home.html', {'chat_boards': chat_boards})

# Function to handle creating a new chat topic
@login_required  # Ensure the user is logged in
def new_board_topic(request, board_pk):
    chat_board = get_object_or_404(ChatBoard, pk=board_pk)

    if request.method == 'POST':
        form = NewChatTopicForm(request.POST)  # Initialize the form with POST data
        if form.is_valid():  # Check if the form is valid
            chat_topic = form.save(commit=False)  # Create the ChatTopic instance without saving yet
            chat_topic.chat_board = chat_board  # Associate the ChatBoard with the ChatTopic
            chat_topic.boardStarter = request.user  # Set the board starter
            chat_topic.save()  # Save the ChatTopic

            # Now create a Post associated with the new ChatTopic
            Post.objects.create(  # Corrected this line
                message=form.cleaned_data.get('message'),
                topic=chat_topic,  # Link the new post to the newly created topic
                createdBy=request.user
            )
            
            return redirect('board_topic', board_pk=board_pk, topic_pk=chat_topic.pk)  # Redirect to the new topic page
    else:
        form = NewChatTopicForm()

    return render(request, 'webchat/new_board_topic.html', {'chat_board': chat_board, 'form': form})

def signup(request):
    return render(request, 'signup.html')

# Function to render a specific board topic
def board_topic(request, board_pk, topic_pk):
    chat_topic = get_object_or_404(ChatTopic, pk=topic_pk)  # Get the topic
    posts = Post.objects.filter(topic=chat_topic)  # Fetch posts related to the topic

    return render(request, 'webchat/board_topic.html', {'chat_topic': chat_topic, 'posts': posts})

# Function to list all topics in a specific chat board
def chat_board_topics(request, board_pk):
    chat_board = get_object_or_404(ChatBoard, pk=board_pk)
    topics = chat_board.topics.all()  # Fetch all topics in the board

    return render(request, 'webchat/chat_board_topics.html', {'chat_board': chat_board, 'topics': topics})
