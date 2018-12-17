from urllib.parse import urlencode, urljoin
import requests

APP_ID = 6775368
AUTH_URL = 'https://oauth.vk.com/authorize?'

token = '66abd0d86143f964120b946a4c3e879fc20e5c36b7818cd812185f7d0cd9dfba867f6cb1f2afe066a0dec'

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

print(AUTH_URL + (urlencode(auth_data)))

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

    def __and__(self, other):
        self_info = self.getId(user1_nickname)
        self_id = self_info['response'][0]['id']
        self_friends = self.friendsId(service_token, self_id)['response']['items']

        other = User(token)
        other_info = other.getId(user2_nickname)
        other_id = other_info['response'][0]['id']
        other_friends = self.friendsId(service_token, other_id)['response']['items']

        mutual_friends_list = []
        for i in self_friends:
            for k in other_friends:
                if i == k:
                    mutual_friends_list.append(i)
                    break
        
        return mutual_friends_list

    def __str__(self):
        return '\nhttps://vk.com/id' + str(user1.getId(user1_nickname)['response'][0]['id'])
        
        
if __name__ == "__main__":
    print(' \n')

    me = User(token)
    target_uid = '5587993'
    mutual_friends_list = me.getMutualFriends(target_uid)
    print('Общие друзья через API:', me.getMutualFriends(target_uid)['response'])  # Получение списка общих друзей с помощью api vk

    line_list = input('\nВведите пользователей через пробел: ').split(' ')

    if line_list[1] == '&':
        user1_nickname = line_list[0]
        user2_nickname = line_list[2]

        user1 = User(token)
        user2 = user2_nickname
        print('\nОбщие друзья:', user1 & user2)
    else:
        print('\nНеправильный ввод')

    print(user1)


