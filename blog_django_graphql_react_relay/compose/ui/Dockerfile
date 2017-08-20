FROM node:8

WORKDIR /app
COPY ./film_ui/package.json /app
COPY ./film_ui/yarn.lock /app

RUN yarn install

ADD ./film_ui/ /app
