#ver0.02a

print("Здравствуйте, у вас уже есть аккаунт или нет? (д/н)")

puss = input("---> ")

if puss == ("д"):
    name = input("Введите ваше имя ---> ")

    input("Введите ваш пароль ---> ")

    print("Добро пожаловать, " + name)

    # короч, надо придумать, как выглядел бы мессенджер в консоли, XD

    print("\nМеню: ")

    print("1) Написать сообщение")
    print("2) Входящие сообщения")
    print("3) Исходяцие сообщения")
    print("4) Спам")
    print("5) Настройки")
    print("6) superdupermenuforfreerobux")

    answ = input("---> ")

    if answ == ("1"):
        print("Кому хотите отправить?")
        vkusno = input("---> ")

        print("Введите тему сообщения (если нет темы, нажми Enter)")
        input("---> ")

        print("Введите текст сообщения")
        input("--->")

        print("Вы хотите отправить сообщение " + vkusno + "? (д/н)")
        kruto = input("--->")

        if kruto == ("д"):

            import time

            for percent in range(101):
                s = f"[{(percent // 10) * '■'}"
                s += f"{(10 - (percent // 10)) * '○'}] "
                s += f"{percent}"
                print(s, end="\r")
                time.sleep(0.01)

            print("\nГотово!")

        if kruto == ("н"):
            print("ну ладно")

    if answ == ("2"):
        print("У вас пока нет новый сообщений")

    if answ == ("3"):
        print("Вы пока ничего не отправляли")

    if answ == ("4"):
        print("У вас нет нового спама")

    if answ == ("5"):
        print("1) Удалить аккаунт и взорвать к хуям хохляндию")
        print("2) Поменять цвет терминала")

        accord = input("---> ")

        if accord == ("1"):
            import time

            for percent in range(101):
                s = f"[{(percent // 10) * '■'}"
                s += f"{(10 - (percent // 10)) * '○'}] "
                s += f"{percent}"
                print(s, end="\r")
                time.sleep(0.1)

            print("\nГАТОВА!")

        if accord == ("2"):
            print("зачем тебе его менять? мы же в 90-ых")

    # меня рома нахуй убьёт
    if answ == ("6"):
        print("how much u want ROBUX")
        robux = input("---> ")

        import time

        for percent in range(101):
            s = f"[{(percent // 10) * '■'}"
            s += f"{(10 - (percent // 10)) * '○'}] "
            s += f"{percent}"
            print(s, end="\r")
            time.sleep(0.1)

        print("\ndone ^_^. now you have " + robux + " robux in yr balance")

    # beluga = hecker

if puss == ("н"):
    print("ну тут короче пока регистрации нет)))")
