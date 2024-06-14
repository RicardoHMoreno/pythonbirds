class Pessoa:
    olhos = 2 # Atributo de classe. 
    #Atributo de classe eh comum a todas as instancias, mas nao eh mostrado por __dict__ por nao ser um atributo de instancia.
    #Ao acessar o atributo olhos em uma instancia, como ele nao exite o python procura nos atributos de classe.
    #Caso nao ache nos tributos de classe, um erro sera gerado.
    #Todas instancias de Pessoa terao 2 olhos por default na sua criaçao e como eh comum, usa menos memoria.

    def __init__(self, *filhos, nome=None, idade=None):# *filhos: *argv representa um paramentro que pode receber 1 ou mais valores
        self.nome = nome # atributo de instancia( consome memoria para cada nova instancia de pessoa)
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

    for pessoa in pessoas:
        print(pessoa.olhos, id(pessoa.olhos), pessoa.nome, id(pessoa.nome))# Mostra os atributos olhos de todas as pessoas e seu id comprovando que sao iguais
        
