current_char = ""
current_state = "q0"
ex_accepted_char = ["0", "1", "0"]
accepted = True

word = input(str("Digite a palavra: "))
print(type(word))

if len(word) != 3:
  accepted = False

if accepted:
  for i in range(len(word)):
    if word[i] != ex_accepted_char[i]:
      accepted = False
    
print(accepted)

if accepted:
  print("palavara %s aceita" %word)
else:
  print("palavra %s nao aceita" %word)



 
  
  