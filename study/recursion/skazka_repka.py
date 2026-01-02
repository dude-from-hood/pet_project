def vitashit_repku(weight=None, level=0):
    if weight is None:
        weight = 200

    if weight == 0:
        return
    else:
        #print(level, weight)
        vitashit_repku(weight=weight - 50, level=level+1) # СНАЧАЛА уходим глубже
        print(level, weight)    # ПОТОМ печатаем (при возврате!)

vitashit_repku(300)