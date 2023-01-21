from person import Person, Action
human = Person(name='Тарас', money=0, mood=100, health=100)

while True:
    print(human)
    go_to_park = Action(name='сходить в парк', money=0, mood=+5, health=+3)
    human.do(go_to_park)

    print(human)
