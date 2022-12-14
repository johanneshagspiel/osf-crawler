<img src=resources/osf_logo.png alt="OSF Crawler Logo" width="399" height="150">

--------------------------------------------------------------------------------
[![MIT-License](https://img.shields.io/github/license/johanneshagspiel/osf-crawler)](LICENSE)
[![Top Language](https://img.shields.io/github/languages/top/johanneshagspiel/osf-crawler)](https://github.com/johanneshagspiel/osf-crawler)
[![Latest Release](https://img.shields.io/github/v/release/johanneshagspiel/osf-crawler)](https://github.com/johanneshagspiel/osf-crawler/releases/)

# OSF Crawler

This repository contains a crawler for the [Open Science Framework](https://osf.io/) website.

## Features

This crawler:
- automatically downloads information about research on a topic from the [Open Science Framework](https://osf.io/) website
- uses the natural language processing library [spaCy](https://spacy.io/) to perform common data cleanup steps such as getting rid of stop words and lemmatizing the words
- outputs the most frequent tags as well as words used in the titles and description in the form of an Excel file 

## Tools

| Purpose                    | Name                                                                    |
|----------------------------|-------------------------------------------------------------------------|
| Programming language       | [Python 3.10](https://www.python.org/)                                  |
| Version control system     | [Git](https://git-scm.com/)                                             |
| HTML parser                | [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) |
| Browser automation library | [Pyppeteer](https://miyakogi.github.io/pyppeteer/)                      |
| NLP library                | [spaCy](https://spacy.io/)                                              |
| Output generator           | [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)                  |
| Asynchronous framework    | [asyncio](https://docs.python.org/3/library/asyncio.html)                  |

## Licence

This "OSF Crawler" is published under the MIT licence, which can be found in the [LICENSE](LICENSE) file.

## References

The "Open Science Framework" logo was taken from the [University of Oklahoma Libraries](https://libraries.ou.edu/sites/default/files/osf_black.png) website.
