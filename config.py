postgresql = {
    'host': '127.0.0.1:25000',
    'user': 'developer',
    'passwd': 'devpassword',
    'db': 'developer'
}

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])
