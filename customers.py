# Sistema de gerenciamento de pedidos - Clientes - V1.0.0

customers = {}
next_id = 1


def insert_customer():
    global next_id
    nome = input("Digite o nome: ")
    fone = input("Digite o telefone: ")
    endereco = input("Digite o endereço: ")
    email = input("Digite o email: ")
    if nome and fone and endereco and email:
        customers[next_id] = {
            'nome': nome,
            'telefone': fone,
            'endereco': endereco,
            'email': email
        }
        print(f"Cliente '{nome}' cadastrado sob o ID: {next_id}")
        next_id += 1
    else:
        print("Erro: algum dado esta vazio, verifique!")


def get_customer():
    print("\n--- Lista de Clientes ---")
    if not customers:
        print("Nenhum cliente cadastrado.")
        return
    for customer_id, info in customers.items():
        print(f'''ID: {customer_id}
Nome: {info['nome']},
Telefone: {info['telefone']},
Endereço: {info['endereco']},
Email: {info['email']}''')
    print("-------------------------\n")


def search_customer():
    print('''
-----* Buscar Cliente *-----
[1] Buscar por nome
[2] Buscar por telefone
[3] Buscar por email
[0] Voltar ao menu principal
    ''')
    search_results_ids = []
    opcao = input("Digite a opção desejada: ")
    if opcao == '1':
        nome = input("Digite o nome do cliente: ").lower()
        for customer_id, info in customers.items():
            if nome in info['nome'].lower():
                search_results_ids.append(customer_id)
    elif opcao == '2':
        fone = input("Digite o telefone do cliente: ")
        for customer_id, info in customers.items():
            if fone in info['telefone']:
                search_results_ids.append(customer_id)
    elif opcao == '3':
        email = input("Digite o email do cliente: ").lower()
        for customer_id, info in customers.items():
            if email in info['email'].lower():
                search_results_ids.append(customer_id)
    elif opcao == '0':
        return []
    else:
        print("Opção inválida.")
        return []

    if not search_results_ids:
        print("\nNenhum cliente foi encontrado com esse critério.")
    else:
        print("\n--- Clientes Encontrados ---")
        for customer_id in search_results_ids:
            info = customers[customer_id]
            print(f'''ID: {customer_id}
Nome: {info['nome']},
Telefone: {info['telefone']},
Endereço: {info['endereco']},
Email: {info['email']}''')
        print("--------------------------\n")

    return search_results_ids


def update_customer():
    print("\n--- Atualizar Cliente ---")
    if not customers:
        print("Nenhum cliente cadastrado.")
        return

    found_ids = search_customer()

    if not found_ids:
        return

    customer_id_to_update = -1

    if len(found_ids) == 1:
        customer_id_to_update = found_ids[0]
        print(f'''Cliente com ID {customer_id_to_update}
        selecionado para atualização.''')
    else:
        print("Múltiplos clientes encontrados.")
        try:
            chosen_id = int(input('''Digite o ID do cliente
            que deseja atualizar: '''))
            if chosen_id in found_ids:
                customer_id_to_update = chosen_id
            else:
                print("Erro: O ID digitado não está na lista de resultados.")
                return
        except ValueError:
            print("Erro: ID inválido. Por favor, digite um número.")
            return

    print("\nDeixe o campo em branco para manter a informação atual.")
    customer_data = customers[customer_id_to_update]

    customers[customer_id_to_update]['nome'] = input(f'''Novo nome
    ({customer_data['nome']}): ''') or customer_data['nome']

    customers[customer_id_to_update]['telefone'] = input(f'''Novo telefone
    ({customer_data['telefone']}): ''') or customer_data['telefone']

    customers[customer_id_to_update]['endereco'] = input(f'''Novo endereço
    ({customer_data['endereco']}): ''') or customer_data['endereco']

    customers[customer_id_to_update]['email'] = input(f'''Novo email
    ({customer_data['email']}): ''') or customer_data['email']

    print(f"\nCliente ID {customer_id_to_update} atualizado com sucesso!")


def main():
    opcao = input('''Escolha uma opção
[1] Cadastrar Cliente
[2] Listar Clientes
[3] Buscar Cliente
[4] Atualizar Cliente
[0] Sair 
''')
    if opcao == '1':
        insert_customer()
    elif opcao == '2':
        get_customer()
    elif opcao == '3':
        search_customer()
    elif opcao == '4':
        update_customer()
    elif opcao == '0':
        print("Saindo do programa...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True


if __name__ == '__main__':
    main()