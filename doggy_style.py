v1 = float(input('Введите скорость движения первого друга в км/ч: '))
v2 = float(input('А теперь скорость движения второго друга: '))
v_dog = float(input('... и скорость бега собаки \n (по умолчанию она всегда быстрее друзей):\n'))
dir = input('Они идут навстречу друг другу? (yes/no) \n')
distance = float(input('Какое между ними расстояние в километрах? \n'))

v_summ = 0  # Сумма (или разница) скорости друзей
meet_quant = 0  # Количество пробегов собаки
s_meet = 0.005  # расстояние встречи
meet_flag = 0  # Момент встречи собаки с одним из друзей
t1 = t2 = 0  # Время пробега собаки

if dir == 'yes':  # Выясняем направление движения
    v_summ = (v1 + v2)
elif dir == 'no':
    v_summ = (v1 - v2) if (v1 > v2) else (v2 - v1)


def dog_run(v_summ):
    global distance, meet_flag, meet_quant
    while distance > s_meet:
        if meet_flag == 0:
            t1 = distance / (v1 + v_dog)
            distance = distance - v_summ * t1
            meet_flag = 1
            meet_quant += 1
        if meet_flag == 1:
            t2 = distance / (v2 + v_dog)
            distance = distance - v_summ * t2
            meet_flag = 0
            meet_quant += 1
    print('Собака пробежит между друзьями ', meet_quant, ' раз, \nпока между ними не будет 0,5 м.')


dog_run(v_summ)  # main
