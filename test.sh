#!/bin/bash

# 1. Iniciar MailHog en Docker
echo "Iniciando MailHog..."
docker run -d --name mailhog -p 1025:1025 -p 8025:8025 mailhog/mailhog

# Esperar unos segundos para que MailHog esté completamente iniciado
sleep 5

pytest --cov --cov-report=term-missing
# 4. Apagar y eliminar el contenedor de MailHog
echo "Apagando y eliminando MailHog..."
docker stop mailhog
docker rm mailhog

echo "Pruebas finalizadas."
