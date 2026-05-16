# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# entrada
arr = input()
b = list(map(int, arr.split(' ')))


# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="C", name="x_1", lb=0)
x2 = modelo.addVar(vtype="I", name="x_2", lb=0)
# funcao objetivo
modelo.setObjective(x1 + 2*x2, sense="minimize")
# restricoes
A = [[-1, 1],
     [1, 1],
     [1, 0],
     [0, 1]]
# sinal das restricoes
sig = [True, False, True, True]
for i, b_i in enumerate(b):
    if sig[i]:
        modelo.addCons(A[i][0] * x1 + A[i][1] * x2 >= b_i)
    else:
        modelo.addCons(A[i][0] * x1 + A[i][1] * x2 <= b_i)
# resolver problema
modelo.optimize()
# mostrar resultado
if modelo.getStatus() == "infeasible":
    print("INFACTÍVEL")
else:
    print(round(modelo.getObjVal(), 2))
    print(round(modelo.getVal(x1), 2))
    print(round(modelo.getVal(x2), 2))
