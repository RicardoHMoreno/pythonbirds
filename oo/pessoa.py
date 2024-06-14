class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):# *filhos: *argv representa um paramentro que pode receber 1 ou mais valores
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        print('\nOla, tudo bem com vc?')

if __name__ == '__main__':
    cafu = Pessoa(nome='Cafu', idade=32)
    bruno = Pessoa(nome='Bruno', idade=20)
    dunga = Pessoa(cafu, bruno, nome='Dunga', idade=44)
    
    cafu.cumprimentar()
    print(f'Eu me chamo {cafu.nome} e tenho {cafu.idade} anos')
    for filho in cafu.filhos:
        print(f'{filho.nome} eh meu filho') 
    
    bruno.cumprimentar()
    print(f'Eu me chamo {bruno.nome} e tenho {bruno.idade} anos')
    for filho in bruno.filhos:
        print(f'{filho.nome} eh meu filho') 
    
    dunga.cumprimentar()
    print(f'Eu me chamo {dunga.nome} e tenho {dunga.idade} anos')
    for filho in dunga.filhos:
        print(f'{filho.nome} eh meu filho') 

    pessoas = [cafu, bruno, dunga]
    for pessoa in pessoas:
        print(pessoa.__dict__)# Mostra os atributos atuais das pessoas

    del dunga.filhos# modifica dinamicamente o atributo filho de dunga, deletando ele. Isso so afteta dunga.
    dunga.sobrenome = 'dos Santos' # Cria dinamicamente o atributo sobrenome para dunga.  

    for pessoa in pessoas:
        print(pessoa.__dict__)# Mostra os atributos novamente apos as modificaçoes dinamicas   
