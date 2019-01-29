'''
Создайте класс Figure. У каждой фигуры есть имя, также можно найти площадь и периметр фигуры. 
Создайте классы Triangle, Circle, Rectangle производные от Figure. 
У класса Triangle есть 3 стороны: a, b, c; у Circle - радиус r; у Rectangle - стороны a и b. 
Переопределите методы нахождения площади и периметра для каждой фигуры (Triangle, Circle, Rectangle). 
Также для объектов классов должны работать операторы сравнения: ==, >, < <=, >=. 
Будем считать, что фигуры равны, если они имеют одинаковую площадь. 
Строковое представление объекта должно возвращать тип фигуры и её имя.
Дополнительная функциональность приветствуется.
'''

class Figure:
    
    def info(self):
        print("класс Фигура")
           
class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tr_sq(self):
        s = 0.5 * (self.a + self.b + self.c)
        return s

    def tr_pr(self):
        p = self.a + self.b + self.c
        return p

    def tr_info(self):
        print('Фигура: Треугольник')
        print('Периметр равен:', self.tr_pr())
        print('Площадь равна:', self.tr_sq())
       
class Circle(Figure):
    
    def __init__(self, r):
        self.r = r

    def cr_sq(self):
        s = 3.14 * self.r ** 2
        return s

    def cr_pr(self):
        p = 2 * 3.14 * self.r
        return p

    def cr_info(self):
        print('Фигура: Круг')
        print('Периметр равен:', self.cr_pr())
        print('Площадь равна:', self.cr_sq())  

class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rt_sq(self):
        s = self.a * self.b
        return s

    def rt_pr(self):
        p = 2 * (self.a + self.b)
        return p

    def rt_info(self):
        print('Фигура: Прямоуголник')
        print('Периметр равен:', self.rt_pr())
        print('Площадь равна:', self.rt_sq())
        
        
