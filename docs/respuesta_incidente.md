# Plan de Respuesta a Incidentes: Contención vs. Prevención

## 1. Contención Inmediata
* **Objetivo:** Mitigar el riesgo en el entorno de ejecución inmediatamente sin esperar el ciclo de desarrollo.
* **Acciones:**
  1. Deshabilitar temporalmente el endpoint `/buscar_publicaciones` mediante un flag de configuración o comentario en la ruta del Blueprint.
  2. Implementar una regla de filtrado en el WAF / proxy reverso para bloquear peticiones con caracteres especiales hacia dicho endpoint.

## 2. Prevención (Solución Raíz)
* **Objetivo:** Corregir la causa raíz del código para evitar la recurrencia.
* **Acciones:**
  1. Refactorizar el código en `app/buscar_publicaciones.py` para utilizar consultas parametrizadas (Prepared Statements) o el ORM.
  2. Validar y sanear las entradas del usuario con una lista blanca de caracteres permitidos.
  3. Reejecutar el pipeline de CI/CD para confirmar que la herramienta SAST apruebe el análisis en verde.
