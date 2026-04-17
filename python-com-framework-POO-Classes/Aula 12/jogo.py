import random

class Jogador:
    def escolher(self):
        escolha= input('Escolha Papel, Tesoura  ou Pedra: ')
        return escolha.lower()

class Maquina:
    def escolher_maqui(self):
        escolha = ['pedra','papel', 'tesoura']
        return random.choice(escolha)
    
class Jogo:
    def verificar_vitoria(self, jogador, maquina):
        if jogador == maquina:
            return 'Empate'
        elif jogador == 'pedra' and maquina == 'tesoura':
            return 'Jogador Ganhou'
        elif jogador == 'papel' and maquina == 'pedra':
            return 'Jogador Ganhou'
        elif jogador == 'tesoura' and maquina == 'papel':
            return 'Jogador Ganhou'
        else:
            return 'Maquina Venceu...'
        
    def jogar(self):
        jogador = Jogador()
        maquina = Maquina()

        escolher_jogador = jogador.escolher()
        escolher_maquina = maquina.escolher_maqui()

        print('O jogador escolheu ',escolher_jogador)
        print('O maquina escolheu ',escolher_maquina)

        resultado = self.verificar_vitoria(escolher_jogador,escolher_maquina)
        print('Vitoria de -->', resultado)

jogo = Jogo()
jogo.jogar()
