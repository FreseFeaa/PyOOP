class User:
    count = 0  # Атрибут класса для хранения количества созданных экземпляров
    
    def __init__(self, name, login, password, grade):
        self._name = name  # Устанавливаем имя 
        self._login = login  # Устанавливаем логин 
        self._password = password  # Устанавливаем пароль 
        self._grade = grade  # Устанавливаем оценку 
        User.count += 1  # Увеличиваем счетчик созданных экземпляров класса
    @property
    def name(self):
        return self._name  # Возвращаем имя пользователя
    
    @name.setter
    def name(self, value):
        self._name = value  # Устанавливаем новое имя пользователя
    
    @property
    def login(self):
        return self._login  # Возвращаем логин пользователя
    
    @property
    def password(self): 
        return "********"  # Возвращаем звездочки вместо пароля
    
    @password.setter
    def password(self, value):
        self._password = value  # Устанавливаем новый пароль пользователя
    
    @login.setter
    def login(self, value: str):
        print("Невозможно изменить логин!")

    @property
    def grade(self):
        return "Неизвестное свойство grade"

    @grade.setter
    def grade(self, _):
        print("Неизвестное свойство grade")

    def show_info(self):
        print(f"Имя: {self._name}, Логин: {self._login}")  # Выводим информацию о пользователе

    def __lt__(self, other):
        return self._grade < other._grade  # Переопределяем оператор < для сравнения пользователей по оценке

    def __eq__(self, other):
        return self._grade == other._grade  # Переопределяем оператор == для сравнения пользователей по оценке

class SuperUser(User):
    count = 0  # Атрибут класса для хранения количества созданных экземпляров
    
    def __init__(self, name, login, password, role, grade):
        super().__init__(name, login, password, grade)  # Вызываем конструктор родительского класса
        self._role = role  # Устанавливаем роль супер-пользователя
        SuperUser.count += 1  # Увеличиваем счетчик созданных экземпляров класса
    
    @property
    def role(self):
        return self._role  # Возвращаем роль супер-пользователя
    
    @role.setter
    def role(self, value):
        self._role = value  # Устанавливаем новую роль супер-пользователя
    
    def show_info(self):
        print(f"Имя: {self._name}, Логин: {self._login}, Роль: {self._role}")  # Выводим информацию о супер-пользователе


# Пример использования
def longStick():
    print ('_____________________________________________________________________________________')
user1 = User('Paul McCartney', 'paul', '1234', 3)  # Создаем обычного пользователя
user2 = User('George Harrison', 'george', '5678', 2)  # Создаем обычного пользователя
user3 = User('Richard Starkey', 'ringo', '8523', 3)  # Создаем обычного пользователя
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)  # Создаем супер-пользователя
longStick()
print('Информация о пользователе user1:')
user1.show_info()  # Выводим информацию о пользователе
print('Информация о супер-пользователе admin:')
admin.show_info()  # Выводим информацию о супер-пользователе


longStick()
users = User.count - SuperUser.count  # Получаем количество обычных пользователей
admins = SuperUser.count  # Получаем количество супер-пользователей
print(f'Всего обычных пользователей: {users}')  # Выводим количество обычных пользователей
print(f'Всего супер-пользователей: {admins}')  # Выводим количество супер-пользователей
longStick()

print(f'user1(3) < user2(2) = {user1 < user2}')  # Сравниваем пользователей по оценке
print(f'admin(5) > user3(3) = {admin > user3}')  # Сравниваем супер-пользователя с пользователем по оценке
print(f'user1(3) == user3(3) = {user1 == user3}')  # Сравниваем пользователей по оценке
longStick()
user3.name = 'Ringo Starr'  # Изменяем имя пользователя
user1.password = 'Pa$$w0rd'  # Изменяем пароль пользователя

print(f'Новое имя user3: {user3.name}')  # Выводим новое имя пользователя
print(f'Новый пароль user2: {user2.password}')  # Выводим пароль пользователя
print(f'Логин user2: {user2.login}')  # Выводим логин пользователя

longStick()

user2.login = 'geo'
print(user1.grade)
admin.grade = 10