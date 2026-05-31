# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# entrada e tratamento
n = int(input())
m = int(input())
tipo = input()
tipo = tipo.replace("R", "C")
tipo = tipo.replace("Z", "I")
tipo = tipo.replace("\r", "")
tipo = list(tipo.split(' '))
A = [list(map(float, input().split(' '))) for _ in range(m)]
b = [10] * m

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x = [modelo.addVar(vtype=tipo[i], name=f"x_{i}", lb=0) for i in range(n)]
# funcao objetivo
modelo.setObjective(sum(x), sense="maximize")
# restricoes
for i in range(m):
    modelo.addCons(sum(A[i][j]*x[j] for j in range(n)) <= b[i])

# resolver problema
modelo.optimize()
# mostrar resultado
if modelo.getStatus() == "infeasible":
    print("INFACTÍVEL")
elif modelo.getStatus() == "unbounded":
    print("ILIMITADO")
else:
    print(round(modelo.getObjVal(), 2))
