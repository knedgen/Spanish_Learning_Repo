from .base import BaseModel
from .words import Word

external_base = 'https://www.spanishdict.com/wordoftheday'
spanish_selector = 'h3'
english_selector = 'div._3iXmZ8Jd'


class Dictionary(BaseModel):

    @classmethod
    def page(self, page_no):
        words = []
        soup = self.request(f'{external_base}/{page_no}')

        for i in range(0,10):
            words.append(
                Word(soup.select(spanish_selector)[i].text,
                     soup.select(english_selector)[i].text))

        return words

    @classmethod
    def pages(self, page_count):
        words = []
        for n in range(0, page_count):
            words.extend(self.page(n+1))
        return words

    @classmethod
    def today(self):
        return self.page(1)[0]

    @classmethod
    def yesterday(self):
        return self.page(1)[1]

    @classmethod
    def week(self):
        return self.page(1)[0:7]

    @classmethod
    def month(self):
        return self.pages(4)[0:31]

    @classmethod
    def year(self):
        return self.pages(37)[0:365]