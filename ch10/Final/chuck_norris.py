import requests

class ChuckNorrisJoke:
    '''
    A class that represents a Chuck Norris joke fetched from the Chuck Norris API.
    Stores the API url as an instance variable.
    '''
    def __init__(self):
        self.url = "https://api.chucknorris.io/jokes/random"
        '''
        Initializes the instance variable 'url' with the icanhazdadjoke API url.
        '''
    def get_joke(self):
        '''
        Fetches a random dad joke from the icanhazdadjoke API.
        return: (str) A dad joke.
        '''
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data["value"]
        else:
            return "Failed to fetch joke. Please try again."

    def __str__(self):
        '''
        Returns a string representation of the class instance.
        return: (str) A string representation of the DadJoke instance.
        '''
        return f"ChuckNorrisJoke(url='{self.url}')"