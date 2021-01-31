import os
import redis
import json
import psycopg2
from bottle import Bottle, request

class Sender(Bottle):
  def __init__(self):
    super().__init__()
    self.route('/', method='POST', callback=self.send)
    self.queue = redis.StrictRedis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=0)
    
    DSN = f'dbname={os.getenv("DB_NAME")} user={os.getenv("DB_USER")} host={os.getenv("DB_HOST")} password={os.getenv("DB_PASSWORD")}'

    self.connection = psycopg2.connect(DSN)

  def register_message(self, subject, message): 
    cursor = self.connection.cursor()
    SQL = 'INSERT INTO emails (subject, message) VALUES (%s, %s)'

    cursor.execute(SQL, (subject, message))
    
    self.connection.commit()
    cursor.close()

    msg = {'subject': subject, 'message': message }
    self.queue.rpush('sender', json.dumps(msg))
    
    print('Success! Message stored')

  def send(self):
    subject = request.forms.get('subject') 
    message = request.forms.get('message')
 
    self.register_message(subject, message)
    return 'Queued Message!\n Subject: {} \nMessage: {}'.format(subject, message)


if __name__ == '__main__':
  sender = Sender()
  sender.run(host='0.0.0.0', port=8080, debug=True)