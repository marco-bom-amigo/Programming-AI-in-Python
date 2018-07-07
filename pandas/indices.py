import pandas as pd
from pandas import Series, DataFrame
serie = Series([1,2,3,4,5,6])
print(serie)

pib_paises = Series(         [10000000,          8000000,  7000000,  6000000,  5000000]
                   , index = [ "China", "Estados Unidos", "Canadá", "Rússia", "Brasil"]
                   )
print(pib_paises)
print("PIB Brasil:", pib_paises["Brasil"])

print("\nHigh PIB\n", pib_paises[pib_paises > 7000000])

pib_paises_dict = pib_paises.to_dict()
print(pib_paises_dict)

lista_paises = ["China", "Estados Unidos", "Canadá", "Rússia", "Brasil", "Peru"]
serie_2 = Series(pib_paises_dict, index = lista_paises)
print(serie_2)
print(pd.isnull(serie_2))
print(pd.notnull(serie_2))

serie_2.name = "Produto interno bruto"
serie_2.index.name = "País"
print(serie_2)

print()