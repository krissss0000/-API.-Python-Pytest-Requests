import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '72b5b15c5dab7f72ee6babde0f981f14'
HEADER = {'Contant-Type' : 'application/json', "trainer_token": TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo": 'https://storage.yandexcloud.net/qastudio/pokemon_battle/pokemons/296.png'
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)


