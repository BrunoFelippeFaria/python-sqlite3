import sqlite3

class Main:
    def __init__(self):
        self.conect = sqlite3.connect("database.db")
        self.cursor = self.conect.cursor()
        self.interface()


    def interface(self):
        while True:
            print("==Banco de dados==")
            opcs = ("Mostrar dados", "Inserir dados")
            
            for i, opc in enumerate(opcs, 1):
                print(f"( {i} ) {opc}")
            
            while True:
                escolha = input("opção: ")
                if escolha == "1":
                    self.mostrar_dados()
                    break
                elif escolha == "2":
                    self.inserir_dados()
                    break
                else:
                    print("opção invalida, escolha novamente")
                    continue
            
            escolha = input("deseja continuar [S/N]")

            if not escolha.lower() == "s":
                break


    def mostrar_dados(self):
        self.cursor.execute("SELECT * FROM Pessoas;")
        usuarios = self.cursor.fetchall()
        for usuario in usuarios:
            print(usuario)
        
    
    def inserir_dados(self):
        nome = input("nome: ")
        sexo = input("sexo: ")[0].upper()
        idade = input("idade: ")
        self.cursor.execute(f'insert into Pessoas(nome, sexo, idade) values ("{nome}", "{sexo}", "{idade}");')
        self.conect.commit()

if __name__ == "__main__":
    Main()