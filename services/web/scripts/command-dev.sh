#!/bin/sh

python web/manage.py create_database
python web/manage.py run -h 0.0.0.0
