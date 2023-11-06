code = ""
qwerty_dic = {}
num_to_qwerty = {}


def make_dics():
    keybroad =".qwertyuiopasdfghjklzxcvbnm."
    for i in range(len(keybroad)):
        char = keybroad[i]
        qwerty_dic.update({char:i})
    keybroad =".qwertyuiopasdfghjklzxcvbnm."
    for i in range(len(keybroad)):
        char = keybroad[i]
        num_to_qwerty.update({i:char})




def decode_input(input_str:str)->str:
    """decoded the input using a qwerty chiper"""
    make_dics()
    new_url =[]
    
    for char in input_str:
        letter=None
        if char == char.upper() and char.isalpha()==True:
            is_cap = True
        if char.isnumeric()==True:
            letter=str(int(char)+1)
        if char.isalnum==False:
            letter=char
        if char.isalpha()==True:
            key = qwerty_dic[char.lower()]
            if num_to_qwerty[key-1]==".":
                key =0
            else :
                key-=1
            if num_to_qwerty[key] == "l" and num_to_qwerty[key-1] == "z":
                letter="m"
            elif num_to_qwerty[key] == "p" and num_to_qwerty[key-1] == "a":
                letter = "l"
            elif num_to_qwerty[key+1] == "q" and num_to_qwerty[key] == ".":
                letter = "p"
            if letter == None:
                letter = num_to_qwerty[key]
        if is_cap    
        new_url.append(letter)

    return("".join(new_url))

def incode_input(input_str:str)->str:
    make_dics()
    new_url =[]
    
    for char in input_str:
        is_cap = False
        letter=None
        if char == char.upper() and char.isalpha()==True:
            is_cap = True
        if char.isnumeric()==True:
            letter=str(int(char)+1)
            
        if char.isalpha()==True:
            key = qwerty_dic[char.lower()]
            if key-1 <0:
                key =0
            else:
                key+=1
            letter=num_to_qwerty[key]
            if num_to_qwerty[key+1] =="a" and num_to_qwerty[key]=="p":
                letter="q"
            elif num_to_qwerty[key] =="l" and num_to_qwerty[key+1]=="z":
                letter="q"
            elif num_to_qwerty[key] =="m" and num_to_qwerty[key+1]==".":
                letter="z"
            
                
            new_url.append(num_to_qwerty[key])

    return("".join(new_url))
    

print(decode_input("q"))
