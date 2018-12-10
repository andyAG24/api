from urllib.parse import urlencode, urljoin
import requests

APP_ID = 6775368
AUTH_URL = 'https://oauth.vk.com/authorize?'

token = 'e8b7abdcb50085369c92d4211e1b401b9b16b098c8e75ad53b9b22ffcfb930931568188a6705caf018e94'

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

class User2:
    def __init__(self, service_token):
        self.service_token = service_token

    def friendsId(self, user_id):
        params = {
            'access_token': service_token,
            'user_id': user_id,
            'v': '5.92'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()

    def getId(self, user_name):
        params = {
            'access_token': service_token,
            'user_ids': user_name,
            'v': '5.92'
        }
        response = requests.get('https://api.vk.com/method/users.get', params)
        return response.json()


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

        user1 = User2(service_token)
        user2 = User2(service_token)

        user1_info = user1.getId(user1_nickname) 
        user1_id = user1_info['response'][0]['id']
        user1_friends = user1.friendsId(user1_id)
        user1_friends = user1_friends['response']['items']

        user2_info = user2.getId(user2_nickname)
        user2_id = user2_info['response'][0]['id']
        user2_friends = user2.friendsId(user2_id)
        user2_friends = user2_friends['response']['items']

        mutual_friends_list = []

        for i in user1_friends:
            for k in user2_friends:
                if i == k:
                    mutual_friends_list.append(i)
                    break
        print('\nОбщих друзей:', mutual_friends_list)
    else:
        print('\nНеправильный ввод')

    User = '\nhttps://vk.com/id{}\n'.format(str(user1.getId(user1_nickname)['response'][0]['id']))
    print(User)

    
    