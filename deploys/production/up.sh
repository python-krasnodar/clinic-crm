#!/usr/bin/env sh

docker-compose pull
docker-compose up -d --remove-orphans --build 
