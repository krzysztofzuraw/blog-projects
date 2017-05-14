FROM nginx:latest

ADD nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /var/www/media

WORKDIR /var/www/media

RUN chown -R nginx:nginx /var/www/media
