class Tratador():
    def __init__(self, separador_elemento: str = '|') -> None:
        """
            Insatancia um novo Tratador

            Keyword arguments: \n
            **separador_elemento** -> caracter unico que separa blocos de elementos da string (Padrão '|')
        """
        self.separador_elemento = separador_elemento

    def remove_conchetes(self, str: str) -> str:
        return str.split('(')[0]

    def count_abilities(self, str: str) -> int:
        count = str.count(self.separador_elemento)
        return count

    def tratar_repeticao(self, str: str) -> str:
        palavras = str.split(self.separador_elemento)[0:-1]
        tratado = []
        while len(palavras) > 0:
            temp = palavras.pop()
            if temp not in tratado: 
                tratado.append(temp)

        resp = ""
        for palavra in tratado:
            resp += palavra + self.separador_elemento
        return resp