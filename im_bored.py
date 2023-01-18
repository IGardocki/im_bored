import requests
from sys import argv

URL=('http://www.boredapi.com/api/activity?')

def get_thing_to_do():
    response = requests.get(URL)
    thing_to_do = response.json()
    print(f'Activity: {thing_to_do["activity"]}')
    print(f'Type: {thing_to_do["type"]}')
    print(f'Participants: {thing_to_do["participants"]}')
    print(f'Price: {thing_to_do["price"]}')
    print(f'Link: {thing_to_do["link"]}')
    print(f'Key: {thing_to_do["key"]}')
    print(f'Accessibility: {thing_to_do["accessibility"]}')

if __name__ == '__main__':
    get_thing_to_do()