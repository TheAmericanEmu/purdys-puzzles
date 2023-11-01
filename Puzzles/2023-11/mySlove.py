from string import ascii_lowercase as alp

coded = "jyyqd://yomuita.vpz/4bcs5jle"

def grab_letter(letter:str)-> int:
  count = 0
  if letter == "/" or letter == "." or letter ==":":
    return None
  for char in alp:
    if letter == char:
      return count
    count+=1


    
key1=-3
key2=-7
key3=-7
key4=-3
key5=15
keys=[-3,-7,-7,-3,15]
newString=""
five_spilt=[]
count = 0
spilt = ""
for char in coded:
  count+=1
  
  spilt=spilt+char
  print(count)
  if count == 5:
    five_spilt.append(spilt)
    spilt=""
    count=0
for code_letter in coded:
  alp_spot = grab_letter(code_letter)
  
  ##  if alp_spot !=None:
  ##    if (alp_spot)+key >=26:
  ##      alp_spot=(26-((alp_spot-1)+key))*-1
  ##      print(alp_spot)
  ##    else:
  ##      alp_spot=key+(alp_spot-1)
  ##    newString=newString+alp[alp_spot]
  ##  if alp_spot==None:
  ##    newString=newString+code_letter
  ##coded=newString
print(five_spilt)
    
print("Done")
