'''
take 64-bit input from user
split in half (32-bit each)

'''

text = input("Enter text to encrypt: ")
key = input("Enter key: ")


# converts hex to binary
def hex2bin(hex_string):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin_string = ""
    for char in hex_string:
        bin_string = bin_string + mp[char]
    return bin_string


# convert binary to hex
def bin2hex(bin_string):
    mp = {"0000": "0",
          "0001": "1",
          "0010": "2",
          "0011": "3",
          "0100": "4",
          "0101": "5",
          "0110": "6",
          "0111": "7",
          "1000": "8",
          "1001": "9",
          "1010": "A",
          "1011": "B",
          "1100": "C",
          "1101": "D",
          "1110": "E",
          "1111": "F"}
    hex_string = ""
    for i in range(0, len(bin_string), 4):
        str = ""
        str = str + bin_string[i]
        str = str + bin_string[i + 1]
        str = str + bin_string[i + 2]
        str = str + bin_string[i + 3]
        hex_string = hex_string + mp[str]
    return hex_string

# convert string to decimal to binary
def str2deci(text):
    deci = ""
    for char in text:
        deci = deci + str(ord(char))
    return deci

strio = str2deci('hello')

def deci2bin(deci):
    bin_string = ""
    for char in deci:
        bin_string = bin_string + format(int(char), '04b')
    return bin_string

#convert binary to hex and back
def bin2deci(bin_string):
    bin_stringC = bin_string
    deci = 0
    i = 0
    n = 0
    while bin_stringC != 0:
        deci = deci + (bin_stringC % 10) * pow(2, i)
        bin_stringC = bin_stringC // 10
        i += 1
    return deci

def deci2bin(deci):
    deci = int(deci)
    rep = bin(deci).replace("0b", "")
    if(len(rep) % 4 !=0):
        div = len(rep) / 4
        div = int(div)
        c = (4* (div + 1)) - len(rep)
        for i in range(0, c):
            rep = '0' + rep
    bin_string = rep
    return bin_string

stext = str2deci(text)
btext = deci2bin(stext)

skey = str2deci(key)
bkey = deci2bin(skey)



#tables
init_perm_table = [58, 50, 42, 34, 26, 18, 10, 2,
                  60, 52, 44, 36, 28, 20, 12, 4,
                  62, 54, 46, 38, 30, 22, 14, 6,
                  64, 56, 48, 40, 32, 24, 16, 8,
                  57, 49, 41, 33, 25, 17, 9 ,1,
                  59, 51, 43, 35, 27, 19 ,11 ,3,
                  61 ,53 ,45 ,37 ,29 ,21 ,13 ,5,
                  63 ,55 ,47 ,39 ,31 ,23 ,15 ,7]

    
choice_2 = [14, 17, 11, 24, 1, 5,
                3, 28, 15, 6, 21, 10,
                23, 19, 12, 4, 26, 8,
                16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55,
                30 ,40 ,51 ,45 ,33 ,48,
                44 ,49 ,39 ,56 ,34 ,53,
                46 ,42 ,50 ,36 ,29 ,32]

sbox = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
             0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
             4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
             15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
             3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
             0 ,14 ,7 ,11 ,10 ,4 ,13 ,1 ,5 ,8 ,12 ,6 ,9 ,3 ,2 ,15,
             13 ,8 ,10 ,1 ,3 ,15 ,4 ,2 ,11 ,6 ,7 ,12 ,0 ,5 ,14 ,9],

            [10 ,0 ,9 ,14 ,6 ,3 ,15 ,5 ,1 ,13 ,12 ,7 ,11 ,4 ,2 ,8,
             13 ,7 ,0 ,9 ,3 ,4 ,6 ,10 ,2 ,8 ,5 ,14 ,12 ,11 ,15 ,1,
             13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
             1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
             13 ,8 ,11 ,5 ,6 ,15 ,0 ,3 ,4 ,7 ,2 ,12 ,1 ,10 ,14 ,9,
             10 ,6 ,9 ,0 ,12 ,11 ,7 ,13 ,15 ,1 ,3 ,14 ,5 ,2 ,8 ,4,
             3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
             14 ,11 ,2 ,12 ,4 ,7 ,13 ,1 ,5 ,0 ,15 ,10 ,3 ,9 ,8 ,6,
             4 ,2 ,1 ,11 ,10 ,13 ,7 ,8 ,15 ,9 ,12 ,5 ,6 ,3 ,0 ,14,
             11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

            [12 ,1 ,10 ,15 ,9 ,2 ,6 ,8 ,0 ,13 ,3 ,4 ,14 ,7 ,5 ,11,
             10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
             9 ,14 ,15 ,5 ,2 ,8 ,12 ,3 ,7 ,0 ,4 ,10 ,1 ,13 ,11 ,6,
             4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

            [4 ,11 ,2 ,14 ,15 ,0 ,8 ,13 ,3 ,7 ,9 ,5 ,6 ,1 ,12 ,10,
             13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
             1 ,4 ,11 ,13 ,12 ,3 ,7 ,14 ,10 ,15 ,6 ,8 ,0 ,5 ,9 ,2,
             6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

            [13 ,2 ,8 ,4 ,6 ,15 ,11 ,1 ,10 ,9 ,3 ,14 ,5 ,0 ,12 ,7,
             1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
             7 ,11 ,4 ,1 ,9 ,12 ,14 ,2 ,0 ,6 ,10 ,13 ,15 ,3 ,5 ,8,
             2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

keyp = [57, 49, 41, 33, 25, 17, 9,
               1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27,
               19, 11, 3, 60, 52, 44, 36,
               63, 55, 47, 39, 31, 23, 15,
               7, 62, 54, 46, 38, 30, 22,
               14, 6, 61, 53, 45, 37, 29,
               21, 13, 5, 28, 20, 12, 4],
               
    
Ebox = [32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 33]
    
perm = [16, 7, 20, 21,
             29, 12, 28, 17,
            1, 15, 23, 26,
            5, 18, 31, 10,
            2, 8, 24, 14,
            32, 27, 3, 9,
            19, 13, 30, 6,
            22, 11, 4, 25]

final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

def perm(k, arr, b):
    permutation = ""
    for i in range(0, b):
        permutation = permutation + k[arr[i] - 1]
    return permutation

def shift_left(k, shifts):
    s = ""
    for i in range(shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k

def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans



def encrypt(plaintext, key):
    ciphertext = ""
    text = hex2bin(btext)

    text = perm(text, init_perm_table, 64)

    left = text[0:32]
    right = text[32:64]
    for i in range(0,16):
        right_expanded = perm(right, Ebox, 48)
        key = hex2bin(bkey)
        key = perm(key, keyp, 56)
        left_key = key[0:28]
        right_key = key[28:56]
        left_key = shift_left(left_key, 1)
        right_key = shift_left(right_key, 1)
        key = left_key + right_key
        key = perm(key, choice_2, 48)

        xor_x = xor(right_expanded, key)

        sbox_str = sbox_substitution(xor_x, sbox)

        sbox_str = perm(sbox_str, perm, 32)

        result = xor(left, sbox_str)
        left = result

        if i != 15:
            left, right = right, left
            print(f"Round {i + 1}: {bin2hex(left)} {bin2hex(right)}")

        comb = left + right
        ciphertext = perm(comb, final_perm, 64)
    return ciphertext



def decrypt(ciphertext, key):
    plaintext = ""
    return plaintext



def sbox_substitution(block, sbox):
    substituted_block = ""
    for i in range(0, len(block), 6):
        row = int(block[i] + block[i + 5], 2)
        col = int(block[i + 1:i + 5], 2)
        substituted_block += format(sbox[row][col], '04b')
    return substituted_block





ciphertext = encrypt(text, key)
print("Ciphertext:", ciphertext)
plaintext = decrypt(ciphertext, key)
print("Plaintext:", plaintext)





