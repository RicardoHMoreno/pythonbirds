''' Exercicio: 
    Objetivo eh elucidar o conceito de composiçao e treinar o que foi aprendido ate o momento.
    Criar uma classe Carro que tem como atributos as classes Motor e Direcao.
    Motor eh reponsavel por controlar a velocidade do carro e tem como atributos de dados:
    1 velocidade [inincial = 0]
    2 metodo acelear (incrementa velocidade em uma unidade qdo executado)
    2 metodo reduzir (decrementa velocidade em duas unidade qdo executado) [velocidade minima = 0]

    Direcao eh reposavel por mudar a direcao do carro e tem como atributos de dados:
    1 direcao [inicial = Norte, Sul, Leste, Oeste] 
    2 metodo girar a direita
    3 metodo girar a esquerda

    Carro eh responsavel por informar a velocidade e direcao do carro e tem como atributos de dados:
    1 metodo calular velocidade
    2 metodo acelerar
    3 metodo reduzir
    4 medodo girar a direita
    5 metodo girar a esquerda
    6 metodo calcular direcao
    '''
class Motor():
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self, step=1):
        self.velocidade += step
        return self.velocidade
    
    def reduzir(self, step=2):
        if self.velocidade > step:
            self.velocidade -= step
        else:
            self.velocidade = 0
        return self.velocidade    

class Direcao():
    direcoes = ['Norte','Lest','Sul','Oest']
    direcao_atual = direcoes[0]

    def girar_a_direita(self):
        if Direcao.direcao_atual == Direcao.direcoes[-1]:
            Direcao.direcao_atual = Direcao.direcoes[0]
        else:
            Direcao.direcao_atual = Direcao.direcoes[Direcao.direcoes.index(Direcao.direcao_atual)+1]
        return Direcao.direcao_atual    
    
    def girar_a_esquerda(self):
        if Direcao.direcao_atual == Direcao.direcoes[0]:
            Direcao.direcao_atual = Direcao.direcoes[-1]
        else:
            Direcao.direcao_atual = Direcao.direcoes[Direcao.direcoes.index(Direcao.direcao_atual)-1]
        return Direcao.direcao_atual

class Carro():
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def status_do_carro(self):
        print(f'Direcao atual do carro: {self.direcao.direcao_atual} Velocidade atual do carro: {self.motor.velocidade}')
    
    def virar_a_direita(self):
        self.direcao.girar_a_direita()
        print('\nO carro virou a direita')
    
    def virar_a_esquerda(self):
        self.direcao.girar_a_esquerda() 
        print('\nO carro virou a esquerda')  
    
    def acelerar(self, step=1):
        delta_speed = self.motor.velocidade
        self.motor.acelerar(step)
        delta_speed = self.motor.velocidade - delta_speed
        print(f'\nO carro acelerou {delta_speed} unidade(s)')
    
    def reduzir(self, step=2):
        delta_speed = self.motor.velocidade
        self.motor.reduzir(step) 
        delta_speed = delta_speed - self.motor.velocidade 
        print(f'\nO carro reduziu {delta_speed} unidade(s)')        

if __name__ == '__main__':
    
    motor = Motor()
    direcao = Direcao()
    carro = Carro(motor, direcao)
    # print('Testes de direcao:')
    # for _ in range(4):
    #     print(direcao.girar_a_direita())
    # for _ in range(4):
    #     print(direcao.girar_a_esquerda())

    # print('Testes de velocidade:')        
    # for _ in range(4):
    #     print(motor.acelerar())  
    # for _ in range(4):
    #     print(motor.reduzir()) 

    print('Testes com o carro:')
    for _ in range(4):
        carro.virar_a_direita()
        carro.status_do_carro()  
    for _ in range(4):
        carro.virar_a_esquerda()
        carro.status_do_carro()          
    for _ in range(4):
        carro.acelerar()
        carro.status_do_carro() 
    for _ in range(4):
        carro.reduzir()
        carro.status_do_carro()         
