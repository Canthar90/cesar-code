alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def change_to_numbers(list, alphabet):
  out_list=[]
  for l in list:
    if l == ' ':
     out_list.append(' ')
    else:
      out_list.append(alphabet.index(l))
    #if l == ' ':
    #  out_list.append(' ')
    #else:
    #  for a in range(0,len(alphabet)) :
    #    if l==alphabet[a]:
    #      counter = a
    #      out_list.append(counter)
  # print(out_list)
  return out_list



def encode_list(lista,alphabet,shift):
  out_list=[]
  out_stat=''
  for l in range(0, len(lista)):
    if lista[l]==' ':
      out_list.append(' ')
      out_stat +=' '
    else:
      newone = int(lista[l]) + shift
      if newone>25:
        newone-=25
        out_list.append(alphabet[newone])
        out_stat += alphabet[newone]
      else:
        out_list.append(alphabet[newone])
        out_stat+=alphabet[newone]

  return out_stat

def decode_list(lista,alphabet,shift):
  out_list=[]
  out_stat=''
  for l in range(0, len(lista)):
    if lista[l]==' ':
      out_list.append(' ')
      out_stat +=' '
    else:
      newone = int(lista[l]) - shift
      if newone<0:
        newone+=25
        out_list.append(alphabet[newone])
        out_stat += alphabet[newone]
      else:
        out_list.append(alphabet[newone])
        out_stat+=alphabet[newone]

  return out_stat



interrupt=False
#​

while interrupt==False:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  text_list=[]
  text_list[:0]=text
  # print(text_list)


  number_list=change_to_numbers(text_list,alphabet)
  #print(number_list)
  if direction=='encode':
    encodet_statment=encode_list(number_list,alphabet,shift)
    print(f"Your encodet message is : {encodet_statment}")
  elif direction=='decode':
    decodet_statment=decode_list(number_list,alphabet,shift)
    print(f"Your encodet message is : {decodet_statment}")

  feedback=input('Do you want to encrypt or decrypt another message (Y/N)?  ')
  feedback=feedback.lower()
  if feedback=='n':
    interrupt=True