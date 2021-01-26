from core.settings import BASE_DIR
from accounts.models import  Account, User
import os


def get_details(uuid_user):
    try:
        Account.objects.get(id=uuid_user)
    except Exception as err:
        pass

def create_workspace(uuid_user):
    try:
        print()
        os.system(f'mkdir {BASE_DIR}/seln/data/{uuid_user}')
        return str(uuid_user)
    except Exception as err:
        print(err)
