set +e
echo "==> Django setup, executing: collectstatic"
python  manage.py collectstatic --settings=BoomBoom.settings.production --noinput -v 3
echo "==> Django deploy with Gunicorn"
gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=BoomBoom.settings.production BoomBoom.wsgi.production:application