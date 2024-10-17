
def count_word(sentence,word_count):
    words=sentence.split()
    for word in words:
        word=word.lower()
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

def print_word_frequencies(word_count):
    for word,frequency in word_count.items():
        print(f"{word}:{frequency}")

def main():
    sentence=input("Enter ta sentence: ")
    word_count={}
    count_word(sentence,word_count)
    print("Word Frequencies")
    print_word_frequencies(word_count)

if __name__=="__main__":
    main()

