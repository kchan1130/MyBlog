"""服务器配置
"""

DATABASE = {
    'host': '127.0.0.1',
    'username': 'root',
    'password': '123456',
    'database': {
        'name': 'myblog',
        'sql': {
            'create': '''CREATE DATABASE IF NOT EXISTS
                myblog
                DEFAULT CHARSET utf8
                COLLATE utf8_general_ci;
            ''',
        }
    },
    'table': {
        'articles': {
            'name': 'articles',
            'sql': {
                'create': '''CREATE TABLE IF NOT EXISTS
                    articles (
                    id BIGINT,
                    title VARCHAR (20),
                    age INT DEFAULT 1
                    )
                '''
            }
        }
    }
}