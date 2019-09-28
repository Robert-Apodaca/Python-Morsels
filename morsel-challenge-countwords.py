#def count_words(phrase):
 #   words = phrase.split()
  #  print(words)
   # (x, words.count(s) for x in set(words)
dictionarytally = {}

def counts_words(phrase):
    words = phrase.split()
    #print(words)
    for x in words:
        tally = words.count(x)
      # print(tally)
        x = x.lower() #added .lower
        dictionarytally[x] = tally
    print(dictionarytally)


   # for x in set

counts_words("Count all the words count all the words")

counts_words("I pledge allegiance to the flag of the united states of America and to the republics for which it stands one nation under God, indivisible with liberty and justice for all")

