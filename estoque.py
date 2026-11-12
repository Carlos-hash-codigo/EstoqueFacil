def consultar_estoque(produto, quantidade):
    return f"{produto}: {quantidade} unidade(s) em estoque."


if __name__ == "__main__":
    print(consultar_estoque("Arroz", 25))