current_index = 0
current_state = "q0"

def filter_word(ex_accepted_char, word):
  for i in range(len(ex_accepted_char)):
    if word[i] != ex_accepted_char[i]:
      accepted = False
    else:
      accepted= True

  return accepted

def main():

  word = input(str("Digite a palavra: "))
  
  accepted = filter_word(["i", "f"], word)
  #accepted = filter_word(["e", "l", "s", "e"], word)

  if accepted:
    print("AFD aceito")
    print("palavra: %s" %word)
  else:
    print("AFD nao aceito")
    print("palavra: %s" %word)

if __name__ == "__main__":
  main()