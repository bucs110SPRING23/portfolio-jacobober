import requests

def main():
    print("Welcome to the Chuck Norris and Dad Jokes API program!")
    print("Please select the type of joke you would like to hear:")
    print("1. Chuck Norris joke")
    print("2. Dad joke")
    
    joke_type = input("Enter your choice (1 or 2): ")
    
    if joke_type == "1":
        chuck_norris_joke()
    elif joke_type == "2":
        dad_joke()
    else:
        print("Invalid choice. Please try again.")
        main()

def chuck_norris_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        data = response.json()
        print(data["value"])
    else:
        print("Failed to fetch joke. Please try again.")

def dad_joke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if response.status_code == 200:
        data = response.json()
        print(data["joke"])
    else:
        print("Failed to fetch joke. Please try again.")

if __name__ == "__main__":
    main()
