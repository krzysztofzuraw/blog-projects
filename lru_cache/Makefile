run:
	gunicorn --workers=2 application:app

store:
	curl -X GET http://127.0.0.1:8000

get_info:
	curl -X GET http://127.0.0.1:8000/get_cache_info

clear_cache:
	curl -X GET http://127.0.0.1:8000/clear_cache
