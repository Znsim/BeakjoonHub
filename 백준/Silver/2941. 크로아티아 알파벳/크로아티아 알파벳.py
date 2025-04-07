word = input()
croa = ["c=","c-","dz=","d-","lj","nj","s=","z="]
count = 0

for i in croa:
    word = word.replace(i,"*")

print(len(word))