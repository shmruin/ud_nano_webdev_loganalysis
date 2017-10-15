import psycopg2

DBNAME = "news"


def get_most_popular_3articles():
    """What are the most popular 3 articles of all time?"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select A.title, count(B.path) as views from articles as A, log as B where \
    B.path like concat('%', A.slug) group by A.title order by views desc \
    limit 3;")
    return c.fetchall()
    db.close()


def get_most_popular_authors():
    """Who are the most popular article authors of all time?"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select A.name, sum(B.views) as author_views from (select B.id, \
    B.name, A.title from articles as A, authors as B where A.author = B.id) \
    as A, (select A.title, count(B.path) as views from articles as A, log \
    as B where B.path like concat('%', A.slug) group by A.title order by \
    views desc) as B where A.title = B.title group by A.name order by \
    author_views desc;")
    return c.fetchall()
    db.close()


def get_day_more_than_1percent_req_error():
    """On which days did more than 1% of requests lead to errors?"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select log_date, round((times * 100 / sum(times) over()), 1) as percentage \
    from (with error_nums as (select A.time::date as log_date, \
    count(A.status) as times from log as A where \
    A.status like '404%' group by log_date) select log_date, \
    times from error_nums where times > (select avg(times) from error_nums) \
    order by log_date) as K;")
    return c.fetchall()
    db.close()


if __name__ == '__main__':
    print("1. What are the most popular three articles of all time?")
    print(get_most_popular_3articles())
    print("2. Who are the most popular article authors of all time?")
    print(get_most_popular_authors())
    print("3. On which days did more than 1%% of requests lead to errors?")
    print(get_day_more_than_1percent_req_error())
