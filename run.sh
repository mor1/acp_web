#!/bin/bash

source /home/tfc_prod/tfc_web_venv/bin/activate
if [[ -f /home/tfc_prod/tfc_web_envvars ]]; then
    source /home/tfc_prod/tfc_web_envvars
    echo 'Setting custom environmnt from /home/tfc_prod/tfc_web_envvars'
fi

cd /home/tfc_prod/tfc_web/tfc_web

echo $(date) "gunicorn started " >> /var/log/tfc_prod/gunicorn.log

nohup gunicorn --config /home/tfc_prod/tfc_web/gunicorn_config.py tfc_web.wsgi & disown
