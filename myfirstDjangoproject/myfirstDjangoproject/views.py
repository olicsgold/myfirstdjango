from django.shortcuts import render
from django.http import HttpResponse
from .models import ChatBoard

# =============================================================================
# 
# def home (request):
#     return HttpResponse('As salamu alykum.. ')
# 
# =============================================================================

# =============================================================================
# uncomment this function if you want to use it
# def homepage(request):
#     chatBoard = ChatBoard.objects.all()
#     chatBoard_names = list()  
#     
#     for board in chatBoard:
#         chatBoard_names.append(board.name)  
#         
#     response_html = '<br>'.join(chatBoard_names)  
#     
#     return HttpResponse(response_html)
# =============================================================================

def home(request):
    chatBoard = ChatBoard.objects.all()
    return render(request, 'home.html', {'chatBoard': chatBoard})
