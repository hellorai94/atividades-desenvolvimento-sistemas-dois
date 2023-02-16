#!/usr/bin/env python
# coding: utf-8

# # Instruções básicas - Operações, Variáveis e Input

# ### Atividade 1 - Operações e Variáveis
# Crie um programa que imprima os principais indicadores da Loja "Kratos Store" no último ano.
# Obs: faça tudo usando variáveis.
# 
# Valores do último ano:
# 
# Quantidade de Vendas de Canecas Personalizadas = 120<br>
# Quantidade de Vendas de Garrafas Personalizadas = 75<br>
# Preço Unitário da Canecas Personalizadas = 12,00 <br>
# Preço Unitário da Garrafas Personalizadas = 18,50<br>
# Custo da Loja: 1.696,50
# 
# Use o bloco abaixo para criar todas as variáveis que precisar.

# In[1]:


qntCanPer = 120
qntGarPer = 75
preUnCanPer = 12.00
preUnGarPer = 18.50
custoLoja = 1696.5


# 1. Qual foi o faturamento de Canecas Personalizadas da Loja?

# In[2]:


fatCanPer = qntCanPer * preUnCanPer
print(fatCanPer)


# 2. Qual foi o faturamento de Garrafas Personalizadas da Loja?

# In[4]:


fatGarPer = qntGarPer * preUnGarPer
print(fatGarPer)


# 3. Qual foi o Lucro da loja?

# In[6]:


lucroTotal = ((fatCanPer + fatGarPer) - custoLoja)
print(lucroTotal)


# 4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual

# In[9]:


margem = (lucroTotal / (fatCanPer + fatGarPer)) * 100

print(margem,"%")


# ### Atividade 2 - Inputs e Strings

# A maioria das empresas trabalham com um Código para cada produto que possuem. A Kratos Store, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.
# Ex: 
# Caneca Simples -> Código: CNC1300543<br>
# Caneca Personalizada -> Código: CNC1300545<br>
# Garrafa Simples -> Código: GRF1546001<br>
# Garrafa Personalizada-> Código: GRF17675002<br>
# 
# Repare que todas as canecas tem o início do Código "CNC" e todas as garrafas tem o início do código "GRF".
# 
# Crie um programa de consulta de produto que, dado um código qualquer, identifique se o produto é uma caneca. O programa deve responder True para caneca e False para garrafa. Para inserir um código, use um input.
# 
# Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.

# In[19]:


verificar = "CNC"
produto = input("Digite o código do produto:")

print(verificar in produto)


# # Desvio Condicional - if, else, elif

# ## Atividade 3. Cálculo de Bônus
# 
# - Crie um programa que calcule e dê um print no bônus que os funcionários da Kratos Store devem receber segundo a regra:
# 
# A meta de vendas é R$ 1000.<br> 
# Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.<br>
# Caso contrário o valor de bônus do funcionário é 0.<br>
# Print o bônus dos 3 funcionários

# In[32]:


vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= 1000:
 bonus1 = vendas_funcionario1 * 0.1
else: 
 bonus1 = 0

if vendas_funcionario2 >= 1000:
 bonus2 = vendas_funcionario2 * 0.1
else: 
 bonus2 = 0

if vendas_funcionario3 >= 1000:
 bonus3 = vendas_funcionario3 * 0.1
else: 
 bonus3 = 0

print("O funcionário 1 ganhou",bonus1,"de bônus")
print("O funcionário 2 ganhou",bonus2,"de bônus")
print("O funcionário 3 ganhou",bonus3,"de bônus")

Resposta esperada:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 270 de bônus
# ## Atividade 4. Cálculo de bônus com uma nova regra
# 
# - Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:
# 
# A meta é 1000 vendas<br>
# Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:<br>
# 
# - Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
# - Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
# - Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.
# 
# Use as mesmas variáveis de vendas_funcionários

# In[3]:


vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= 2000:
 bonus1 = vendas_funcionario1 * 0.15
elif vendas_funcionario1 >=1000:
 bonus1 = vendas_funcionario1 * 0.1
else: 
 bonus1 = 0

if vendas_funcionario2 >= 2000:
 bonus2 = vendas_funcionario2 * 0.15
elif vendas_funcionario2 >=1000:
 bonus1 = vendas_funcionario2 * 0.1
else: 
 bonus2 = 0

if vendas_funcionario3 >= 1000:
 bonus3 = vendas_funcionario3 * 0.15
elif vendas_funcionario3 >=1000:
 bonus1 = vendas_funcionario3 * 0.1
else: 
 bonus3 = 0

print("O funcionário 1 ganhou",bonus1,"de bônus")
print("O funcionário 2 ganhou",bonus2,"de bônus")
print("O funcionário 3 ganhou",bonus3,"de bônus")

Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 405 de bônus
# ## Atividade 5. Criando um mini sistema de controle de estoque
# 
# - Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
# - Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve ser avisado (print) para fazer um novo pedido daquele produto.
# - Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:
# 
# - alimentos -> Estoque mínimo: 50
# - bebidas -> Estoque mínimo: 75
# - limpeza -> Estoque mínimo: 30
# 
# Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e quantidade atual em estoque.
# 
# Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"
# 
# Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.<br>
# Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.
# 
# Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.<br>
# Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente.

# In[43]:


categoria = input("Digite a categoria:")
produto = input("Digite o nome do produto:")
quantidade = int(input("Digite a quantidade atual do estoque:"))

if not produto or not categoria or not quantidade:
    print("Por favor, preencha todas as informações corretamente.") 
elif categoria == "alimentos" and quantidade < 50:
    print("Solicitar",produto,"à equipe de compras, temos apenas 60 unidades em estoque.")    
elif categoria == "bebidas" and quantidade < 75:
    print("Solicitar",produto,"à equipe de compras, temos apenas 60 unidades em estoque.")  
elif categoria == "limpeza" and quantidade < 30:
    print("Solicitar",produto,"à equipe de compras, temos apenas 60 unidades em estoque.")
else:
    print()

