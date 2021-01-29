from core.settings import BASE_DIR
from accounts.models import  Account, User
import os


def get_details(uuid_user):
    try:
        Account.objects.get(id=uuid_user)
    except Exception as err:
        print(err)

        
def create_workspace(uuid_user):
    try:
        os.system(f'mkdir {BASE_DIR}/seln/data/{uuid_user}')
        return str(uuid_user)
    except Exception as err:
        print(err)
