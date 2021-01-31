#!/bin/sh

pip install bottle==0.12.13 python-dotenv redis==2.10.5
pip install --no-binary :all: psycopg2
python -u sender.py