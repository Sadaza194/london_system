from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Player
from .models import Game
from yattag import Doc
from bs4 import BeautifulSoup


from .scraper import ChessScraper

# Create your views here.
# To use the scraper code here:
#     First, comment out the num_players line and the player_list line (lines 19 and 21)
#     Paste the scraper code after the value of sort is established
#     You may want to change the part in the scraper code that says for "i in range(201)" to a smaller range value

def index(request):

    print("Loading home page...")

    sort = request.GET.get('sort')
    if sort is None: 
        sort = 'rank'
        num_players = 10 # -1 for all -- GETS ERROR THAT 'NEGATIVE INDEXING IS NOT ALLOWED'

    player_list = Player.objects.order_by(sort) # Param for order by somehow? and for number to dispaly ie. top 5?

    context = {"player_list": player_list}
    # output = '<br>'.join(str(player.fname + " " + player.lname) for player in player_list)

    return render(request, "rankings/index.html", context)


def reload_button(request): 
    # request.GET.get()
    # Re-scrape Here
    print("Scraping...")

    scraper = ChessScraper()
    scraper.goto('all-fide-players')
    scraper.scrape_players_to_db(5) #get data from 5 countries (201 by default)
    
    scraper.goto('games?page=1') #you need to specify page 1 even though it does that by default
    scraper.scrape_games_to_db(2) #get data from 2 pages (20 by default)
    scraper.shutDown()

    return redirect(index)
    # return render(request, "rankings/index.html", context)


def games(request):
    # tryin to order by date but couldnt get it to work
    # games_list = Game.objects.all().order_by('date__month', 'date__day', 'date__year')
    games_list = Game.objects.all().order_by('date')
    context = {"games_list": games_list}
    return render(request, "rankings/games.html", context)



