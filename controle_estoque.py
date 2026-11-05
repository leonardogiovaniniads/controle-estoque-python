estoque = 20
produtos = totalVendido = TotalReposto = 0
while True:
    escolha = int(input('[1] Consultar estoque\n[2] Vender produtos\n[3] Repor produtos\n[4] Encerrar'))
    if escolha == 1:
        print(f'Seu estoque atual é {estoque}')
    elif escolha == 2:
        produtos = int(input('Quantos produtos deseja vender?'))
        if produtos > estoque:
            print(f'produtos insuficientes,seu estoque atual é {estoque}')
        elif produtos <=0:
            print('Quantidade invalida')
        else:
            estoque = estoque - produtos
            totalVendido += produtos
            print(f'Venda realizada! Seu estoque atual é {estoque}')
        if estoque == 0:
            print('\033[31mATENÇAO!ESTOQUE ESGOTADO\033[m')
        elif estoque <= 5:
            print('\033[33mAtençao! ESTOQUE BAIXO\033[m')
    elif escolha == 3:
        produtos = int(input('Quantos produtos deseja repor?'))
        if produtos <=0:
            print('Quantidade invalida')
        else:
            estoque = estoque + produtos
            TotalReposto = TotalReposto + produtos
            print(f'Reposiçao realizada , seu estoque atual: {estoque}')
    elif escolha == 4:
        print('='*20)
        print('RELATORIO')
        print('=' * 20)
        print(f'ESTOQUE FINAL: {estoque}')
        print(f'Total de produtos vendidos: {totalVendido}')
        print(f'total de produtos repostos: {TotalReposto}')
        print('encerrado')
        break
    else:
        print('DIGITE UMA OPÇAO VALIDA')