from main import User
from main import SuperUser

def test_UserClass():
    user1 = User('Paul McCartney', 'paul', '1234', 3)  
    user2 = User('George Harrison', 'george', '5678', 2)
    user3 = User('Richard Starkey', 'ringo', '8523', 3)  
    users = User.count - SuperUser.count
    
    assert user1 < user2 == False                                                                                                                                                                                                                                                                                # noqa: E712
    assert user1 == user3 == True                                                                                                                                           # noqa: E712
    assert users == 3
    assert user1.show_info() == 'Имя: Paul McCartney, Логин: paul'
    assert user1.name == 'Paul McCartney'

    user1.name = 'Ringo Starr'
    
    assert user1.name == 'Ringo Starr'

