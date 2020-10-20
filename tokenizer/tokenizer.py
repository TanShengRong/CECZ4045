import nltk
import glob

#files = glob.glob("C:/Users/owner/Desktop/NLP Dataset/*.txt")
files = glob.glob("*.txt")  # reads all text files in the current directory
tokens = []
stemmed_tokens = []

# function that accepts a list of tokens and returns
# number of tokens with a certain character count


def length_distributor(token_list):
    # stores a list of integers corresponding to number of characters of tokens
    num_of_characters_list = []
    token_count_objects_list = []  # stores all instances of token_count objects
    for token in token_list:
        temp_length = len(token)
        if temp_length not in num_of_characters_list:
            num_of_characters_list.append(temp_length)
            new_token_count = token_count(temp_length)
            token_count_objects_list.append(new_token_count)
            new_token_count.token_list.append(token)
            new_token_count.count = new_token_count.count + 1
        else:
            for token_count_object in token_count_objects_list:
                if token_count_object.character_num == temp_length:
                    token_count_object.token_list.append(token)
                    token_count_object.count = token_count_object.count + 1

    print("sorting results...")
    token_count_objects_list.sort(key=lambda x: x.character_num)

    print("summarizing results...")
    for obj in token_count_objects_list:
        print("Tokens with " + str(obj.character_num) + " characters:")
        print(obj.count)


class token_count:
    """
    a class representing a certain unique character count
    keeps a list of tokens that have that character count 
    as well as count variable
    """

    def __init__(self, character_num):
        self.character_num = character_num
        self.token_list = []
        self.count = 0


print("tokenizing...")
for f in files:
    f = open(f, "r", encoding="utf-8")
    text = f.read()
    templist = nltk.word_tokenize(text)
    for item in templist:
        if item not in tokens:
            tokens.append(item)
        else:
            continue


print("No. of unique tokens:")
print(len(tokens))
length_distributor(tokens)

ps = nltk.PorterStemmer()
print("stemming...")
for token in tokens:
    s_token = ps.stem(token)
    if s_token not in stemmed_tokens:
        stemmed_tokens.append(s_token)
    else:
        continue

print("No. of unique tokens after stemming is:")
print(len(stemmed_tokens))
length_distributor(stemmed_tokens)
