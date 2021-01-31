# email-sender-compose :mailbox:

email-sender-compose is a complete example of a application with multiples services in docker. This application have some nice components:

* **Web Server**: Configured with nginx to provide pages and to create a layer that directs clients request to the appropriate backend server (reverse proxy).
* **Database**: Postgres - used for just to store simple messages.
* **Workers**: Used for capture messages from service queue and send them.
* **Queue management**: With redis it was possible to create a queue service that provide messages to workers.
* **Main application**: It's a little backend server that comunicate with database service and send messages to queue service. 


<p align=center style="margin: 40px 0;">
<strong>Final Diagram</strong><br/>
<img width="600" style="margin: 10px 0" src="https://i.imgur.com/6eky2FE.png"/>
</p>


## Instalation 🔧

First of all make sure you have installed [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install) on your machine.

After that, create a copy from file **env.example** and rename them to **.env**:

```bash
cp env.example .env
```

Obs: Just remember to define a value to DB_PASSWORD.

Finally just build all containers and be happy! 
```bash
sudo docker-compose up -d
```

### Workers :zap:

We can run multiples instances of workers on demand for messaging. To define the numbers of workers use the following command:

```bash
sudo docker-compose up -d --scale worker=<number_of_instances>
```

