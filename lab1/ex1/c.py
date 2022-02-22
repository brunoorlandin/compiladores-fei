current_index = 0
current_state = "q0"
accepted = True
ex_accepted_char = []

word = input(str("Digite a palavra: "))

for i in range(len(word)):
  current_index = i
  if word[i] != "0" and word[i] != "1":
    accepted = False
  elif word[i] != "0" and word[i] == "1":
    current_state = "q1"
    break
  if word[i] != "0" and word[i] == "1":
    current_state = "q1"
    break
  
if word[current_index] == "0":
  accepted = False

current_index = current_index + 1

for i in range(current_index, len(word)):
  if word[i] != "1":
    accepted = False

if accepted:
  print("palavara %s aceita" %word)
else:
  print("palavra %s nao aceita" %word)

