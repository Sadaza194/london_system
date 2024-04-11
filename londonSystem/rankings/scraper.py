from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .models import Player, Game

class ChessScraper():

    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.field = None

    def goto(self, url: str) -> None:
        self.website = 'https://2700chess.com/' + url
        self.driver.get(self.website)

    def select(self, category: str) -> None:
        if category == 'count':
            self.field = self.driver.find_element(By.ID, 'count')
        elif category == 'country':
            self.field = self.driver.find_element(By.CSS_SELECTOR, '.select2-selection')
        elif category == 'next':
            self.field = self.driver.find_element(By.CSS_SELECTOR, 'div.col-xs-6:nth-child(2) > a:nth-child(1)')
            self.website = self.website[:-2] + str(int(self.website[-1])+1)
        elif category == 'search':
            if len(self.website) > 30:
                self.field = self.driver.find_element(By.CSS_SELECTOR, '.btn')
            else:
                self.field = self.driver.find_element(By.CSS_SELECTOR, '.btn-2700')
        self.field.send_keys(Keys.ENTER)

    def inputKeys(self, inputList: list) -> None:
        for t in inputList:
            if t[0] == 'down':
                self.field.send_keys(Keys.DOWN*t[1])
            elif t[0] == 'up':
                self.field.send_keys(Keys.UP*t[1])
            elif t[0] == 'left':
                self.field.send_keys(Keys.LEFT*t[1])
            elif t[0] == 'right':
                self.field.send_keys(Keys.RIGHT*t[1])
            elif t[0] == 'tab':
                self.field.send_keys(Keys.TAB*t[1])
            elif t[0] == 'enter':
                self.field.send_keys(Keys.ENTER*t[1])
        self.field.send_keys(Keys.ENTER)

    def fetchResults(self, doSearch: bool = True) -> str:
        if doSearch:
            self.select('search')
        self.driver.get(self.website)
        html = self.driver.page_source
        return html

    def shutDown(self) -> None:
        self.driver.close()

    def scrape_players_to_db(self, countryCount: int = 201) -> list:
        self.select('count')
        self.inputKeys([('down',1)])
        self.select('country')
        self.inputKeys([('down',5)])
        for i in range(countryCount): #2700chess lists 202 countries, so we call changeCountry 201 times
            soup = BeautifulSoup(self.fetchResults(),'xml')

            for c in soup.find_all('tr')[1:]:
                p = Player()

                for d in c.find_all('td'):
                    if d.get('class') == 'position':
                        if d.string is not None:
                            p.rank = d.string.strip()
                        else:
                            p.rank = "N/A"
                    elif d.get('class') == 'title':
                        if d.span.string is not None:
                            p.title = d.span.string.strip()
                        else:
                            p.title = 'N/A'
                    elif d.get('class') == 'name':
                        p.name = d.span.string
                    elif d.get('class') == 'country f24':
                        p.country = d.span.string
                    elif d.get('class') == 'standard':
                        p.classic_rank = d.span.string
                    elif d.get('class') == 'rapid canhide':
                        p.rapid_rank = d.span.string
                    elif d.get('class') == 'blitz canhide':
                        p.blitz_rank = d.span.string
                    elif d.get('class') == 'age':

                        if d.span.string is not None:
                            # p.age = int(d.span.string.strip())
                            p.age = d.span.string
                        else:
                            p.age = 'N/A'

                if p.rank or p.title or p.name or p.age or p.country or p.classic_rank or p.blitz_rank or p.rapid_rank is not None:
                    print("Saving Player:", p.rank, p.title, p.name, p.age, p.country, p.classic_rank, p.blitz_rank, p.rapid_rank)
                    repeated_player = Player.objects.filter(
                        rank=p.rank,
                        title=p.title,
                        name=p.name,
                        age=p.age,
                        country=p.country,
                        classic_rank=p.classic_rank,
                        blitz_rank=p.blitz_rank,
                        rapid_rank=p.rapid_rank
                    )
                    if repeated_player.exists():
                        print("Player already exists in database.")
                        repeated_player = repeated_player.first()
                        repeated_player.rank = p.rank
                        repeated_player.title = p.title
                        repeated_player.name = p.name
                        repeated_player.age = p.age
                        repeated_player.country = p.country
                        repeated_player.classic_rank = p.classic_rank
                        repeated_player.blitz_rank = p.blitz_rank
                        repeated_player.rapid_rank = p.rapid_rank
                        repeated_player.save()
                        
                    else:
                        p.save()
                else: 
                    print("player rank is none:", p.rank, p.title, p.name, p.age, p.country, p.classic_rank, p.blitz_rank, p.rapid_rank)

            self.select('country')
            self.inputKeys([('down',1)])

            
    def scrape_games_to_db(self, pages: int = 20) -> None:
        for i in range(pages): #we collect 20 pages, and thus 1000 games, by default
            soup = BeautifulSoup(self.fetchResults(False),'xml')
            for c in soup.find_all('tr')[1:]:
                g = Game()
                for d in c.find_all('td')[:9]:
                    if d.get('class') == 'white_player name':
                        g.w_player = d.string
                    elif d.get('class') == 'white_elo rating':
                        g.w_player_rank = d.string
                    elif d.get('class') == 'black_player name':
                        g.b_player = d.string
                    elif d.get('class') == 'black_elo rating':
                        g.b_player_rank = d.string
                    elif d.get('class') == 'popover-game result':
                        g.game_result = d.a.string
                    elif d.get('class') == 'plycount':
                        g.number_of_moves = d.string
                    elif d.get('class') == 'site':
                        if d.string == None:
                            d.string = 'None'
                        g.location = d.string
                    elif d.get('class') == 'date text-align-right':
                        g.date = d.string
                g.save()
            self.select('next')

if __name__ == '__main__':

    chess = ChessScraper('all-fide-players')
    #print(chess.scrape_to_db())
