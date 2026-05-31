# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# entrada
m = int(input())
A = [list(map(float, input().split(' '))) for _ in range(m)]
b = [0] * m

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="C", name="x_1", lb=0)
x2 = modelo.addVar(vtype="C", name="x_2", lb=0)
x3 = modelo.addVar(vtype="I", name="x_3", lb=0)
# funcao objetivo
modelo.setObjective(10*x1 + 5*x2 + 1*x3, sense="maximize")
# restricoes
for i in range(m):
    modelo.addCons(A[i][0] * x1 + A[i][1] * x2 + A[i][2] * x3 <= b[i])

# resolver problema
modelo.optimize()
# mostrar resultado
if modelo.getStatus() == "infeasible":
    print("INFACTÍVEL")
elif modelo.getStatus() == "unbounded":
    print("ILIMITADO")
else:
    print(round(modelo.getObjVal(), 2))
