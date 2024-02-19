def busca_menor(lista):  # Função que busca o menor elemento e menor índice da lista.
    menor_elemento = lista[0]
    indice_menor_elemento = 0
    for i in range(1, len(lista)):
        if menor_elemento > lista[
            i]:  # Condicional que compara os elementos da lista entre si, se um é maior que o outro.
            menor_elemento = lista[i]  # Redefine o novo menor elemento da lista após a comparação.
            indice_menor_elemento = i  # Redefine o índice do menor elemento.
    return indice_menor_elemento  # Retorna o índice do menor elemento que será utilizado mais tarde.

def ordenacao_por_selecao(lista):
    nova_lista = []  # Cria uma nova lista vaiza.
    for i in range(len(lista)):
        menor_elemento = busca_menor(
            lista)  # O menor elemento será pego pela função busca_menor() e guarda na variável menor_elemento.
        nova_lista.append(lista.pop(
            menor_elemento))  # A lista remove o menor elemento e após isso o adiciona na nova lista, assim ordenando os números por ordem crescente.
    return nova_lista

def main():
    lista = [] #Lista principal vazia
    while True: #Looping principal
        try:
            numero_elementos = int(input("Quantos elementos (números inteiros) você quer na lista? ")) #Define a quantidade de números dentro da lista
            for n in range(numero_elementos):
                numero = int(input("Digite o número inteiro que deseja ter na lista: ")) #Define quais serão os números inseridos na lista
                lista.append(numero)
            print(f"Lista não ordenada: {lista}.")
            print(f"Lista ordenada por seleção: {ordenacao_por_selecao(lista)}.")
            input("Aperte ENTER para sair.")
            break

        except ValueError as V: #Capta o erro de valor caso qualquer coisa que não seja um número inteiro seja digitado no input e mostra para o usuário o erro.
            print(f"Ocorreu um erro: {V}.\nPor favor, tente novamente.")

if __name__ == "__main__":
    main()