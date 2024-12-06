import pytest
from UserManager import UserManager

@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    user_manager.add_user("Amanda")
    assert "Amanda" in user_manager.users
    assert user_manager.add_user("Amanda") == "User already exists"

def test_remove_user(user_manager):
    user_manager.add_user("Pedro")
    user_manager.remove_user("Pedro")
    assert "Pedro" not in user_manager.users
    assert user_manager.remove_user("Pedro") == "não encontrado"

manager = UserManager()
manager.add_user("Amanda")
print(manager.users)  

manager = UserManager()
manager.add_user("Pedro")
#manager.remove_user("marcos")
print(manager.users) 