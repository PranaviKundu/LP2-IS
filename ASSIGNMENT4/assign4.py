SBOX = [i for i in range(256)]
import random
random.seed(42) 
random.shuffle(SBOX)


def get_matrix(text):
    matrix = []
    for i in range(0, 16, 4):
        
        matrix.append([ord(c) for c in text[i:i+4]])
    return matrix

def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = SBOX[state[i][j]]
    return state


def shift_rows(state):
    state[1] = state[1][1:] + state[1][:1] 
    state[2] = state[2][2:] + state[2][:2] 
    state[3] = state[3][3:] + state[3][:3] 
    return state


def mix_columns(state):
    for j in range(4):
        
        col_total = state[0][j] ^ state[1][j] ^ state[2][j] ^ state[3][j]
        for i in range(4):
            state[i][j] ^= col_total
    return state
ix
def add_round_key(state, key_mat):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= key_mat[i][j]
    return state


msg = input("Enter 16-character message: ")
key = input("Enter 16-character key: ")


msg = msg.ljust(16)[:16]
key = key.ljust(16)[:16]

state = get_matrix(msg)
key_mat = get_matrix(key)

print("\n--- Starting AES 10 Rounds ---")


state = add_round_key(state, key_mat)


for round_num in range(1, 10):
    state = sub_bytes(state)
    state = shift_rows(state)
    state = mix_columns(state)
    state = add_round_key(state, key_mat)
    print(f"Round {round_num} Complete")


state = sub_bytes(state)
state = shift_rows(state)
state = add_round_key(state, key_mat)


result_hex = ""
for row in state:
    for val in row:
        result_hex += hex(val)[2:].zfill(2).upper()

print("\nFinal Encrypted Message (Hex):", result_hex)