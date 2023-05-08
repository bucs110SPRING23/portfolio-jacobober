import requests

class DadJoke:
    '''
    A class that represents a dad joke fetched from the icanhazdadjoke API.
    Stores the API url as an instance variable.
    '''
    def __init__(self):
        '''
        Initializes the instance variable 'url' with the icanhazdadjoke API url.
        '''
        self.url = "https://icanhazdadjoke.com/"

    def get_joke(self):
        '''
        Fetches a random dad joke from the icanhazdadjoke API.
        return: (str) A dad joke.
        '''
        headers = {"Accept": "application/json", "User-Agent": "Python Joke Bot"}
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data["joke"]
        else:
            return "Failed to fetch joke. Please try again."

    def __str__(self):
        '''
        Returns a string representation of the class instance.
        return: (str) A string representation of the DadJoke instance.
        '''
        return f"DadJoke(url='{self.url}')"