# Registrando dados de um usuário
# em um arquivo "txt"
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
profissao = input("Digite sua profissão: ")

# Gerando o arquivo txt
arquivo = open("Dados_usuário.txt","w")

# Inserindo dados no arquivo
arquivo.write("Meu nome: {}\n".format(nome))
arquivo.write("Minha idade: {}\n".format(idade))
arquivo.write("Minha profissão: {}\n".format(profissao))
arquivo.write("Python é top!")

# Fechando o arquivo
arquivo.close()