from collections import deque

# Создаём граф друзей
graph = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy", "tom"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "tom": [],
    "thom": [],
    "jonny": []
}


# Функция проверки продавца манго
def person_is_seller(person):
    # Например, продавец манго - тот, у кого имя заканчивается на 'm'
    return person[-1] == 'm'


# Функция поиска (ваш код)
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


# Запускаем поиск от "you"
search("you")
