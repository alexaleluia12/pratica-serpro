import os

import redis


REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))


def store(id, url):
    print(f'{REDIS_HOST=} {REDIS_PORT=}')
    with redis.Redis(host=REDIS_HOST, port=REDIS_PORT) as rc:
        rc.set(id, url)
    # url_connection = redis.from_url("redis://localhost:6379?decode_responses=True&health_check_interval=2")
    # print(url_connection.ping())
    # rc.set(id, url)

    # print(id, ' armazenado com sucesso')



url = 'https://www.google.com/search?q=como+fazer+pure&sca_esv=560150485&sxsrf=AB5stBio3QJxXAjxcAL01B7NObBkycOkow%3A1692992585355&source=hp&ei=SQTpZKXgE6fd1sQP9O6UiAk&iflsig=AD69kcEAAAAAZOkSWSV1-2jwIJOo9R1BIyY0WlvDEZZ-&ved=0ahUKEwjlqJ_tyPiAAxWnrpUCHXQ3BZEQ4dUDCAk&uact=5&oq=como+fazer+pure&gs_lp=Egdnd3Mtd2l6Ig9jb21vIGZhemVyIHB1cmUyBRAAGIAEMggQABiABBixAzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESNIhUABY7R1wAHgAkAEAmAF9oAHSDaoBBDAuMTW4AQPIAQD4AQHCAgQQIxgnwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxiDARjHARjRA8ICCBAuGIAEGLEDwgIFEC4YgATCAgcQIxiKBRgnwgIREC4YigUYsQMYgwEYxwEY0QPCAgsQLhiABBjHARjRA8ICCBAuGIoFGLED&sclient=gws-wiz'
store('4523', url)