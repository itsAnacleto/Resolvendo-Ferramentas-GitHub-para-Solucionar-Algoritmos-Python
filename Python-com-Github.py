#1 - Concatenando Dados 

# Passo 1: Entrada de dados
# O computador pergunta o nome e guarda a resposta numa "caixa" chamada 'primeiro_nome'
primeiro_nome = input("Digite o seu primeiro nome: ")

# O computador faz a mesma coisa para o sobrenome
sobrenome = input("Digite o seu sobrenome: ")

# Passo 2: Manipulação e Concatenação
# Vamos colar o nome, dar um espaço em branco " ", e colar o sobrenome
nome_completo = primeiro_nome + " " + sobrenome

# Passo 3: Mostrar o resultado
print("Olá! O seu nome completo é: " + nome_completo)

#2 - Repetindo Textos

# Passo 1: Receber o texto (String)
palavra = input("Digite uma palavra ou frase para repetir: ")

# Passo 2: Receber o número (Inteiro)
# Atenção: Usamos int() "abraçando" o input para transformar o texto digitado em número!
numero = int(input("Quantas vezes você quer repetir? "))

# Passo 3: Manipulação e Repetição
# Primeiro juntamos a palavra com um espaço para não ficar tudo grudado, depois multiplicamos.
resultado = (palavra + " ") * numero

# Passo 4: Mostrar o resultado
print("Aqui está o seu texto repetido: " + resultado)

#3 - Operações Matemáticas Simples

# Passo 1: Receber os dois números
# Usamos float() para aceitar tanto números inteiros quanto quebrados
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Passo 2: Realizar as operações matemáticas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# Passo 3: Mostrar os resultados
# Podemos usar a vírgula dentro do print() para juntar texto e números facilmente!
print("O resultado da Soma é:", soma)
print("O resultado da Subtração é:", subtracao)
print("O resultado da Multiplicação é:", multiplicacao)
print("O resultado da Divisão é:", divisao)

#4 - Verificando Números Pares e Ímpares

# Passo 1: Receber o número inteiro (já sabemos usar o int!)
numero = int(input("Digite um número inteiro: "))

# Passo 2: A Condicional (A tomada de decisão)
# Lemos assim: "Se o resto da divisão do número por 2 for igual a zero..."
if numero % 2 == 0:
    # Este bloco só roda se a resposta for SIM
    print("O número que você digitou é Par!")

else:
    # Este bloco só roda se a resposta for NÃO
    print("O número que você digitou é Ímpar!")

    # ou pela IA

    print("Par" if numero % 2 == 0 else "Ímpar")

#5 - Calculando Média de Notas

# Passo 1: Solicitar as três notas ao usuário
nota1 = float(input("Digite a primeira nota (ex: 7.5): "))
nota2 = float(input("Digite a segunda nota (ex: 8.0): "))
nota3 = float(input("Digite a terceira nota (ex: 6.2): "))

# Passo 2: Calcular a média usando os parênteses para proteger a soma
media = (nota1 + nota2 + nota3) / 3

# Passo 3: Mostrar o resultado final
print("A média final do aluno é:", media)

#6 - Verificando Palíndromos

# Passo 1: Receber a palavra do usuário
palavra_original = input("Digite uma palavra para testarmos: ")

# Passo 2: Padronização
# Transformamos a palavra em minúsculas para não dar problema na comparação
palavra_limpa = palavra_original.lower()

# Passo 3: Inversão da String
# Usamos o superpoder do fatiamento [::-1] para virar a palavra de trás para frente
palavra_invertida = palavra_limpa[::-1]

# Passo 4: Verificação (A Condicional)
# Comparamos se a palavra limpa é exatamente igual (==) à sua versão invertida
if palavra_limpa == palavra_invertida:
    print("Incrível! '" + palavra_original + "' é um Palíndromo! 🔄")
else:
    print("Poxa, '" + palavra_original + "' não é um Palíndromo.")
    