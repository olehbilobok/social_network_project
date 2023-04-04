import json
import os.path
import random
import requests

HOST = 'http://127.0.0.1:8000'


class FileManager:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        with open(self.file_path, 'r') as config_file:
            return json.load(config_file)


class FakeData:

    def __init__(self, data):
        self.data = data

    def user_data(self):
        first_name = ['Angelina', 'Chris', 'Robert', 'Valery', 'Jennifer', 'Betty', 'Morgan', 'Robbi', 'Natalie', 'Tom']
        last_name = ['Nicholson', 'De Niro', 'Brando', 'Washington', 'Hepburn', 'Streep', 'Jackson', 'Downey', 'Willis',
                     'Diesel']
        users = []
        while len(users) < self.data.get('number_of_users'):
            username = random.choice(first_name) + random.choice(last_name)
            if username not in [user_name.get('username') for user_name in users]:
                users.append(
                    {
                        'username': username,
                        'password': 'fake12345'
                    }
                )
        return users

    def post_data(self):
        titles = ['A Guide To...', 'No ONE Will Tell You..', 'How to', 'Infographic', 'Mistakes to avoid...',
                  'Question', 'Everything you should know about', 'Keyword...', 'Increase your...', 'The simple']
        description = ['description1', 'description2', 'description3', 'description4', 'description5', 'description6',
                       'description7', 'description8', 'description9', 'description10']

        posts = []
        while len(posts) < self.data.get('max_posts_per_user'):
            title = random.choice(titles)
            if title not in [title_.get('title') for title_ in posts]:
                posts.append(
                    {
                        'title': title,
                        'description': random.choice(description)
                    }
                )
        return posts


class APIActivity:

    def __init__(self, data):
        self.data = data

    def create_user(self, url):
        users = []
        for user in self.data.user_data():
            response = requests.post(url, user)
            if isinstance(response.json().get('username'), list):
                continue
            users.append(response.json())
        return users

    @staticmethod
    def get_access_token(url, user):
        response = requests.post(url, user)
        return response.json()

    def create_post(self, url, users):
        posts = []
        for user in users:
            token = self.get_access_token(HOST + '/api/token', {'username': user.get('username'),
                                                                'password': 'fake12345'})
            user.update({'access': token.get('access')})
            for post in self.data.post_data():

                body = {'user': user.get('id'),
                        'title': post.get('title'),
                        'description': post.get('description')
                        }
                response = requests.post(url=url, json=body, headers={"Authorization": f"Bearer {token.get('access')}"})
                posts.append(response.json())
        return posts

    @staticmethod
    def like_post(posts, users):
        for post in posts:
            for user in users:
                if post.get('user') == user.get('id'):

                    body = {
                        'post': post.get('id'),
                        'user': post.get('user')
                    }
                    requests.post(url=HOST + f"/api/post/{post.get('id')}/like", data=body, headers={
                        "Authorization": f"Bearer {user.get('access')}"
                    })


def main():
    file = FileManager(os.path.abspath('config.json'))
    config_data = file.read_data()
    fake_data = FakeData(config_data)
    api = APIActivity(fake_data)
    users = api.create_user(HOST + '/api/register')
    posts = api.create_post(HOST + '/api/post', users)
    api.like_post(posts, users)


if __name__ == '__main__':
    main()



