def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            nuevo_char = chr((ord(char) - ascii_offset - desplazamiento) % 26 + ascii_offset)
            resultado += nuevo_char
        else:
            resultado += char
    return resultado

print("--- DESCIFRADOR CÉSAR (SIN LIBRERÍAS) ---")
mensaje_usuario = input("Introduce el criptograma:\n> ")

if mensaje_usuario.strip():
    print("\nGenerando las 25 combinaciones posibles...\n")
    for clave in range(1, 26):
        texto_prueba = descifrar_cesar(mensaje_usuario, clave)
        # Se imprime la clave con dos dígitos (ej. 01, 09, 25) para alinear el texto
        print(f"Clave {clave:02d}: {texto_prueba}")
else:
    print("No has introducido ningún mensaje.")