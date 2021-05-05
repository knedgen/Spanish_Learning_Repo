# Spanish Tools by MK2
Spanish Tools by MK2 is a python library that uses BeautifulSoup webscraping to gather Spanish words along with their english translations.
It can pull words ranging from today up to over the last year.
It features a 4 choice multiple choice quiz that pulls over 100 words and keeps track of your score. 
The scores will be saved to a file called hiscores.xlsx and it creates the file if it does not exist. 
The tools can be called individually or an automated feature can be called that allows the used to pick options with keys.

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
```


