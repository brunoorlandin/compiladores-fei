current_index = 0
current_state = "q0"

def filter_word(ex_accepted_char, word):

  accepted = False

  if word != "":
    for i in range(len(ex_accepted_char)):
      if word[i] != ex_accepted_char[i]:
        accepted = False
      else:
        accepted= True
    
  return accepted

def main():

  word = input(str("Digite a palavra: "))
  
  words = [["i", "f"], ["f", "o", "r"], ["e", "l", "s", "e"], ["t", "h", "e", "n"]]

  for i in range(len(words)):
    accepted = filter_word(words[i],word)

    if accepted == True:
      break

  if accepted:
    print("AFD aceito")
    print("palavra: %s" %word)
  else:
    print("AFD nao aceito")
    print("palavra: %s" %word)

if __name__ == "__main__":
  main()