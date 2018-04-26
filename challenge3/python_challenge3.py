

def check_next(char, col, line):
    if char.isupper():
        return False
    all_up = True
    for index in range(col - 3, col + 4):
        if index == col:
            continue 
        if index >= 0 and index < len(line):
            all_up = line[index].isupper() and all_up
        else:
            all_up = False   

    if (all_up):
        result = True
        if col - 4 >= 0:
            result = line[col-4].islower() and result
        if col + 4 < len(line):
            result = line[col + 4].islower() and result
 
        return result 


def count(words):
   for index, char in enumerate(words):
        if check_next(char, index, words): 
            result = char +  " " + str(index) 
            print(result) 

with open('python_challenger_str.txt', 'r') as myfile:
    word = myfile.read().replace('\n', '') 
    count(word)


    print("\n\n")
    print(len(word))
    print("\n\n")

    print(word[101066:101077])
    count("ilLKSndielkxdvnfLIucfHITuTHI")
