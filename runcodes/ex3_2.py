# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# entrada
c = float(input())

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="C", name="x_1", lb=0)
x2 = modelo.addVar(vtype="I", name="x_2", lb=0)
# funcao objetivo
modelo.setObjective((c**2)*x1 + c*x2, sense="minimize")
# restricoes
# A = [[5, 1],
#     [1, -1],
#     [-1, 12],
#     [-1, -1],
#     [1, 0],
#     [0, 1]]
# b = [100, 15, 255, -10, 20, 20]
# x = [x1, x2]
# for i, a in enumerate(A):
#     modelo.addCons(a[0]*x[0] + a[1]*x[1] <= b[i])
modelo.addCons(5*x1 + 1*x2 <= 100)
modelo.addCons(1*x1 - 1*x2 <= 15)
modelo.addCons(-1*x1 + 12*x2 <= 225)
modelo.addCons(1*x1 + 1*x2 >= 10)
modelo.addCons(1*x1 + 0*x2 <= 20)
modelo.addCons(0*x1 + 1*x2 <= 20)
# resolver problema
modelo.optimize()
# mostrar resultado
print(round(modelo.getObjVal(), 2))
print(round(modelo.getVal(x1), 2))
print(modelo.getVal(x2))
