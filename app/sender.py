import os
import psycopg2
from bottle import route, run, request

DSN = f'dbname={os.getenv("DB_NAME")} user={os.getenv("DB_USER")} host={os.getenv("DB_HOST")} password={os.getenv("DB_PASSWORD")}'
SQL = 'INSERT INTO emails (subject, message) VALUES (%s, %s)'

def register_message(subject, message): 
  connection = psycopg2.connect(DSN)
  cursor = connection.cursor()

  cursor.execute(SQL, (subject, message))
  
  connection.commit()
  cursor.close()
  connection.close()

  print('Success! Message stored')

@route('/', method='POST')
def send():
  subject = request.forms.get('subject') 
  message = request.forms.get('message')
  
  register_message(subject, message)
  return 'Queued Message!\n Subject: {} \nMessage: {}'.format(subject, message)


if __name__ == '__main__':
  run(host='0.0.0.0', port=8080, debug=True)