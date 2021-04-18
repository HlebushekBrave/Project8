def HanoiTower(n, from_, to_, additional):
    if n == 1:
        print("Переместите диск 1 со стержня", from_, "на стержень", to_)
        return
    HanoiTower(n - 1, from_, additional, to_)
    print("Переместите диск", n, "со стержня", from_, "на стержень", to_)
    HanoiTower(n - 1, additional, to_, from_)


n = int(input('Введите изначальное количество дисков в башне: '))
HanoiTower(n, 'A', 'B', 'C')
