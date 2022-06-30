# class Transport:
#     def move_to(self):
#         raise NotImplementedError

class Transport:
    def move_to(self):
        return 'I can move'

class Radio:
    def listen_radio(self):
        return 'I can listen to the radio'

    def move_to(self):
        return 'I can MOVE'


# class Car(Transport, Radio):
#     pass

class Car(Transport,Radio):
    def move_to(self):  # переопределение метода
        return 'I can drive'


class Plain(Transport):
    def fly_to(self):
        return 'I can fly'


porsche = Car()
print(porsche.move_to())
print(porsche.listen_radio())

boeing = Plain()
print(boeing.move_to())
print(boeing.fly_to())