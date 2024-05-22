from main import User
from main import SuperUser


def test_UserClass():

    user1 = User('Paul McCartney', 'paul', '1234', 3)  
    user2 = User('George Harrison', 'george', '5678', 2)
    user3 = User('Richard Starkey', 'ringo', '8523', 3)  
    admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)  
    admins = SuperUser.count          

    assert admin > user1 == True                                                                                                                                           # noqa: E712        
    assert admin > user2 == True                                                                                                                                        # noqa: E712         
    assert admin > user3 == True                                                                                                                                      # noqa: E712                                                                                                                                      
    assert admins == 1
    assert admin.show_info() == 'Имя: John Lennon, Логин: john, Роль: admin'