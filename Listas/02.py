# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
# Loop para adicionar itens ao carrinho
for _ in range(n):
    #print("Adicione iten:" )
    linha = input().strip()

    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(",")

    # Separa o nome do produto e o preço
    nome = (linha[:posicao_espaco]).strip()
    tema = (linha[posicao_espaco + 1:]).strip()

    if tema in eventos:
        eventos[tema].append(nome)
    else:
        eventos[tema] = [nome]



# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")