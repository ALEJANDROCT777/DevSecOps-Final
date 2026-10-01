# Evidencia de Despliegue en Producción

## 1. Detalle del Entorno
* **Instancia EC2:** `torres-produccion`
* **Estado:** Desplegado y Operativo.
* **IP / URL de Producción:** `http://<TU_IP_PUBLICA_PROD>:8000`

## 2. Verificación del Ciclo DevSecOps
1. **QA:** Se identificó la vulnerabilidad y el pipeline bloqueó la construcción (`pipeline_bloqueado.txt`).
2. **Remediación:** Se aplicó el arreglo en el código fuente.
3. **Validación:** El pipeline se ejecutó nuevamente obteniendo resultado favorable (`pipeline_verde.txt`).
4. **Despliegue:** El artefacto verificado fue promovido e instalado en la instancia de Producción.

*(Nota: Adjuntar capturas de pantalla de la app corriendo en la EC2 de producción en la plantilla de entrega).*
