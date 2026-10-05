def xor_zifraketa(datuak_bytes, gakoa_bytes):
    # Byte bakoitzari XOR eragiketa aplikatu
    return bytes([b ^ k for b, k in zip(datuak_bytes, gakoa_bytes)])

# 1. Datu probak
mezua = "GURE MEZUA HAU DA"
gakoa_hastapena = "GAKO1234567890"

# Gakoaren luzera mezuaren luzerara egokitu (behar adina errepikatuz)
gakoa = (gakoa_hastapena * (len(mezua) // len(gakoa_hastapena) + 1))[:len(mezua)]

# 2. String-ak byte kate (hex) bihurtu
mezua_bytes = mezua.encode('utf-8')
gakoa_bytes = gakoa.encode('utf-8')

# 3. Zifraketa (Mezua XOR Gakoa = Kriptograma)
kriptograma = xor_zifraketa(mezua_bytes, gakoa_bytes)

# 4. Deskodetzea (Kriptograma XOR Gakoa = Mezua)
deskodetua = xor_zifraketa(kriptograma, gakoa_bytes)

# 5. Emaitzak hexadezimalean erakutsi
print("--- DATUAK HEXADEZIMALEAN ---")
print(f"Jatorrizko mezua (hex): {mezua_bytes.hex()}")
print(f"Gakoa (hex):            {gakoa_bytes.hex()}")
print(f"Kriptograma (hex):      {kriptograma.hex()}")
print("-" * 30)

# 6. Egiaztapena
deskodetua_str = deskodetua.decode('utf-8')
print("\n--- EGIAZTAPENA ---")
print(f"Deskodetutako mezua: '{deskodetua_str}'")

if deskodetua == mezua_bytes:
    print("Emaitza: ZUZENA. Deskodetutako mezua eta jatorrizkoa zehazki berdinak dira.")
else:
    print("Emaitza: AKATSA. Deskodetzeak ez du jatorrizko mezua sortu.")