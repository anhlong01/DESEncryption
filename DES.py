import Key as k
import S_box as sbox
from ftfy import fix_encoding
# ------------------------------------------------


def XOR(a, b, length):
    a1 = list(a)
    b1 = list(b)
    c1 = list()
    for i in range(length):
        c1.append(str(int(a1[i]) ^ int(b1[i])))
    m = ''.join(c1)
    return m


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def decimalToBinary(n):
    m = bin(n).replace("0b", "")
    return m.zfill(4)

# -----------------------------------------------------------
def encrypt(msg):
    if msg == "":
        return ""
    cipher = []
    Left_msg = ''
    Right_msg = ''
    temp = [format(ord(c), "x") for c in msg]
    msg = ''.join(temp)
    list1 = [msg[i:i+16] for i in range(0, len(msg),16)]
    if(len(list1[-1]) != 16):
        list1[-1] += '0'*(16-len(list1[-1]))
    for i in range(len(list1)):
        partial_msg_list = ["{0:04b}".format(int(j, 16)) for j in list1[i]]
        partial_msg = list(''.join(partial_msg_list))
        partial_msg_string = ''
        # print(''.join(partial_msg_list))
        for x in range(8):
            for y in range(8):
                partial_msg_string += partial_msg[sbox.IP[x][y] - 1]
        # print(partial_msg_string)

        Left_msg = partial_msg_string[:int(len(partial_msg_string) / 2)]
        Right_msg = partial_msg_string[int(len(partial_msg_string) / 2):]
        # print(Left_msg+Right_msg)

        for j in range(16):
            Left_temp_msg = Right_msg
            f_right_msg = ''
            f_right_list = list(Right_msg)
            for x in range(8):
                for y in range(6):
                    f_right_msg = f_right_msg + f_right_list[sbox.EP[x][y] - 1]
            # print(f_right_msg)
            # print(k_after_PC2_Permutation[j])
            m = XOR(k.k_after_PC2_Permutation[j], f_right_msg, len(f_right_msg))
            B = [m[x:x + 6] for x in range(0, len(m), 6)]

            S_box_output = ''
            for l in range(len(B)):
                S_box_output += decimalToBinary(
                    sbox.dict1['S' + str(l + 1)][binaryToDecimal(int(B[l][0] + B[l][5]))][binaryToDecimal(int(B[l][1:5]))])
            # print(S_box_output)

            S_box_list = list(S_box_output)
            S_box = ''
            for x in range(8):
                for y in range(4):
                    S_box += S_box_list[sbox.P[x][y] - 1]

            # print(S_box)

            Right_msg = XOR(Left_msg, S_box, len(S_box))
            Left_msg = Left_temp_msg
            # print(Left_msg, Right_msg)

        Left_msg, Right_msg = Right_msg, Left_msg

        partial_cipher = Left_msg + Right_msg
        partial_cipher_list = list(partial_cipher)
        bin_cipher_text = ''
        for x in range(8):
            for y in range(8):
                bin_cipher_text += partial_cipher_list[sbox.IP_inverse[x][y] - 1]

        l11 = [bin_cipher_text[i:i + 4] for i in range(0, len(bin_cipher_text), 4)]
        # print(l11)

        l12 = [hex(int(i, 2)).replace("0x", "") for i in l11]
        # print(l12)
        cipher_text = ''.join(l12)
        cipher.append(cipher_text)
    cipher = "".join(cipher)
    return cipher

# ---------------------------
def decrypt(msg):
    plain = []
    plain_temp = []
    Left_msg = ''
    Right_msg = ''
    list1 = [msg[i:i+16] for i in range(0, len(msg),16)]
    if msg == "":
        return ""
    if(len(list1[-1]) != 16):
        list1[-1] += '0'*(16-len(list1[-1]))

    for i in range(len(list1)):
        partial_msg_list = ["{0:04b}".format(int(j, 16)) for j in list1[i]]
        partial_msg = list(''.join(partial_msg_list))
        partial_msg_string = ''
        # print(''.join(partial_msg_list))
        for x in range(8):
            for y in range(8):
                partial_msg_string += partial_msg[sbox.IP[x][y] - 1]
        # print(partial_msg_string)

        Left_msg = partial_msg_string[:int(len(partial_msg_string) / 2)]
        Right_msg = partial_msg_string[int(len(partial_msg_string) / 2):]
        # print(Left_msg+Right_msg)

        for j in range(15,-1,-1):
            Left_temp_msg = Right_msg
            f_right_msg = ''
            f_right_list = list(Right_msg)
            for x in range(8):
                for y in range(6):
                    f_right_msg = f_right_msg + f_right_list[sbox.EP[x][y] - 1]
            # print(f_right_msg)
            # print(k_after_PC2_Permutation[j])
            m = XOR(k.k_after_PC2_Permutation[j], f_right_msg, len(f_right_msg))
            B = [m[x:x + 6] for x in range(0, len(m), 6)]

            S_box_output = ''
            for l in range(len(B)):
                S_box_output += decimalToBinary(
                    sbox.dict1['S' + str(l + 1)][binaryToDecimal(int(B[l][0] + B[l][5]))][
                        binaryToDecimal(int(B[l][1:5]))])
            # print(S_box_output)

            S_box_list = list(S_box_output)
            S_box = ''
            for x in range(8):
                for y in range(4):
                    S_box += S_box_list[sbox.P[x][y] - 1]

            # print(S_box)

            Right_msg = XOR(Left_msg, S_box, len(S_box))
            Left_msg = Left_temp_msg
            # print(Left_msg, Right_msg)

        Left_msg, Right_msg = Right_msg, Left_msg

        partial_cipher = Left_msg + Right_msg
        partial_cipher_list = list(partial_cipher)
        bin_cipher_text = ''
        for x in range(8):
            for y in range(8):
                bin_cipher_text += partial_cipher_list[sbox.IP_inverse[x][y] - 1]

        l11 = [bin_cipher_text[i:i + 4] for i in range(0, len(bin_cipher_text), 4)]
        # print(l11)

        l12 = [hex(int(i, 2)).replace("0x", "") for i in l11]
        plain_temp.clear()
        for i in range(0, len(l12),2):
            temp = l12[i] + l12[i+1]
            if temp != "00":
                plain_temp.append(temp)
        # print(l12)
        plain_text = ''.join(plain_temp)
        plain.append(plain_text)
    plain = "".join(plain)
    plain = plain.replace("8f", "")
    plain = plain.replace("90", "")
    plain = plain.replace("81", "")
    plain = plain.replace("8d", "")
    plain = plain.replace("9d", "")
    plain2 = bytearray.fromhex(plain).decode('cp1252')

    return plain2
# -------------------------------
# msg = input('Enter a plaintext:')
# temp = [format(ord(c), "x") for c in msg]
# msg = ''.join(temp)
# list1 = [msg[i:i+16] for i in range(0, len(msg),16)]
# if(len(list1[-1]) != 16):
#     list1[-1] += '0'*(16-len(list1[-1]))
# print(list1)
#
#
# y = encrypt(list1)
# print(y)
# plain = decrypt(y)
# print(plain)

# ---------------------
# y = ''.join(y)

# temp = bytearray.fromhex(m).decode()

# y = encrypt(m)

# print(y)

# y = ''.join(y)


# temp = bytearray.fromhex(y).decode()
# print(temp)
