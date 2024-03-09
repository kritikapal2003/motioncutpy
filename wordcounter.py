#defining a function to count no. of words in given text
def count_words(text):
    words=text.split()
    return len(words)
#defining function to take input from user and display output
def main():
    text=input("enter your phrase").strip()
    if not text:
        print("Oops,the input is empty. kindly enter some text")
    else:
        word_count= count_words(text)
        print(f"No. of words in the above phrase :{word_count}")
if __name__=="__main__":
        main()
 
