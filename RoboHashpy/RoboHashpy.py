import requests

class RoboHash:
    def __init__(self):
        self._get = requests.get
        self._base_url = "https://robohash.org"

    def get_im_hash(self, text: str, set = 1, size = "200x200"):
        img = f"{self._base_url}/{text}.png/?set=set{int(set)}/?size={size}"
        return img

    def get_grav_hash(self, email: str, gravatar = "no"):
        img = f"{self._base_url}/{email}?gravatar={gravatar}"
        return img
