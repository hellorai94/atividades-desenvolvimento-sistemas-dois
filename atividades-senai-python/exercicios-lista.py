#!/usr/bin/env python
# coding: utf-8

# # Exercícios
# 
# ## 1. Faturamento do Melhor e do Pior Mês do Ano
# 
# Qual foi o valor de vendas do melhor mês do Ano?
# E valor do pior mês do ano?

# In[74]:


meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas = vendas_1sem + vendas_2sem
maiorVendas = max(vendas)
menorVendas = min(vendas)
print("O valor máximo de vendas foi:",maiorVendas)
print("O valor mínimo de vendas foi:",menorVendas)


# ## 2. Continuação
# 
# Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.
# 
# Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.
# 
# Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista

# In[75]:


x = vendas.index(max(vendas))
y = vendas.index(min(vendas))

maior = meses[x]
menor = meses[y]
soma = sum(vendas)
porcentual = maiorVendas / soma

print("O melhor mês foi",maior,"com",maiorVendas,"de vendas")
print("O pior mês foi",menor,"com",menorVendas,"de vendas")
print("O faturamento total foi",soma,".")
print('O melhor mês representou {:2%}'.format(porcentual))


# ## 3. Crie uma lista com o top 3 valores de vendas do ano
# 
# Dica: o método remove retira um item da lista.

# In[76]:


top3 = sorted((vendas), reverse=True)[:3]
print(top3)


# In[ ]:




