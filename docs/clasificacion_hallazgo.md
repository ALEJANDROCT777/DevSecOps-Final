# Clasificación del Hallazgo de Seguridad

## 1. Información General
* **Archivo afectado:** `app/buscar_publicaciones.py`
* **Funcionalidad:** Búsqueda de publicaciones por nombre de usuario.

## 2. Clasificación de la Vulnerabilidad
* **Tipo de Falla:** Inyección SQL (SQL Injection)
* **Identificador CWE:** CWE-89 (Improper Neutralization of Special Elements used in an SQL Command)

## 3. Severidad e Impacto
* **Severidad:** Alta / Crítica
* **Justificación de Severidad:** Aunque la herramienta Bandit marca por defecto la regla B608 como severidad `MEDIUM`, en una evaluación manual de riesgo se eleva a **Crítica/Alta** debido a que permite a un atacante no autenticado ejecutar consultas SQL no autorizadas, pudiendo leer o alterar tablas completas de la base de datos.
* **Explotabilidad:** Alta. Se explota directamente en el campo de entrada sin requerir privilegios.

## 4. Análisis de Falso Positivo
* **¿Es un falso positivo?:** No. Se verificó que el código original concatenaba el parámetro directamente en el query sin parametrizar.
