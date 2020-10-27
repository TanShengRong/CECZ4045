import nltk
import glob

#files = glob.glob("C:/Users/owner/Desktop/NLP Dataset/*.txt")

tokens = []
stemmed_tokens = []
files = None
# function that accepts a list of tokens and returns
# number of tokens with a certain character count


dataset_select = input(
    "Please enter 1 for Game Guides, 2 for Deep Learning Papers, 3 for Food Reviews:")

if dataset_select == "1":
    # reads all text files in the current directory
    files = glob.glob("dataset1/*.txt")
    print(files)
elif dataset_select == "2":
    # reads all text files in the current directory
    files = glob.glob("dataset2/*.txt")
    print(files)
elif dataset_select == "3":
    # reads all text files in the current directory
    files = glob.glob("dataset3/*.txt")
    print(files)


report_name = input("Please enter a filename for the generated report:")
report = open(str(report_name) + ".txt", "w+", encoding="UTF-8")


def length_distributor(token_list, report):
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
        report.write("Tokens with " + str(obj.character_num) +
                     " characters: "+str(obj.count)+"\n")
        print(obj.count)
        report.write("List of tokens with "+str(obj.character_num)+"\n")
        counter = 0
        L = []
        for item in obj.token_list:
            if counter < 10:
                L.append(item)
                L.append(",")
                counter += 1
            else:
                report.writelines(L)
                report.write("\n")
                counter = 0


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
report.write("BEFORE STEMMING"+"\n")
report.write(""+"\n")
length_distributor(tokens, report)
report.write(""+"\n")


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
report.write("AFTER STEMMING"+"\n")
report.write(""+"\n")
length_distributor(stemmed_tokens, report)
report.write(""+"\n")
report.close()
