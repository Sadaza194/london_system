from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .models import Player

class ChessDriver():

    def __init__(self) -> None:
        self.website = 'https://2700chess.com/all-fide-players'
        self.driver = webdriver.Firefox()
        self.driver.get(self.website)
        field = self.driver.find_element(By.ID, 'count')
        field.send_keys(Keys.DOWN)
        field = self.driver.find_element(By.CSS_SELECTOR, '.select2-selection')
        field.send_keys(Keys.ENTER)
        field.send_keys(Keys.DOWN*5)
        field.send_keys(Keys.ENTER)

    def changeCountry(self, downs: int) -> None:
        field = self.driver.find_element(By.CSS_SELECTOR, '.select2-selection')
        field.send_keys(Keys.ENTER)
        field.send_keys(Keys.DOWN*downs)
        field.send_keys(Keys.ENTER)

    def fetchResults(self) -> str:
        field = self.driver.find_element(By.CSS_SELECTOR, '.btn')
        field.send_keys(Keys.ENTER)
        self.driver.get(self.website)
        html = self.driver.page_source
        return html

    def shutDown(self) -> None:
        self.driver.close()

    def scrape_to_db(self) -> list:
        for i in range(1): #2700chess lists 202 countries, so we call changeCountry 201 times
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
                        p.fname = d.span.string
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

                if p.rank or p.title or p.fname or p.lname or p.age or p.country or p.classic_rank or p.blitz_rank or p.rapid_rank is not None:
                    print("Saving Player:", p.rank, p.title, p.fname, p.lname, p.age, p.country, p.classic_rank, p.blitz_rank, p.rapid_rank)
                    p.save()
                else: 
                    print("player rank is none:", p.rank, p.title, p.fname, p.lname, p.age, p.country, p.classic_rank, p.blitz_rank, p.rapid_rank)

            self.changeCountry(1)
        self.shutDown()
        # return player_list



if __name__ == '__main__':

    chess = ChessDriver()

    for i in range(201): #2700chess lists 202 countries, so we call changeCountry 201 times
        soup = BeautifulSoup(chess.fetchResults(),'xml')
        for c in soup.find_all('tr'):
            p = Player()
            for d in c.find_all('td'):
                if d.span == None:
                    pass
                elif d.get('class') == 'position':
                    p.rank = int(d.string.strip())
                elif d.get('class') == 'title':
                    if d.string is not None:
                        p.title = d.string.strip()
                    else:
                        p.title = ''
                elif d.get('class') == 'name':
                    p.fname = d.span.string.strip()
                elif d.get('class') == 'country f24':
                    p.country = d.span.string.strip()
                elif d.get('class') == 'standard':
                    p.classic_rank = d.span.string.strip()
                elif d.get('class') == 'rapid canhide':
                    p.rapid_rank = d.span.string.strip()
                elif d.get('class') == 'blitz canhide':
                    p.blitz_rank = d.span.string.strip()
                elif d.get('class') == 'age':
                    p.age = int(d.span.string.strip())
        chess.changeCountry(1)
    chess.shutDown()
