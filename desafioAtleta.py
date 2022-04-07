class DesafioAtletas:
            
    def validarQuantidade():
        quantidade = int(input("Qual a quantidade de atletas: "))
        if quantidade > 0:
            return quantidade
        else:
            while quantidade <= 0:
                print("Quantidade menor ou igual a zero!")
                quantidade = int(input("Digite a quantidade de atleta: "))      
            return quantidade
    
    def validarSexo(self):
        self.sexo = input("Sexo do atleta: ")
        if (self.sexo =='M') or (self.sexo =='F'):
            return self.sexo
        else:    
            print("Digite M -> masculino ou F -> feminino")
            verificador = True
            while verificador:
                self.sexo = input("Sexo do atleta: ")
                if self.sexo =='M' or self.sexo =='F':
                    verificador = False
                    return self.sexo
                else:
                    verificador = True
    
    def validarAltura(self):
        self.altura = float(input("Altura: "))
        if(self.altura > 0):
            return self.altura
        else:
            while self.altura <= 0:
                print("Digite um valor positivo maior que zero!")
                self.altura = float(input("Altura: "))
            return self.altura        

    def validarPeso(self):
        self.peso = float(input("Peso: "))
        if(self.peso > 0):
            return self.peso
        else:
            while self.peso <= 0:
                print("Digite um valor positivo maior que zero!")
                self.peso = float(input("Peso: "))
            return self.peso                  



if __name__=="__main__":
    # instanciando o objeto
    atleta = DesafioAtletas()
    quantidade = DesafioAtletas.validarQuantidade()
    i = 0   # indice da listaAtleta
    #  criando 4 listas
    listaAtletaNome = []
    listaAtletaSexo = []
    listaAtletaAltura = []
    listaAtletaPeso = []
        
    while quantidade > 0:
        atleta.nome = input("Nome: ")
        atleta.sexo = atleta.validarSexo()
        atleta.altura = atleta.validarAltura()
        atleta.peso = atleta.validarPeso()
        listaAtletaNome.insert(i,atleta.nome)
        listaAtletaSexo.insert(i,atleta.sexo)
        listaAtletaAltura.insert(i,atleta.altura)
        listaAtletaPeso.insert(i,atleta.peso)
        i += 1
        quantidade -= 1
        
        
    j = 0 # indice da lista
    for a in listaAtletaNome:
       print(f"Nome: {a}")
       print(f"Sexo: {listaAtletaSexo[j]}")
       print(f"Altura: {listaAtletaAltura[j]}")
       print(f"Peso: {listaAtletaPeso[j]}")
       j += 1

        
    