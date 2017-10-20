#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def connect(database_name):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print("Unable to connect to database")
        # THEN perhaps exit the program
        sys.exit(1)  # The easier method
        # OR perhaps throw an error
        raise e
        # If you choose to raise an exception,
        # It will need to be caught by the whoever called this function


def get_query_results(query):
    # connect to database, grab cursor
    db, c = connect(DBNAME)
    # execute
    c.execute(query)
    # commit
    results = c.fetchall()
    # close
    db.close()
    # return results
    return results


if __name__ == '__main__':

    """What are the most popular 3 articles of all time?"""
    query1 = "select A.title, count(B.path) as views from articles as A, log as B where \
    B.path like concat('%', A.slug) group by A.title order by views desc \
    limit 3;"

    """Who are the most popular article authors of all time?"""
    query2 = "select A.name, sum(B.views) as author_views from (select B.id, \
    B.name, A.title from articles as A, authors as B where A.author = B.id) \
    as A, (select A.title, count(B.path) as views from articles as A, log \
    as B where B.path like concat('%', A.slug) group by A.title order by \
    views desc) as B where A.title = B.title group by A.name order by \
    author_views desc;"

    """On which days did more than 1% of requests lead to errors?"""
    query3 = "select log_date, round((times * 100 / sum(times) over()), 1) as percentage \
    from (with error_nums as (select A.time::date as log_date, \
    count(A.status) as times from log as A where \
    A.status like '404%' group by log_date) select log_date, \
    times from error_nums where times > (select avg(times) from error_nums) \
    order by log_date) as K;"

    print("1. What are the most popular three articles of all time?")
    results = get_query_results(query1)
    for el in results:
        print("\"" + el[0] + "\"" + " - " + str(el[1]) + " views")
    print("2. Who are the most popular article authors of all time?")
    results = get_query_results(query2)
    for el in results:
        print("\"" + el[0] + "\"" + " - " + str(el[1]) + " views")
    print("3. On which days did more than 1% of requests lead to errors?")
    results = get_query_results(query3)
    for el in results:
        print(el[0].strftime("%b %d, %Y") + " - " + str(el[1]) + "% errors")
