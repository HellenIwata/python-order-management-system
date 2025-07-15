# Sistema de gerenciamento de pedidos - Pedidos - V1.0.0
from customers import customers, search_customer

orders = {}
next_id = 1


def insert_order():
    global next_id
    print("\n--- Vincular Cliente ao Pedido ---")
    found_customer_ids = search_customer()
    if not found_customer_ids:
        print('''Nenhum cliente encontrado.
Cancele a operação ou cadastre um cliente primeiro.''')
        return

    try:
        customer_id = int(input("Digite o ID do cliente para este pedido: "))
        if customer_id not in customers:
            print("Erro: ID de cliente inválido.")
            return
    except ValueError:
        print("Erro: ID de cliente inválido.")
        return

    new_order_items = []
    while True:
        print('''\n--- Adicionar Item ao Pedido
(digite 'fim' no nome do item para concluir) ---''')
        item_name = input("Nome do item: ").strip()
        if item_name.lower() == 'fim':
            if not new_order_items:
                print("Pedido cancelado pois nenhum item foi adicionado.")
                return
            break

        try:
            quantity = int(input("Quantidade: "))
            unit_price = float(input("Valor Unitário: "))
        except ValueError:
            print('''
\nErro: Quantidade e valor devem ser números. Tente novamente.''')
            continue

        new_order_items.append({
            'item_name': item_name,
            'quantity': quantity,
            'unit_price': unit_price
        })
        print(f"Item '{item_name}' adicionado.")

    total_value = sum(item['quantity'] * item['unit_price'] for item in new_order_items)

    orders[next_id] = {
        'customer_id': customer_id,
        'items': new_order_items,
        'total_value': total_value
    }
    print(f'''
    \nPedido ID {next_id} cadastrado com sucesso para o cliente ID {customer_id}!''')
    next_id += 1


def _print_order_details(order_id, info):
    print(f"\n--- Detalhes do Pedido ID: {order_id} ---")
    print(f'''
Cliente: {customers.get(info['customer_id'], {}).get('nome', 'N/A')}
(ID: {info['customer_id']})''')
    print("Itens do Pedido:")
    if not info['items']:
        print("  (Nenhum item neste pedido)")
    else:
        for item in info['items']:
            subtotal = item['quantity'] * item['unit_price']
            print(f"  - Item: {item['item_name']}, Qtd: {item['quantity']}, "
                  f'''
                  V. Unit.: R$ {item['unit_price']:.2f},
                  Subtotal: R$ {subtotal:.2f}''')
    print(f"VALOR TOTAL DO PEDIDO: R$ {info['total_value']:.2f}")


def get_order():
    print("\n--- Lista de pedidos ---")
    if not orders:
        print("Nenhum pedido cadastrado.")
        return
    for order_id, info in orders.items():
        _print_order_details(order_id, info)
    print("-------------------------\n")


def search_order():
    print('''
-----* Buscar Pedido *-----
[1] Buscar por nome do item
[0] Voltar ao menu principal
    ''')
    search_results_ids = []
    opcao = input("Digite a opção desejada: ")
    if opcao == '1':
        item_search = input('''
        Digite o nome do item a ser buscado no pedido: ''').lower()
        for order_id, info in orders.items():
            for item in info['items']:
                if item_search in item['item_name'].lower() and order_id not in search_results_ids:
                    search_results_ids.append(order_id)
    elif opcao == '0':
        return []
    else:
        print("Opção inválida.")
        return []

    if not search_results_ids:
        print("\nNenhum pedido foi encontrado com esse critério.")
    else:
        print("\n--- Pedidos Encontrados ---")
        for order_id in search_results_ids:
            _print_order_details(order_id, orders[order_id])
        print("--------------------------\n")

    return search_results_ids


def update_order():
    print("\n--- Atualizar Pedido ---")
    if not orders:
        print("Nenhum pedido cadastrado.")
        return

    found_ids = search_order()

    if not found_ids:
        return

    order_id_to_update = -1

    if len(found_ids) == 1:
        order_id_to_update = found_ids[0]
        print(f'''Pedido com ID {order_id_to_update}
selecionado para atualização.''')
    else:
        print("Múltiplos pedidos encontrados.")
        try:
            chosen_id = int(input('''Digite o ID do pedido
que deseja atualizar: '''))
            if chosen_id in found_ids:
                order_id_to_update = chosen_id
            else:
                print("Erro: O ID digitado não está na lista de resultados.")
                return
        except ValueError:
            print("Erro: ID inválido. Por favor, digite um número.")
            return

    order_data = orders[order_id_to_update]
    while True:
        _print_order_details(order_id_to_update, order_data)
        print('''
O que você deseja fazer?
[1] Adicionar novo item
[2] Remover item existente
[0] Concluir atualização
        ''')
        action = input("Escolha uma opção: ")

        if action == '1':
            # Adicionar item
            item_name = input("Nome do novo item: ").strip()
            if not item_name:
                print("Nome do item não pode ser vazio.")
                continue
            try:
                quantity = int(input("Quantidade: "))
                unit_price = float(input("Valor Unitário: "))
                order_data['items'].append({
                    'item_name': item_name,
                    'quantity': quantity,
                    'unit_price': unit_price
                })
                print(f"Item '{item_name}' adicionado.")
            except ValueError:
                print("Erro: Quantidade e valor devem ser números.")

        elif action == '2':
            # Remover item
            if not order_data['items']:
                print("Não há itens para remover.")
                continue
            item_to_remove = input('''
            Digite o nome exato do item a ser removido: ''').strip()
            original_items = list(order_data['items'])
            item_found = False
            for item in original_items:
                if item['item_name'] == item_to_remove:
                    order_data['items'].remove(item)
                    item_found = True
                    print(f"Item '{item_to_remove}' removido.")
                    break
            if not item_found:
                print("Item não encontrado.")

        elif action == '0':
            # Recalcular o total e sair
            order_data['total_value'] = sum(item['quantity'] * item['unit_price'] for item in order_data['items'])
            print(f"\nPedido ID {order_id_to_update} atualizado com sucesso!")
            _print_order_details(order_id_to_update, order_data)
            break

        else:
            print("Opção inválida.")


def main():
    opcao = input('''Escolha uma opção
[1] Cadastrar Pedido
[2] Listar Pedidos
[3] Buscar Pedido
[4] Atualizar Pedido
[0] Sair
''')

    if opcao == '1':
        insert_order()
    elif opcao == '2':
        get_order()
    elif opcao == '3':
        search_order()
    elif opcao == '4':
        update_order()
    elif opcao == '0':
        print("Saindo do programa...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True


if __name__ == '__main__':
    main()
