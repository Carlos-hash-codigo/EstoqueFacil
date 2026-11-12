def verificar_reposicao(quantidade, estoque_minimo=10):
    if quantidade <= estoque_minimo:
        return "Atenção: realizar reposição."

    return "Estoque em nível adequado."


if __name__ == "__main__":
    print(verificar_reposicao(8))