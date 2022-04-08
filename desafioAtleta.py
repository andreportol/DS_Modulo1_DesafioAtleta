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
        if (self.sexo == 'M') or (self.sexo == 'F'):
            return self.sexo
        else:
            print("Digite M -> masculino ou F -> feminino")
            verificador = True
            while verificador:
                self.sexo = input("Sexo do atleta: ")
                if self.sexo == 'M' or self.sexo == 'F':
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

    def calcularPesoMedio():
        soma = sum(listaAtletaPeso)
        numero = len(listaAtletaPeso)
        return (soma/numero)

    def calcularMaiorAltura():
        indiceAltura = listaAtletaAltura.index(max(listaAtletaAltura))
        valorAlturaMax = max(listaAtletaAltura)
        lista2 = set(listaAtletaAltura)
        lista3 = []
        # se as listas tiverem o mesmo tamanho não há altura repetidas
        if (len(lista2) == len(listaAtletaAltura)):
            return listaAtletaNome[indiceAltura]
        else:
            for x in range(len(listaAtletaAltura)):
                valor_elemento = listaAtletaAltura[x]
                if valor_elemento == valorAlturaMax:
                    nome_lista = listaAtletaNome[x]
                    lista3.append(nome_lista)
            return lista3

    def exibirRelatorio():
        print("**************RELATORIO****************")
        print(f"Peso medio: {DesafioAtletas.calcularPesoMedio():.2f} kg")
        print(f"Maior altura:  {DesafioAtletas.calcularMaiorAltura()}")
        print(
            f"Porcentagem de homens: {DesafioAtletas.calcularPorcentagemHomens():.2f}%")
        if DesafioAtletas.calcularMediaAlturaMulheres() == 0:
            print("")
        else:
            print(
                f"Altura media mulheres: {DesafioAtletas.calcularMediaAlturaMulheres():.2f} m")

    def calcularPorcentagemHomens():
        numero1 = listaAtletaSexo.count('M')
        numero2 = len(listaAtletaSexo)
        return (numero1/numero2)*100

    def calcularMediaAlturaMulheres():
        contagem = listaAtletaSexo.count('F')
        valorAlturaFinal = 0
        if contagem == 0:
            print("Não há mulheres cadastradas.")
            return 0
        else:
            contadorElementos = 0
            indice = 0
            for _ in listaAtletaSexo:
                s = listaAtletaSexo[indice]
                if s == 'F':
                    #indice1 = listaAtletaSexo[indice]
                    valorAltura = listaAtletaAltura[indice]
                    valorAlturaFinal = valorAlturaFinal + valorAltura
                contadorElementos += 1
                indice += 1
            mediaAltura = (valorAlturaFinal) / (contadorElementos - 1)
            return mediaAltura


if __name__ == "__main__":
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
        listaAtletaNome.insert(i, atleta.nome)
        listaAtletaSexo.insert(i, atleta.sexo)
        listaAtletaAltura.insert(i, atleta.altura)
        listaAtletaPeso.insert(i, atleta.peso)
        i += 1
        quantidade -= 1
        print("*******************************")

    DesafioAtletas.exibirRelatorio()
