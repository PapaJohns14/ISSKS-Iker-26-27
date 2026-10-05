from langdetect import detect, LangDetectException

def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Determinar si es mayúscula o minúscula para el código ASCII
            ascii_offset = 65 if char.isupper() else 97
            # Aplicar el desplazamiento hacia atrás
            nuevo_char = chr((ord(char) - ascii_offset - desplazamiento) % 26 + ascii_offset)
            resultado += nuevo_char
        else:
            # Mantener espacios y signos de puntuación intactos
            resultado += char
    return resultado

def romper_cifrado(criptograma):
    print(f"Criptograma original: '{criptograma}'\n")
    print("Iniciando ataque de fuerza bruta con autodetección de idioma...\n")
    
    # Probar los 25 desplazamientos posibles
    for clave in range(1, 26):
        texto_prueba = descifrar_cesar(criptograma, clave)
        
        try:
            # Detectar el idioma del texto descifrado
            idioma = detect(texto_prueba)
            
            # Si detecta que es español ('es'), hemos encontrado la clave
            if idioma == 'es':
                print("-" * 40)
                print(f"¡ÉXITO! Clave inferida: {clave} (Desplazamiento)")
                print(f"Mensaje descifrado: {texto_prueba}")
                print("-" * 40)
                return texto_prueba, clave
        except LangDetectException:
            # Ignorar si langdetect no puede procesar la cadena
            pass
            
    print("No se pudo detectar un mensaje coherente en español.")
    return None, None

if __name__ == "__main__":
    mensaje_cifrado = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"
    romper_cifrado(mensaje_cifrado)