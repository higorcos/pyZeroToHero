# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
# print("Quantos itens:" )
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    # print("Adicione iten:" )
    linha = input().strip()

    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")

    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])

    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

for itens in carrinho:
    ipreco = float(itens[1])
    print(f"{itens[0]}: R${ipreco:.2f}")
print(f"Total: R${total:.2f}")

# TODO: Exiba os itens e o total da compra