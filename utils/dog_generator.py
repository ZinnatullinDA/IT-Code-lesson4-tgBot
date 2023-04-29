import requests

class Dog:

    def __int__(self):
        response: dict
        pic_url: str

    def get_any_dog(self) -> str:
        response = requests.get("https://random.dog/woof.json").json()
        pic_url = response['url']
        return pic_url

    def get_pic_dog(self) -> str:
        response = requests.get('https://random.dog/woof?include=jpg,jpeg,png,JPEG').text
        pic_url = 'https://random.dog/' + response
        return pic_url

    def get_gif_dog(self) -> str:
        response = requests.get('https://random.dog/woof?include=gif').text
        pic_url = 'https://random.dog/' + response
        return pic_url

    def get_vid_dog(self) -> str:
        response = requests.get('https://random.dog/woof?include=mp4,gif').text
        pic_url = 'https://random.dog/' + response
        print(pic_url)
        return pic_url