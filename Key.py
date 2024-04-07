PC1 = [
        [57, 49, 41, 33, 25, 17, 9], [1, 58, 50, 42, 34, 26, 18], [10, 2, 59, 51, 43, 35, 27], [19, 11, 3, 60, 52, 44, 36],
        [63, 55, 47, 39, 31, 23, 15], [7, 62, 54, 46, 38, 30, 22],[14, 6, 61, 53, 45, 37, 29], [21, 13, 5, 28, 20, 12, 4]
]

PC2 = [
    [14, 17, 11, 24, 1, 5], [3, 28, 15, 6, 21, 10], [23, 19, 12, 4, 26, 8], [16, 7, 27, 20, 13, 2], [41, 52, 31, 37, 47, 55],
    [30, 40, 51, 45, 33, 48], [44, 49, 39, 56, 34, 53], [46, 42, 50, 36, 29, 32]
]
Rotation_KEY = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# ---------------------------------------------------------

key = '0101010101010101'
#key = list(input('Enter a 64 bit hexadecimal number:'))
klist1 = ["{0:04b}".format(int(i, 16)) for i in key]

k56_final = ''.join(klist1)
k56_list = list(k56_final)
#print(len(k56_list))

k_afterpermutation = []
for i in range(8):
    for j in range(7):
        k_afterpermutation.append(k56_list[PC1[i][j]-1])

klist_final = ''.join(k_afterpermutation)

Left_key = klist_final[:int(len(klist_final)/2)]
Right_key = klist_final[int(len(klist_final)/2):]
#print(Left_key)
#print(Right_key)


Left_keyList = [Left_key]
Right_keyList = [Right_key]
j = 0
for i in range(len(Rotation_KEY)):
    j = j + Rotation_KEY[i]
    Left_keyList.append(Left_key[j:]+Left_key[:j])
    Right_keyList.append(Right_key[j:]+Right_key[:j])
#print(Left_keyList)
#print(Right_keyList)


k_after_PC2_Permutation = []
for i in range(1,len(Left_keyList)):
    m = list(Left_keyList[i]+Right_keyList[i])
    k_for_PC2_Permutation = []
    for i in range(8):
        for j in range(6):
            k_for_PC2_Permutation.append(m[PC2[i][j]-1])
    k_after_PC2_Permutation.append(''.join(k_for_PC2_Permutation))

