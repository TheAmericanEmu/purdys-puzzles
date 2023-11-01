from string import ascii_lowercase as alp
coded = "jyyqd://yomuita.vpz/4bcs5jle"

def grab_letter(letter:str)-> int:
  count = 0
  if letter == "/" or letter == "." or letter ==":":
    return None
  for char in alp:
    if letter = char:
      return count
    count+=1
    
    
key = 6
newString=""
for code_leter in coded:
  alp_spot = grab_letter(code_leter)
  if alp_spot !=None:
    newString=newString+alp[(alp_spot-1)+key]
  if alp_spot==None:
    newString=newString+coded_letter

print(newString)
    
