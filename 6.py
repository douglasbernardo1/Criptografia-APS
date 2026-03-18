# RSA didático com blocos automático para mensagens (funciona com 'olá', emojis, etc.)

# 1) Parâmetros (seus primos pequenos de exemplo)
p = 61
q = 53
n = p * q
phi_n = (p - 1) * (q - 1)
e = 17
# encontrar d (inverso de e mod phi_n)
d = None
for k in range(1, 10000):
    if (k * phi_n + 1) % e == 0:
        d = (k * phi_n + 1) // e
        break

print(f"n = {n}, phi = {phi_n}, chave pública = {e}, chave privada = {d}")


def criptografar(texto, e, n):
    b = texto.encode()
    maxb = (n.bit_length() - 1) // 8
    blocos = [b[i : i + maxb] for i in range(0, len(b), maxb)]
    cifra = [pow(int.from_bytes(ch, "big"), e, n) for ch in blocos]
    tamanho = [len(ch) for ch in blocos]
    return cifra, tamanho


def descriptografar(cifra, tamanho, d, n):
    textodesc = bytearray()
    for c, l in zip(cifra, tamanho):
        textodesc += pow(c, d, n).to_bytes(l, "big")
    return textodesc.decode()


msg = "ISSO TEM QUE ATINGIR 218 CARACTERES É MUITO CARACTER NA VERCADED ENEM ANDAWIDAWMDWAOTA89WDAWUFMKAWK 30! AHHAHAHAHAHAHAHAHAHAHAHHAHAHA"
print("\nMensagem:", msg)
cifra, tamanho = criptografar(msg, e, n)
print("Criptografada:", cifra)
print("Descriptografada:", descriptografar(cifra, tamanho, d, n))
