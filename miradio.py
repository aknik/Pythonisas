def hashcode(s):  # http://garage.pimentech.net/libcommonPython_src_python_libcommon_javastringhashcode/
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000


input ="av2j4j9n1bbaqaoh./ciowlvn/-pwlp/uzqu/oyglyj:kc"
output =""

line = ""
S1 = ""
S2 = ""

for i in range(0,len(input)-1,2):
    if (i == len(input)-1):
        S1 = S1 + input[:len(input)-1]
    else:

        S1 = S1 + input[i+1:i+2]
        S2 = input[i:i+1] + S2


line = S1 + S2

print (line)

b = "9876543210/:.zyxwvutsrqponmlkjihgfedcba"
a = "0123456789abcdefghijklmnopqrstuvwxyz.:/"

for i in range(0,len(line)):

    for j in range(0,39):

        if line[i] == a[j]:
            output = output + b[j]
            break
        else:
            if j == 38: output = output + line[i]

print (input)
print (output)
