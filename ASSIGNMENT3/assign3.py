P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

def permute(bits, table):
    return "".join(bits[i - 1] for i in table)

def shift_left(bits, n=1):
    for _ in range(n):
        bits = bits[1:] + bits[0]
    return bits

def xor(a, b):
    return "".join('0' if a[i] == b[i] else '1' for i in range(len(a)))

def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])

def f_k(bits, key):
    L, R = bits[:4], bits[4:]
    expanded_R = permute(R, EP)
    xor_res = xor(expanded_R, key)
    s0_out = sbox_lookup(xor_res[:4], S0)
    s1_out = sbox_lookup(xor_res[4:], S1)
    p4_out = permute(s0_out + s1_out, P4)
    return xor(L, p4_out) + R

# --- Key Generation ---
main_key = input("Enter 10-bit binary key ")
p10_key = permute(main_key, P10)
L_k, R_k = p10_key[:5], p10_key[5:]

# Generate K1 (Shift by 1)
L_k, R_k = shift_left(L_k), shift_left(R_k)
K1 = permute(L_k + R_k, P8)

# Generate K2 (Shift by 2 more)
L_k, R_k = shift_left(L_k, 2), shift_left(R_k, 2)
K2 = permute(L_k + R_k, P8)

# --- Encryption ---
plaintext = input("Enter 8-bit binary text ")

def sdes_process(data, ka, kb):
    temp = permute(data, IP)
    temp = f_k(temp, ka)
    temp = temp[4:] + temp[:4] # Swap
    temp = f_k(temp, kb)
    return permute(temp, IP_INV)

ciphertext = sdes_process(plaintext, K1, K2)
decrypted = sdes_process(ciphertext, K2, K1)

print("\n--- Results ---")
print("K1 Generated", K1)
print("K2 Generated", K2)
print("Encrypted Binary", ciphertext)
print("Decrypted Binary", decrypted)