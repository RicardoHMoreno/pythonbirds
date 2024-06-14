class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print('Ola, tudo bem com vc?')

if __name__ == '__main__':
    p = Pessoa('Cafu', 32)
    p.cumprimentar()
    print(f'Eu me chamo {p.nome} e tenho {p.idade} anos')