from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse


from .models import Board 
from .models import Topic 
from .models import User 
from .models import post

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards})

def board_topics(request, pk):
    board = Board.objects.get(pk = pk)
    return render(request, 'topics.html', {'board':board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
   
    if request.method== 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )
        
        post = post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        
        return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})


