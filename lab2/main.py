current_index = 0
current_state = "q0"

def token(word):
  type = word.upper()

  token = (type, word)

  return token

def filter_word(word):

  words_accepted = ["if", "else", "then", "for"]

  for i in range(len(words_accepted)):
    if word == words_accepted[i]:
      token_afd = token(word)
      print(token_afd)
    
def main():

  words = []
  words_split = []
  
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