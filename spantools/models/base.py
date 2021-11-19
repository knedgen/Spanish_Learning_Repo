import bs4
import requests
#import pandas as pd
import sqlite3 as sq


class BaseModel():
    @classmethod
    def query(self, query_string):
        conn = sq.connect('spantools.db')
        result = pd.read_sql_query(query_string, conn)
        conn.close()
        return result

    @classmethod
    def request(self, url):
        result = requests.get(url)
        return bs4.BeautifulSoup(result.text,'lxml')        