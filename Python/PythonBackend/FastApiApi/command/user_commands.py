
from PythonBackend.FastApiApi.models.user_models import User


users_list=[User(id=1,name="Tilapia",surname="Madona",age=12,game_id=1500),User(id=2,name="Rawr",surname="dinosaur",age=12,game_id=1501)]

def get_user_list()->list:
    return users_list