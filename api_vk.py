from urllib.parse import urlencode, urljoin
import requests

APP_ID = 6775368
AUTH_URL = 'https://oauth.vk.com/authorize?'

token = 'af5f312d6b2e1c74163cca2d2ce6f1e71390d32fcced6463c1f5b2a1d6fa712771cbc0a3d135ccf89cfc8'

service_token = 'fc722e7afc722e7afc722e7acbfc154c32ffc72fc722e7aa07870048263346b0c441e79'

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

class User:
    def __init__(self, token):
        self.token = token

    def getMutualFriends(self, target_uid):
        params = {    
            'access_token': token,
            'target_uid': target_uid,
            'v': '5.92'
        }
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return response.json()

    def getId(self, user_name):
        params = {
            'access_token': service_token,
            'user_ids': user_name,
            'v': '5.92'
        }
        response = requests.get('https://api.vk.com/method/users.get', params)
        return response.json()

    def friendsId(self, service_token, user_id):
        params = {
            'access_token': service_token,
            'user_id': user_id,
            'v': '5.92'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()

    def __and__(self, user1, user2):
        user1_info = self.getId(user1)
        user1_id = user1_info['response'][0]['id']
        user1_friends = self.friendsId(service_token, user1_id)['response']['items']

        user2_info = self.getId(user2)
        user2_id = user2_info['response'][0]['id']
        user2_friends = self.friendsId(service_token, user2_id)['response']['items']

        mutual_friends_list = []
        for i in user1_friends:
            for k in user2_friends:
                if i == k:
                    mutual_friends_list.append(i)
                    break
        
        return mutual_friends_list
        
if __name__ == "__main__":
    print(' \n')

    me = User(token)
    target_uid = '5587993'
    mutual_friends_list = me.getMutualFriends(target_uid)
    print('Общие друзья через API:', me.getMutualFriends(target_uid)['response'])  # Получение списка общих друзей с помощью api vk

    line_list = input('\nВведите пользователей: ').split(' ')

    if line_list[1] == '&':
        user1_nickname = line_list[0]
        user2_nickname = line_list[2]

        user1 = User(token)
        print('\nОбщие друзья:', user1.__and__(user1_nickname, user2_nickname))
    else:
        print('\nНеправильный ввод')

    User = '\nhttps://vk.com/id{}\n'.format(str(user1.getId(user1_nickname)['response'][0]['id']))
    print(User)