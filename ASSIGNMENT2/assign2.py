import math

message = input("Enter the message ")
rails = int(input("Enter the number of rails "))

encrypted = ""
for i in range(rails):
    encrypted += message[i::rails]

print("Encrypted Message", encrypted)

n = len(message)
row_length = math.ceil(n / rails)
decrypted = [''] * n

idx = 0
for r in range(rails):
    for c in range(row_length):
        pos = c * rails + r
        if pos < n:
            decrypted[pos] = encrypted[idx]
            idx += 1

print("Decrypted Message", "".join(decrypted))