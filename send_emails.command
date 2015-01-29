#!/bin/sh
cd "$(dirname "$0")"
pwd
env PYTHONPATH=/usr/local/lib/python2.7/site-packages python src/data_loader.py --infolder input-data --send > send_emails_log.log