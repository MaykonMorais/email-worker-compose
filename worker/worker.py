import os
import redis
import json

from time import sleep
from random import randint



if __name__ == '__main__':
  r = redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=0)

  while True:
    message = json.loads(r.blpop('sender')[1])

    # It's only a simulate of sending a message
    print('Sending message: ', message['subject'])
    sleep(randint(15, 45))

    print('Message ', message['subject'], ' sent')