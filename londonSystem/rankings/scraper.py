from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from models.py import Player

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

if __name__ == '__main__':

    plist = []
    chess = ChessDriver()

    for i in range(201):
        soup = BeautifulSoup(chess.fetchResults(),'xml')
        for c in soup.find_all('tr'):
            p = Player()
            for d in c.find_all('td'):
                if d.span == None:
                    pass
                elif d.get('class') == 'position':
                    p.rank = int(d.string.strip())
                elif d.get('class') == 'title':
                    p.title = d.string.strip()
                elif d.get('class') == 'name':
                    p.fname = d.string.strip()
                elif d.get('class') == 'country f24':
                    p.country = d.string.strip()
                elif d.get('class') == 'standard':
                    p.classic_rank = int(d.string.strip())
                elif d.get('class') == 'rapid canhide':
                    p.rapid_rank = int(d.string.strip())
                elif d.get('class') == 'blitz canhide':
                    p.blitz_rank = int(d.string.strip())
                elif d.get('class') == 'age':
                    p.age = int(d.string.strip())
            if p not in plist:
                plist += p
        chess.changeCountry(1)
    chess.shutDown()
    print(plist)

'''
    for i in range(201):
        soup = BeautifulSoup(chess.fetchResults(),'xml')
        for c in soup.find_all('tr'):
            tmp = ''
            for d in c.find_all('td'):
                if d.span == None:
                    pass
                elif d.get('class') == 'position':
                    tmp += d.string.strip() + ';'
                elif d.span.string == None:
                    tmp += ' ;'
                else:
                    tmp += d.span.string.strip() + ';'
            if tmp not in final:
                final.append(tmp + '\n')
        chess.changeCountry(1)
'''
