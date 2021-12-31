'''
4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри'''

class Figure(object):
    
    def __init__(self, color):
        self.color = color
    
class Oval(Figure):
        
    def __init__(self, far_distance, close_distance, color='white'):
        self.far_distance = far_distance
        self.close_distance = close_distance
        super(Oval, self).__init__(color=color)
            
class Square(Figure):
        
    def __init__(self, side, color='white'):
        self.side = side
        super(Square, self).__init__(color=color)
            
sq_1 = Square(4)
print(sq_1.color, sq_1.side)

ov_1 = Oval(5, 2, 'black')

print(ov_1.far_distance, ov_1.close_distance, ov_1.color)
