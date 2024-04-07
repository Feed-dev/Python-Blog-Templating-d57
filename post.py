# post.py
import requests


class Post:
    API_URL = "https://api.npoint.io/c790b4d5cab58020d391"

    @classmethod
    def get_posts(cls):
        response = requests.get(cls.API_URL)
        posts = response.json() if response.status_code == 200 else []
        return posts

