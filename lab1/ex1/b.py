accepted = True
ex_accepted_char = []

word = input(str("Digite a palavra: "))

for i in range(len(word)):
  if word[0] == "0":
    ex_accepted_char.append("0")
  else:
    ex_accepted_char.append("1")

for j in range(len(word)):
  if word[j] != ex_accepted_char[j]:
    accepted = False

if accepted:
  print("palavara %s aceita" %word)
else:
  print("palavra %s nao aceita" %word)