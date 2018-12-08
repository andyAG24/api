from urllib.parse import urlencode, urljoin
import requests

APP_ID = 6775368
AUTH_URL = 'https://oauth.vk.com/authorize?'

token = '635dee2f384f1c2b941bec75faca54854f80814748f837978cdab1b6f7d36e5656d030fbdd3cc2c549294'
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'response_type': 'token',
    'scope': 'status, friends',
    'v': '5.92' 
}

params = {
    'access_token': token,
    'v': '5.92' 
}

# print(AUTH_URL + (urlencode(auth_data)))

# response = requests.get('https://api.vk.com/method/status.get', params)
# print(response.json())

# params['text'] = ''
# response = requests.get('https://api.vk.com/method/status.set', params)
# print(response.json())

# def get_status(self):
#         params = {
#             'access_token': token,
#             'v': '5.92'
#         }
#         response = requests.get('https://api.vk.com/method/status.get', params)
#         return response.json()

#     def set_status(self, text):
#         params = {
#             'access_token': token,
#             'v': '5.92',
#             'text': text
#         }
#         response = requests.get('https://api.vk.com/method/status.set', params)
#         return response.json()

class User:
    def __init__(self, token):
        self.token = token

    def getFriendsOnlineList(self):
        params = {
            'access_token': token,
            'v': '5.92'
        }
        response = requests.get('https://api.vk.com/method/friends.getOnline', params)
        return response.json()

    def getMutualFriends(self, target_uid): #поиск общих друзей
        params = {    
            'access_token': token,
            'target_uid': target_uid,
            'v': '5.92'
        }
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return response.json()

if __name__ == "__main__":
    me = User(token)
    target_uid = '138151317'
    mutual_friends_list = me.getMutualFriends(target_uid)
    # print(type(mutual_friends_list))

    line = input('Введите строку: ')
    line = line.split(' ')
    print(line)

    if line[1] == '&':
        mutual_friends_list = me.getMutualFriends(target_uid)
        i = 0
        while i < len(mutual_friends_list['response']):
            print('https://vk.com/id' + str(mutual_friends_list['response'][i]))
            i += 1
        print(me)