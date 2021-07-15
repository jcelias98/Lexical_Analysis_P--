###### Método Pânico ####
def panic_method(chain, followers): #essa função consome a cadeia até que seja encontrado um seguidor a partir do dicionário, sendo a chave o símbolo faltante
    if not chain:
        print("Cadeia vazia")
    else:
        inicial = chain[0]["token"]
        while chain and chain[0]["token"] not in followers:
            chain.pop(0)
        if not chain:
            print("Método do pânico consumiu toda a cadeia a partir de ", inicial)
    return chain

