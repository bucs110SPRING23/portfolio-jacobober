import requests

from chuck_norris import ChuckNorrisJoke
from dad_joke import DadJoke

def main():
    print("Welcome to the Chuck Norris and Dad Jokes API program!")
    print("Please select the type of joke you would like to hear:")
    print("1. Chuck Norris joke")
    print("2. Dad joke")
    
    joke_type = input("Enter your choice (1 or 2): ")
    
    if joke_type == "1":
        joke = ChuckNorrisJoke().get_joke()
    elif joke_type == "2":
        joke = DadJoke().get_joke()
    else:
        print("Invalid choice. Please try again.")
        main()
    
    print(joke)

if __name__ == "__main__":
    main()