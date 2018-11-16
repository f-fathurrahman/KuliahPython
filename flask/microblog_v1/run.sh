#!/bin/bash
source /home/students/activate_anaconda3.sh
export FLASK_APP=microblog.py
export FLASK_DEBUG=1
# or export FLASK_ENV=development
flask run
