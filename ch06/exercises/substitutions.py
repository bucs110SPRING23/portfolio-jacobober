import json

def main():
    text = open("news.txt", "r").read().lower()
    sub_fptr = open("subs.json", "r")
    subs = json.load(sub_fptr)
    print(subs, type(subs))

    #use one list to modify another list
    #which list should you loop through

    for k, v in sub.items():
        text = text.replace(k,v)

    fptr = open("betternews.txt")
    fptr.write(text)
    fptr.close()

main()




# file_pointer = open("news.txt", "w")
# file_pointer = open("subs,json", "w")
# news = file_pointer.read('news.txt')
