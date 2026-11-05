# 📦 Controle de Estoque em Python

Projeto de estudo desenvolvido para praticar lógica de programação
por meio de um controle de estoque executado no terminal.

O programa controla um único produto, com estoque inicial de 20 unidades.

## Funcionalidades

- Consultar o estoque disponível.
- Registrar vendas.
- Impedir vendas acima da quantidade disponível.
- Repor unidades no estoque.
- Recusar quantidades iguais ou menores que zero.
- Exibir alertas de estoque baixo ou esgotado.
- Apresentar um relatório ao encerrar.
- Informar quando uma opção numérica do menu é inválida.

## Conceitos praticados

- Variáveis e operações matemáticas.
- Entrada e saída de dados com input e print.
- Condições com if, elif e else.
- Repetição com while.
- Encerramento de laço com break.
- Acumuladores.
- Formatação de textos com f-strings.
- Cores no terminal com códigos ANSI.

## Como executar

É necessário ter Python 3 instalado. O projeto não utiliza
bibliotecas externas.

1. Baixe o arquivo controle_estoque.py.
2. Abra o terminal na pasta em que o arquivo foi salvo.
3. Execute:

```bash
python controle_estoque.py
```

No Windows, também é possível utilizar:

```bash
py controle_estoque.py
```

Outra opção é abrir o arquivo no PyCharm e executá-lo.

## Menu

```text
[1] Consultar estoque
[2] Vender produtos
[3] Repor produtos
[4] Encerrar
```

## Regras dos alertas

- Estoque igual a zero: estoque esgotado.
- Estoque entre 1 e 5 unidades: estoque baixo.
- Estoque acima de 5 unidades: sem alerta.

Os alertas são verificados na opção de venda.

## Exemplo

Começando com 20 unidades:

- Venda de 16 unidades: estoque passa para 4.
- Reposição de 10 unidades: estoque passa para 14.
- Relatório final: 14 em estoque, 16 vendidas e 10 repostas.

## Limitações atuais

- Os dados ficam apenas na memória e reiniciam ao executar novamente.
- O programa controla apenas um produto.
- As entradas numéricas devem ser números inteiros.
- Letras ou números decimais nos campos numéricos causam erro.
- A exibição das cores depende do suporte do terminal.

## Próxima evolução

Cadastrar vários produtos utilizando listas e dicionários,
conforme avanço nos estudos de Python.

## Autor

Leonardo Giovanini
