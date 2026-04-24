text = "Hello World"

print("Original String:", text)

and_result = ""
for char in text:
    and_result += chr(ord(char) & 127)

print("Result after AND with 127:", and_result)

xor_result = ""
for char in text:
    xor_result += chr(ord(char) ^ 127)

print("Result after XOR with 127:", xor_result)