from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Player
from yattag import Doc
from bs4 import BeautifulSoup

from .scraper import ChessDriver

# Create your views here.
# To use the scraper code here:
#     First, comment out the num_players line and the player_list line (lines 19 and 21)
#     Paste the scraper code after the value of sort is established
#     You may want to change the part in the scraper code that says for "i in range(201)" to a smaller range value

def index(request):

    print("Loading home page...")

    sort = request.GET.get('sort')
    if sort is None: sort = 'rank'
    num_players = 10 # -1 for all -- GETS ERROR THAT 'NEGATIVE INDEXING IS NOT ALLOWED'

    player_list = Player.objects.order_by(sort)[:num_players] # Param for order by somehow? and for number to dispaly ie. top 5?

    context = {"player_list": player_list}
    # output = '<br>'.join(str(player.fname + " " + player.lname) for player in player_list)

    return render(request, "rankings/index.html", context)


def reload_button(request): 
    # request.GET.get()
    # Re-scrape Here
    print("Scraping...")

    scraper = ChessDriver()
    results = scraper.scrape_to_db()
    for player in results:
        player.save()

    sort = request.GET.get('sort')
    if sort is None: sort = 'rank'
    num_players = 10 # -1 for all -- GETS ERROR THAT 'NEGATIVE INDEXING IS NOT ALLOWED'

    player_list = Player.objects.order_by(sort)[:num_players] # Param for order by somehow? and for number to dispaly ie. top 5?

    context = {"player_list": player_list}

    # index(request)
    return render(request, "rankings/index.html", context)
