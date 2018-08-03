from pg_python import pg_crawler


crawler_db = "postgres-crawler.hawker.news"
pg_crawler.pg_server("crawler", "postgres", "@hawkerIndia", crawler_db, True)
