from datetime import datetime
class Atleta:
    def __init__(self, id, nome, idade,posicao):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__posicao = posicao

    # Métodos de acesso
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_posicao(self):
        return self.__posicao

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_posicao(self,posicao):
        self.__posicao = posicao

    def __str__(self):
        return f"Atleta[ID: {self.__id}, Nome: {self.__nome}, Idade: {self.__idade} , Posição: {self.__posicao}]"

class Atletas:
    __lista_atletas=[]

    def inserir(self, atleta):

        id = 0
        for a in self.__lista_atletas:
            id = a.get_id()
        atleta.set_id(id + 1)
        self.__lista_atletas.append(atleta)


    def atualizar(self, novo_atleta):

        for atleta in self.__lista_atletas:
            if atleta.get_id()==novo_atleta.get_id():
                atleta.set_nome(novo_atleta.get_nome())
                atleta.set_idade(novo_atleta.get_idade())
                atleta.set_posicao(novo_atleta.get_posicao())
                break

    def excluir(self, novo_atleta):

        for atleta in self.__lista_atletas:
            if atleta.get_id()==novo_atleta.get_id():
                self.__lista_atletas.remove(atleta)
                break

    def listar(self):
        return self.__lista_atletas


class Jogo:
    def __init__(self, id, data, local):
        self.__id = id
        self.__data = data
        self.__local = local

    # Métodos de acesso
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_local(self):
        return self.__local

    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_local(self, local):
        self.__local = local

    def __str__(self):
        return f"Jogo[ID: {self.__id}, Data: {self.__data}, Local: {self.__local}]"
    



class Jogos:
    __lista_jogos=[]

    def inserir(self, jogo):

        while True:
            try:
                datetime.strptime(jogo.get_data(), "%d/%m/%Y")
                break
            except ValueError:
                print("Formato inválido. Tente novamente.")
            jogo.set_data(input('Digite a data do Jogo (formato DD/MM/AAAA): '))

        id = 0
        for j in self.__lista_jogos:
            id = j.get_id()
        jogo.set_id(id + 1)
        self.__lista_jogos.append(jogo)


    def atualizar(self, novo_jogo):

        for jogo in self.__lista_jogos:
            if jogo.get_id()==novo_jogo.get_id():
                jogo.set_data(novo_jogo.get_data())
                jogo.set_local(novo_jogo.get_local())
                break

    def excluir(self, novo_jogo):

        for jogo in self.__lista_jogos:
            if jogo.get_id()==novo_jogo.get_id():
                self.__lista_jogos.remove(jogo)
                break

    def listar(self):
        return self.__lista_jogos



class Gol:
    def __init__(self, id, minuto, id_atleta, id_jogo):
        self.__id = id
        self.__minuto = minuto
        self.__id_atleta = id_atleta
        self.__id_jogo = id_jogo

    # Métodos de acesso
    def get_id(self):
        return self.__id

    def get_minuto(self):
        return self.__minuto

    def get_id_atleta(self):
        return self.__id_atleta
    
    def get_id_jogo(self):
        return self.__id_jogo

    def set_id(self, id):
        self.__id = id

    def set_minuto(self, minuto):
        self.__minuto = minuto

    def set_id_atleta(self, id_atleta):
        self.__id_atleta = id_atleta

    def set_id_jogo(self, id_jogo):
        self.__id_jogo = id_jogo

    def __str__(self):
        return f"Gol[ID: {self.__id}, Minuto: {self.__minuto}, AtletaID: {self.__id_atleta}, JogoID: {self.__id_jogo}]"



class Gols:
    __lista_gols=[]
    
  
    def inserir(self, gol):
        
        atleta_encontrado = False

        while True:
            for atleta in Atletas.listar():
                
                if atleta.get_id() == gol.get_id_atleta():
                  atleta_encontrado = True
                  break

            if atleta_encontrado == True:
                print('Atleta inserido com sucesso')
                break
            

            
            print(f"Erro: Atleta com ID {gol.get_id_atleta()} não encontrado.")
            gol.set_id_atleta(int(input("Digite novamente o ID do atleta: ")))


        jogo_encontrado=False
        while True:
            for jogo in Jogos.listar():
                if jogo.get_id() == gol.get_id_jogo():
                    jogo_encontrado=True
                    break

            if jogo_encontrado==True:
                print('Jogo inserido com sucesso')
                break
            
            print(f"Erro: Jogo com ID {gol.get_id_jogo()} não encontrado.")
            gol.set_id_jogo(int(input("Digite novamente o ID do jogo: ")))

        id = 0
        for g in self.__lista_gols:
            id = g.get_id()
        gol.set_id(id + 1)

        self.__lista_gols.append(gol)
        print("Gol inserido com sucesso!")



    def atualizar(self, novo_gol):


        atleta_encontrado = False

        while True:
            for atleta in Atletas.listar():
                
                if atleta.get_id() == novo_gol.get_id_atleta():
                  atleta_encontrado = True
                  break

            if atleta_encontrado == True:
                print('Atleta inserido com sucesso')
                break
            

            
            print(f"Erro: Atleta com ID {novo_gol.get_id_atleta()} não encontrado.")
            novo_gol.set_id_atleta(int(input("Digite novamente o ID do atleta: ")))


        jogo_encontrado=False
        while True:
            for jogo in Jogos.listar():
                if jogo.get_id() == novo_gol.get_id_jogo():
                    jogo_encontrado=True
                    break

            if jogo_encontrado==True:
                print('Jogo inserido com sucesso')
                break
            
            print(f"Erro: Jogo com ID {novo_gol.get_id_jogo()} não encontrado.")
            novo_gol.set_id_jogo(int(input("Digite novamente o ID do jogo: ")))







        for gol in self.__lista_gols:
            if gol.get_id()==novo_gol.get_id():
                gol.set_minuto(novo_gol.get_minuto())
                gol.set_id_atleta(novo_gol.get_id_atleta())
                gol.set_id_jogo(novo_gol.get_id_jogo())

                break

    def excluir(self, novo_gol):

        for gol in self.__lista_gols:
            if gol.get_id()==novo_gol.get_id():
                self.__lista_gols.remove(gol)
                break
    
    def listar(self):
        return self.__lista_gols

Atletas = Atletas()
Jogos = Jogos()
Gols = Gols()


class UI:
    @staticmethod
    def main():
        op = UI.menu_secundario()
        while op != 99:
            if op == 1:
                op = UI.menu_primario()
                while op != 99:
                    if op == 1:
                        UI.InserirAtleta()
                    elif op == 2:
                        UI.ListarAtleta()
                    elif op == 3:
                        UI.AtualizarAtleta()
                    elif op == 4:
                        UI.ExcluirAtleta()
                    op = UI.menu_primario()

            elif op == 2:
                op = UI.menu_primario()
                while op != 99:
                    if op == 1:
                        UI.InserirJogo()
                    elif op == 2:
                        UI.ListarJogo()
                    elif op == 3:
                        UI.AtualizarJogo()
                    elif op == 4:
                        UI.ExcluirJogo()
                    op = UI.menu_primario()

            elif op == 3:
                op = UI.menu_primario()
                while op != 99:
                    if op == 1:
                        UI.InserirGol()
                    elif op == 2:
                        UI.ListarGol()
                    elif op == 3:
                        UI.AtualizarGol()
                    elif op == 4:
                        UI.ExcluirGol()
                    op = UI.menu_primario()

            op = UI.menu_secundario()

    @staticmethod
    def menu_secundario():
        print('OPERAÇÕES')
        print('-------------------------------------------------------------------')
        print('Atleta: 1 , Jogo: 2 , Gol: 3 , 99 - Fechar programa')
        return int(input('Digite: '))

    @staticmethod
    def menu_primario():
        print('-------------------------------------------------------------------')
        print('1 - INSERIR , 2 LISTAR , 3 - ATUALIZAR , 4 EXCLUIR , 99 - VOLTAR')
        return int(input('Digite: '))


    
    def InserirAtleta():
        nome = input('Digite o nome do Atleta: ')
        idade = int(input('Digite sua idade: '))
        posicao= input('Digite a posição do Atleta: ')
        Atletas.inserir(Atleta(0, nome, idade,posicao))

    
    def ListarAtleta():
        for atleta in Atletas.listar():
            print(atleta)

    
    def AtualizarAtleta():
        UI.ListarAtleta()
        id = int(input('Digite o id que será alterado: '))
        nome = input('Digite o nome do Atleta: ')
        idade = int(input('Digite sua idade: '))
        posicao= input('Digite a posição do Atleta: ')
        Atletas.atualizar(Atleta(id, nome, idade,posicao))
        print('Atleta atualizado com sucesso')

    
    def ExcluirAtleta():
        UI.ListarAtleta()
        id = int(input('Qual Atleta será excluído: '))
        Atletas.excluir(Atleta(id, "", "",""))

    
    def InserirJogo():
        data = input('Digite a data do Jogo (formato DD/MM/AAAA): ')
        local = input('Digite o local: ')
        Jogos.inserir(Jogo(0, data, local))

    
    def ListarJogo():
        for jogo in Jogos.listar():
            print(jogo)

    
    def AtualizarJogo():
        UI.ListarJogo()
        id = int(input('Digite o id que será alterado: '))
        data = input('Digite a data do Jogo (formato DD/MM/AAAA): ')
        local = input('Digite o local: ')
        Jogos.atualizar(Jogo(id, data, local))
        print('Jogo atualizado com sucesso')

    
    def ExcluirJogo():
        UI.ListarJogo()
        id = int(input('Qual Jogo será excluído: '))
        Jogos.excluir(Jogo(id, "", ""))

    
    def InserirGol():
        minuto = input('Digite o minuto do Gol: ')
        id_atleta = int(input('Digite o id do Atleta: '))  # Convertendo para int
        id_jogo = int(input('Digite o id do Jogo: '))  # Convertendo para int
        Gols.inserir(Gol(0, minuto, id_atleta, id_jogo))


        
    def ListarGol():
        for gol in Gols.listar():
            print(gol)

    
    def AtualizarGol():
        UI.ListarGol()
        id = int(input('Digite o id que será alterado: '))
        minuto = input('Digite o minuto do Gol: ')
        id_atleta = int(input('Digite o id do Atleta: '))  # Convertendo para int
        id_jogo = int(input('Digite o id do Jogo: '))  # Convertendo para int
        Gols.atualizar(Gol(id, minuto, id_atleta, id_jogo))
        print('Gol atualizado com sucesso')

    
    def ExcluirGol():
        UI.ListarGol()
        id = int(input('Qual Gol será excluído: '))
        Gols.excluir(Gol(id, "", "", ""))

if __name__ == "__main__":
    UI.main()
