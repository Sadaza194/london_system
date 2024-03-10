from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Player
from yattag import Doc

from .scraper import ChessDriver

# Create your views here.
# copy+paste main function from scraper.py into index function
#     Put it after the value of sort is established
#     Comment out the num_players line and the player_list line
#     You may want to change the part in the scraper code that says for "i in range(201)" to a smaller range value

def index(request):

    sort = request.GET.get('sort')
    if sort is None: sort = 'rank'
    num_players = 10 # -1 for all -- GETS ERROR THAT 'NEGATIVE INDEXING IS NOT ALLOWED'

    player_list = Player.objects.order_by(sort)[:num_players] # Param for order by somehow? and for number to dispaly ie. top 5?

    context = {"player_list": player_list}
    # output = '<br>'.join(str(player.fname + " " + player.lname) for player in player_list)

    return render(request, "rankings/index.html", context)


### Return as HTML formatted List
# def index_old(request):

#     sort = 'fname'
#     num_players = 10 # -1 for all

#     player_list = Player.objects.order_by(sort)[:num_players] # Param for order by somehow? and for number to dispaly ie. top 5?

    # doc, tag, text = Doc().tagtext()

    # with tag('table'):
    #     with tag('tr'):
    #         with tag('th'):
    #             text("Rank")
    #         with tag('th'):
    #             text('Title')
    #         with tag('th'):
    #             text('First Name')
    #         with tag('th'):
    #             text('Last Name')    
    #         with tag('th'):
    #             text('Country')
    #         with tag('th'):
    #             text('Age')
    #         with tag('th'):
    #             text('Classic')
    #         with tag('th'):
    #             text('Rapid')
    #         with tag('th'):
    #             text('Blitz')

        
    #     for player in Player.objects.order_by('fname'):

    #         with tag('tr'):
    #             with tag('td'):
    #                 text(player.rank)
    #             with tag('td'):
    #                 text(player.title)
    #             with tag('td'):
    #                 text(player.fname)
    #             with tag('td'):
    #                 text(player.lname)
    #             with tag('td'):
    #                 text(player.country)
    #             with tag('td'):
    #                 text(player.age)
    #             with tag('td'):
    #                 text(player.classic_rank)
    #             with tag('td'):
    #                 text(player.blitz_rank)
    #             with tag('td'):
    #                 text(player.rapid_rank)


    # return HttpResponse(doc.getvalue())
