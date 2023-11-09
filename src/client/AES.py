from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return ciphertext, cipher.iv

def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

# Example usage:
key = get_random_bytes(16)
message = "Hello, AES!"
ciphertext, iv = aes_encrypt(message, key)
decrypted_message = aes_decrypt(ciphertext, key, iv)

print(f"Original message: {message}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {decrypted_message}")

'''Testing

import numpy as np

def key_expansion(key):
    # Key expansion using the Rijndael key schedule
    key_words = [int(key[i:i+2], 16) for i in range(0, len(key), 2)]
    key_schedule = np.array(key_words).reshape(4, 4).T
    for i in range(4, 44):
        temp = key_schedule[:, i-1]
        if i % 4 == 0:
            temp = np.roll(temp, -1)
            temp = sub_bytes(temp)
            temp[0] ^= Rcon[i//4 - 1]
        key_schedule = np.column_stack((key_schedule, key_schedule[:, i-4] ^ temp))
    return key_schedule

def sub_bytes(state):
    # SubBytes transformation
    return [SBox[b] for b in state]

def shift_rows(state):
    # ShiftRows transformation
    state[1:] = [np.roll(row, -i) for i, row in enumerate(state[1:], 1)]
    return state

def mix_columns(state):
    # MixColumns transformation
    for i in range(4):
        col = state[i]
        state[i] = [
            multiply(0x02, col[0]) ^ multiply(0x03, col[1]) ^ col[2] ^ col[3],
            col[0] ^ multiply(0x02, col[1]) ^ multiply(0x03, col[2]) ^ col[3],
            col[0] ^ col[1] ^ multiply(0x02, col[2]) ^ multiply(0x03, col[3]),
            multiply(0x03, col[0]) ^ col[1] ^ col[2] ^ multiply(0x02, col[3])
        ]
    return state

def add_round_key(state, round_key):
    # AddRoundKey transformation
    return state ^ round_key

def encrypt_block(block, key_schedule):
    state = np.array([int(block[i:i+2], 16) for i in range(0, len(block), 2)]).reshape(4, 4).T
    key_schedule = key_expansion(key_schedule)

    state = add_round_key(state, key_schedule[:, :4])

    for round_num in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key_schedule[:, 4 * round_num: 4 * (round_num + 1)])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_schedule[:, 40:])

    return ''.join(format(b, '02x') for b in state.T.flatten())

def aes_encrypt(plaintext, key):
    ciphertext = ''
    for block_start in range(0, len(plaintext), 32):
        block = plaintext[block_start:block_start+32]
        ciphertext += encrypt_block(block, key)
    return ciphertext

def multiply(a, b):
    # Galois Field (256) multiplication
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        high_bit_set = a & 0x80
        a <<= 1
        if high_bit_set:
            a ^= 0x1b  # XOR with the irreducible polynomial x^8 + x^4 + x^3 + x + 1
        b >>= 1
    return p

# SBox and Rcon tables
SBox = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3

'''
