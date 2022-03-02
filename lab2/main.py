current_index = 0
current_state = "q0"

def filter_word(word):

  words_accepted = ["if", "else", "then", "for"]

  file = open("palavras_aceitas.txt", "a")

  for i in range(len(words_accepted)):
    if word == words_accepted[i]:
      print("palavra %s aceita" %word)
      file.write(word)
      file.write("\n")

  file.close()
    

def main():

  words = []
  words_split = []

  file_words_accepted = open("palavras_aceitas.txt", "w")

  file_words_accepted.close()
  
  file = open("palavras.txt", "r")

  words.append(file.readlines())

  file.close()

  for i in range(len(words)):
    for j in range(len(words[i])):
        words_split.append(words[i][j].strip().split(" "))

  for i in range(len(words_split)):
    for j in range(len(words_split[i])):
      filter_word(words_split[i][j])

if __name__ == "__main__":
  main()