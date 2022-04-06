class DesafioAtletas:
            
    def main():
        quantidade = int(input("Qual a quantidade de atletas: "))
        if quantidade > 0:
            while quantidade > 0:
                nome = input("Nome do atleta: ")
                sexo1 = DesafioAtletas.sexo()  
                quantidade -= 1
        else:
            while quantidade <= 0:
                print("Valor menor ou igual a zero!")
                quantidade = int(input("Digite a quantidade: "))      
    
    
    def sexo():
        sexo = input("Sexo do atleta: ")
        if (sexo =='M') or (sexo =='F'):
            return sexo
        else:    
            print("Digite M -> masculino ou F -> feminino")
            verificador = True
            while verificador:
                sexo = input("Sexo do atleta: ")
                if sexo =='M' or sexo =='F':
                    verificador = False
                    return sexo
                else:
                    verificador = True
                        
   
DesafioAtletas.main()
DesafioAtletas.sexo()