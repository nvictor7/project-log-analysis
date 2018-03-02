#! /usr/bin/env python3

import psycopg2

DBNAME = 'news'


# query request connection to database
def run_query(query):
    try:
        db = psycopg2.connect('dbname=' + DBNAME)
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
        db.close()
        return rows
    except BaseException:
        print('Sorry, unable to connect to database')


# analysize aritcles and log tables and produce results of popular articles
def popular_three_articles():
    query = """
        SELECT articles.title, COUNT(*) AS views
        FROM articles, log
        WHERE log.path = CONCAT('/article/', articles.slug)
        GROUP BY articles.title ORDER BY views DESC LIMIT 3;"""
    popular_articles = run_query(query)
    print('MOST POPULAR THREE ARTICLES OF ALL TIME')
    list_order = 1
    for i in popular_articles:
        print(str(list_order) + '.' + i[0] + ' - ' + str(i[1]) + ' views')
        list_order += 1
    print("")


# analyse authors and articles tables and produce results of popular authors
def most_popular_authors():
    query = """
        SELECT authors.name, COUNT(*) AS views
        FROM authors, articles, log
        WHERE authors.id = articles.author
        AND log.path = CONCAT('/article/', articles.slug)
        GROUP BY authors.name ORDER BY views DESC;"""
    popular_authors = run_query(query)
    print('MOST POPULAR ARTICLE AUTHORS OF ALL TIME')
    list_order = 1
    for i in popular_authors:
        print(str(list_order) + '.' + i[0] + ' - ' + str(i[1]) + ' views')
        list_order += 1
    print("")


# analyze request errors and produce resutls of more 1% failed connections
def days_request_errors():
    query = """
        SELECT date, error_perc
        FROM error_percentage
        WHERE error_perc > 1;"""
    days_errors = run_query(query)
    print('DAYS HAVE MORE THAN 1% OF REQUESTS LEAD TO ERRORS')
    for i in days_errors:
        print(str(i[0]) + ' - ' + str(round(i[1], 2)) + ' % errors')


if __name__ == '__main__':
    popular_three_articles()
    most_popular_authors()
    days_request_errors()
