import psycopg2

# sql to retrieve the top 3 articles
top_3_articles = "select articles.title , count(*) as accessed " \
            "from articles inner join log on log.path " \
            "like concat('%', articles.slug, '%') " \
            "group by articles.title " \
            "order by accessed desc limit 3"

# sql to retrieve the authors popularity order
popular_authors = "select authors.name, count(*) as accessed from articles " \
                "inner join authors on articles.author = authors.id " \
                "inner join log on log.path " \
                "like concat('%', articles.slug, '%') "\
                "where log.status like '%200%' group " \
                "by authors.name order by accessed desc"

# sql tor retrieve days with more than one percent errors
more_than_one_percent_days = "select day, perc from (" \
                "select day, round((sum(requests)/(select count(*) from log " \
                "where substring(cast(log.time as text), 0, 11) = day) " \
                "* 100), 2) " \
                "as perc from (" \
                "select substring(cast(log.time as text), 0, 11) " \
                "as day, count(*) " \
                "as requests "\
                "from log where status like '%404%' group by day) "\
                "as log_percentage " \
                "group by day order by perc desc) as final_query " \
                "where perc > 1"


def connect():
    """Connect to the PostgreSQL news database."""
    try:
        conn = psycopg2.connect("dbname=news")
        return conn
    except:
        print ("Unable to connect to the news database.")


def get_query_results(conn, query):
    """Return the query results for the given query parameter."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def print_query_results(query_results, type):
    """Print the query results.The type could be "views" or "errors" """
    for rows in query_results:
        print rows[0], "--", rows[1], type

if __name__ == '__main__':
    # connect to the news database
    conn = connect()
    # Query to most popular authors
    print
    print "The most popular three articles of all time:"
    popular_articles_results = get_query_results(conn, top_3_articles)
    # print the query results
    print_query_results(popular_articles_results, "views")

    # Query to most popular authors
    print
    print "The most popular article authors of all time:"
    popular_authors_results = get_query_results(conn, popular_authors)
    # print the query results
    print_query_results(popular_authors_results, "views")

    # Query the days with error more than 1%
    print
    print "Days did more than 1% of requests lead to errors:"
    more_than_one_percent_days_results = \
        get_query_results(conn, more_than_one_percent_days)
    # print the query results
    print_query_results(more_than_one_percent_days_results, "errors")

    # close the DB connection
    conn.close()
