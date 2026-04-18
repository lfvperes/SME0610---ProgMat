from pyscipopt import Model

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
modelo.redirectOutput()
# variaveis de decisao
x1 = modelo.addVar(vtype="C", lb=0)
x2 = modelo.addVar(vtype="C", lb=0)
# funcao objetivo
modelo.setObjective(1*x1 + 2*x2, sense="maximize")
# restricoes
modelo.addCons(x1+x2 <= 4)
modelo.addCons(x1 <= 2)
modelo.addCons(x2 <= 3)
# resolver problema
modelo.optimize()
# mostrar resultado
print(modelo.getObjVal())
