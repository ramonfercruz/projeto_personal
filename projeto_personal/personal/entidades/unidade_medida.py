class UnidadeMedida():
    def __init__(self, unidade_medida, sigla_unidade_medida):
        self.__unidade_medida = unidade_medida
        self.__sigla_unidade_medida = sigla_unidade_medida

    @property
    def unidade_medida(self):
        return self.__unidade_medida

    @unidade_medida.setter
    def unidade_medida(self, unidade_medida):
        self.__unidade_medida = unidade_medida

    @property
    def sigla_unidade_medida(self):
        return self.__sigla_unidade_medida

    @sigla_unidade_medida.setter
    def sigla_unidade_medida(self, sigla_unidade_medida):
        self.__sigla_unidade_medida = sigla_unidade_medida


