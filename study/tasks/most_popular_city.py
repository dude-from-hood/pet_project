if __name__ == '__main__':
    from collections import Counter
    most_popular_city = ["London, UK", "Paris, France", "Berlin, Germany", "Paris, France", "London, UK"]

    # Вариант №1
    #Counter({'New York, USA': 3, 'London, UK': 2, 'Paris, France': 1})
    # obj = Counter(most_popular_city)
    # #самый первый элемент - [('New York, USA', 3)]
    # pop = obj.most_common(1)[0][0]
    # print(pop.split(",")[0])

    # Вариант №2
    set_cities = set(most_popular_city)
    dict_cities = dict()

    for item in set_cities:
        dict_cities[item] = 0

    for item in most_popular_city:
        if item in dict_cities.keys():
            dict_cities[item] += 1

    #для сортировки по убыванию по кол-ву упоминаний ставим -x[1]
    sort_ = sorted(dict_cities.items(), key=lambda x: (-x[1], x[0]))
    most_popular = str(sort_[0][0])
    print(most_popular.split(',')[0])


