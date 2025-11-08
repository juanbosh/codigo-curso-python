import inspect
class ejemplo:
    def __init__(self):
        self.atributo = 42
    def metodo(self):       
        return "Hola Mundo"

print(inspect.getmembers(ejemplo, predicate=inspect.isfunction)) 
miejemplo = ejemplo()
print(miejemplo.metodo())   
print(miejemplo.atributo)
print(inspect.getmembers(miejemplo, predicate=inspect.ismethod))
