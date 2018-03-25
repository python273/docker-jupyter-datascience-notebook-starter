# docker-jupyter-datascience-notebook-starter

DO Docker Droplet:

```bash
$ git clone https://github.com/python273/docker-jupyter-datascience-notebook-starter.git
$ cd docker-jupyter-datascience-notebook-starter/
$ apt-get update && apt-get install python3-pip -y && pip3 install ipython
$ mkdir work && chmod 777 work
$ python3 gen-docker-compose.py

# Copy port & password

$ docker-compose up

# Open: https://{IP}:{PORT}/
```
