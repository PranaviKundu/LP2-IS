import math

p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)


e = 7
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

d = pow(e, -1, phi) 

print(f"n: {n}")
print(f"Public Key (e): {e}")
print(f"Private Key (d): {d}")

msg = int(input(f"Enter a number to encrypt (less than {n}): "))
cipher = pow(msg, e, n)
print(f"Encrypted Message: {cipher}")

decrypted = pow(cipher, d, n)
print(f"Decrypted Message: {decrypted}")