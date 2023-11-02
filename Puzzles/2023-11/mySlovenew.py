code = ""
qwerty_dic = {}
num_to_qarty = {}

with open("C:\\Users\\Certiport\\Downloads\\thing.txt") as file:
    for line in file:
        code=code+line.strip()
def make_dics():
    keybroad ="qwertyuiopasdfghjklzxcvbnm"
    for i in range(len(keybroad)):
        char = keybroad[i]
        qwerty_dic.update({char:i})
    keybroad ="qwertyuiopasdfghjklzxcvbnm"
    for i in range(len(keybroad)):
        char = keybroad[i]
        num_to_qarty.update({i:char})

make_dics()

new_url =[]
for char in code:
    if char.isalpha()==True:
        key = qwerty_dic[char]
        if key-1 <0:
            key =0
        else:
            key-=1
        letter = None
        if num_to_qarty[key] == "l" and num_to_qarty[key+1] == "z":
            letter="m"
        elif num_to_qarty[key] == "p" and num_to_qarty[key+1] == "a":
            letter = "l"
        elif num_to_qarty[key+1] == "q":
            letter = "p"
        if letter == None:
            letter = num_to_qarty[key]
        new_url.append(letter)
    else:
        new_url.append(char)

print("".join(new_url))

