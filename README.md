# Spanish Tools by MK2 V1.3
Latest update(7/18/2021): Reworked the python code to scrape the data. 
Spanish Tools by MK2 1.3 is a python library that uses BeautifulSoup webscraping to gather Spanish words along with their english translations.
It can pull words ranging from today up to over the last year.
It features a 4 choice multiple choice quiz that pulls over 100 words and keeps track of your score.
With the new version scores are now saved in a SQL database instead of an excel file.
The hiscores can now also be called either by top points, best percent, or most questions.
The tools can be called individually or the Spanish.span_comp('') function can be called that will allow the user to choose the option with a corresponding key.

## Usage

```python
from spantools import Spanish

Automate Tools:

    Spanish.span_comp('')


Individual Tools:

    Spanish.today('')
    Spanish.yesterday('')
    Spanish.week('')
    Spanish.month('')
    Spanish.year('')
    Spanish.Quiz('')
    Spanish.top_points('')
    Spanish.top_percent('')
    Spanish.top_questions('')
```


