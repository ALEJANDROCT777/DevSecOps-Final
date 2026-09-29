#!/bin/bash
echo "=== Ejecutando Análisis Estático de Seguridad con Bandit ==="
mkdir -p reportes

# Escaneo con Bandit usando la ruta global
bandit -r app/ -f txt -o reportes/salida_bandit.txt

if [ $? -ne 0 ]; then
    echo "[BLOQUEADO] Se detectaron fallas de seguridad graves en el código."
    exit 1
else
    echo "[PASÓ] El código cumple con los estándares de seguridad."
    exit 0
fi
