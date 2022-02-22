ex_accepted_char = ["0", "1", "0"]
accepted = True

word = input(str("Digite a palavra: "))

if len(word) != len(ex_accepted_char):
  accepted = False

if accepted:
  for i in range(len(word)):
    if word[i] != ex_accepted_char[i]:
      accepted = False

if accepted:
  print("palavara %s aceita" %word)
else:
  print("palavra %s nao aceita" %word)



 
  
  