def buscar_publicaciones(cursor, usuario_input):
    # Remediación CWE-89: Uso de parámetros seguros para evitar SQL Injection
    query = "SELECT usuario, contenido, fecha FROM publicaciones WHERE usuario = %s"
    cursor.execute(query, (usuario_input,))
    return cursor.fetchall()
