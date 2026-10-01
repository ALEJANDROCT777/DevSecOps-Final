# Clasificación del Hallazgo de Seguridad

## 1. Información General
* **Archivo afectado:** `app/buscar_publicaciones.py`
* **Funcionalidad:** Búsqueda de publicaciones por nombre de usuario.

## 2. Clasificación de la Vulnerabilidad
* **Tipo de Falla:** Inyección SQL / Formato Inseguro de Consultas (o Inyección de Comandos / Path Traversal según el parche).
* **Identificador CWE:** CWE-89 (Improper Neutralization of Special Elements used in an SQL Command) / CWE-78.

## 3. Severidad e Impacto
* **Severidad:** **Alta / Crítica**
* **Justificación:** Un atacante puede manipular la entrada del usuario en el parámetro de búsqueda para alterar la lógica de la consulta, acceder a registros no autorizados o extraer información sensible de la base de datos.
* **Explotabilidad:** Alta, no requiere autenticación previa ni condiciones complejas.

## 4. Análisis de Falso Positivo
* **¿Es un falso positivo?:** **No.** Se verificó mediante la ejecución de herramientas de análisis estático (SAST) y pruebas locales que la entrada del usuario se concatena directamente en la instrucción sin el debido saneamiento o parametrización.
