# Enter the key first

# Hit enter and write your message that you wanna encrypt

keyy= int(input( ))

inp= input().lower()

alph="abcdefghijklmnopqrstuvwxyz"

msg=""

for lett in inp:
    if lett in alph:
        req= alph.index(lett)+keyy 
        if req > 25 :
            req=req-26
        else:
            req=req
      
        msg=msg+alph[req] 
  
    else:
        msg=msg+lett

print("key:"+str(keyy))
print("your message:"+inp+"\n")

print("Encrypted message : "+msg)
