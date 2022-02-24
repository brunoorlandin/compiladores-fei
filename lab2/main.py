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

  words = []
  words_split = []

  words_accepted = [["i", "f"], ["f", "o", "r"], ["e", "l", "s", "e"], ["t", "h", "e", "n"]]
  
  file = open("palavras.txt", "r")

  words.append(file.readlines())

  for i in range(len(words)):
    for j in range(len(words[i])):
        words_split.append(words[i][j].strip().split(" "))

  print(words_split)

  for i in range(len(words_split)):
      for j in range(len(words_split[i])):
        accepted = filter_word(words_accepted[i],words_split[i][j])

        if accepted == True:
            print("palavra %s aceita" %words_split[i][j])

        accepted = False

if __name__ == "__main__":
  main()