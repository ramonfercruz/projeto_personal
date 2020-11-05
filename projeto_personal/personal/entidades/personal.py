class Personal():
    def __init__(self, pessoa):
        self.__pessoa = pessoa

    @property
    def pessoa(self):
        return self.__pessoa

    @pessoa.setter
    def pessoa(self, pessoa):
        self.__pessoa = pessoa