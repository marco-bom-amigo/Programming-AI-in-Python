import pandas as pd
import numpy as np

data_frame_1 = pd.DataFrame({"cidade":["Santo André", "Petrópolis", "Belo Horizonte"],"vendas":[1231, 3312, 3212]})
print(data_frame_1)

mapeamento_estado = {"Santo André": "SP", "Belo Horizonte": "MG", "Petrópolis": "RJ"}
data_frame_1["estado"] = data_frame_1["cidade"].map(mapeamento_estado)
print(data_frame_1)

data_frame_1["cidade"] = data_frame_1["cidade"].map(mapeamento_estado)
print(data_frame_1)
