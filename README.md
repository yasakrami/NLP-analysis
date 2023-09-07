# Web Scraping and NLP Analysis

## Description

In this project, we perform web scraping and Natural Language Processing (NLP) analysis on web page content. We use the `requests` library to download web page content from [www.python.org](https://www.python.org) and then utilize the `Beautiful Soup` library to extract text from the page. We will eliminate stop words from the extracted text and use the `wordcloud` module to create a word cloud based on the cleaned text.

### Web Scraping

We start by using the `requests` library to retrieve the content of the [Python website](https://www.python.org). We get the web page's HTML content and then use `Beautiful Soup` to parse the content and obtain only the text, removing the structural information.

### NLP Analysis

a. We use the cleaned text and perform the following tasks:
   - Tokenize the text into words and sentences.
   - Extract noun phrases from the text.

b. We download a web page for a current news article and create a `TextBlob` object. We then display the sentiment for the entire `TextBlob` and for each sentence.

c. We repeat the previous exercise but use the `NaiveBayesAnalyzer` for sentiment analysis.

d. We download a current news article and use the spaCy library's named entity recognition capabilities to identify and display named entities such as people, places, organizations, etc.

e. We download several news articles on the same topic and compare them for similarity using NLP techniques.

## Usage

1. Install the required libraries if you haven't already:
   - `requests`
   - `beautifulsoup4`
   - `wordcloud`
   - `textblob`
   - `spacy`
