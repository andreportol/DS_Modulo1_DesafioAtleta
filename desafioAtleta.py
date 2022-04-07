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
    
    def altura(self):
        self.altura1 = float(input("Altura: "))
        if(self.altura1 > 0):
            return self.altura1
        else:
            while self.altura1 <= 0:
                print("Digite um valor positivo maior que zero!")
                self.altura1 = float(input("Altura: "))
            return self.altura1        
                        
if __name__=="__main__":
    quantidade1 = DesafioAtletas.validarQuantidade()
    if quantidade1 > 0:
        # instanciando o objeto
        atleta1 = DesafioAtletas()
        print(atleta1.validarSexo())