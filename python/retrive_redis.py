import os
import sys

import redis


REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))


def retrive(id):

    with redis.Redis(host=REDIS_HOST, port=REDIS_PORT) as rc:
        data = rc.get(id)
        return data.decode('utf-8')



if __name__ == '__main__':
    arg = sys.argv[1]
    print("Redis:", retrive(arg))