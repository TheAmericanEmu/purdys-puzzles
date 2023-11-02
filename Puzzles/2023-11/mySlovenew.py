code = "jyyqd://yomuita.vpz/4bcs5jle"
qwerty_dic = {}
num_to_qarty = {}

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
        new_url.append(num_to_qarty[key])
    else:
        new_url.append(char)

print("".join(new_url))
