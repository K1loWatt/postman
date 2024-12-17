#!/bin/bash

#init mailhog
echo "mailhog init..."
docker run -d --name mailhog -p 1025:1025 -p 8025:8025 mailhog/mailhog

#Wait for mailhog to start
sleep 5

pytest --cov --cov-report=term-missing

#Clean up
echo "removing services..."
docker stop mailhog
docker rm mailhog
