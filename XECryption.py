with open("encrypted-text.txt", "r") as myfile:
    data = myfile.read().replace("\n","")

data = data.split(".")[1:]
""" Creating dictionary to get a histogram containing
the number of occurrences of every sum """
d = {}
sums = []
for i in range(0, len(data), 3):
    temp = map(int, (data[i:i+3]))
    s = sum(temp)
    sums.append(s)
    if s not in d.keys():
        d[s] = 1
    else:
        d[s] += 1

max_occur = 0
for key in d.keys():
    if d[key]>max_occur:
        max_occur = d[key]
        password = key

output = ''
for i in sums:
    curr = i-(password-32)
    output += chr(curr)
with open("decrypted-text.txt", "w") as myfile:
    myfile.write(output)
