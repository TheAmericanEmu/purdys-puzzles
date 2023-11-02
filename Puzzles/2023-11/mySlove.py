
from string import ascii_lowercase as alp

coded = "jyyqd://yomuita.vpz/4bcs5jle"
#https://youtube.com/4bcs5jle
def grab_letter(letter:str)-> int:
  count = 0
  if letter == "/" or letter == "." or letter ==":":
    return None
  for char in alp:
    if letter == char:
      return count
    count+=1


def letter_decode(letter,key):
  alp_spot = grab_letter(letter)
  if alp_spot !=None:
    if (alp_spot)+key >=26:
      alp_spot=(26-((alp_spot-1)+key))*-1
      print(alp_spot)
    else:
      alp_spot=key+(alp_spot-1)
    return(alp[alp_spot])
  return(letter)

    

keys=[25,22,22,26,16]
newString=""
five_spilt=[]
count = 0
spilt = ""
new_url = ""
for char in coded:
  
  spilt=spilt+char
  count+=1
  print(count)
  if count == 5:
    five_spilt.append(spilt)
    spilt=""
    count=0
five_spilt.append(spilt)
for group in five_spilt:
  for i in range(len(group)):
    char = group[i]
    key = keys[i]
    new_url= new_url+letter_decode(char,key)

print(new_url)    
print("Done")
