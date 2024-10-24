import numpy as np
import pandas as pd
def ordinal_encoding(source,attribute):
    import pandas as pd
    import numpy as np

    data = pd.read_csv(source)

    categories = data[attribute].unique()
    order = {category: idx + 1 for idx, category in enumerate(sorted(categories))}

    data['Size_encoded'] = data['Size'].map(order)

    print(data)

def one_hot_encoding(source,attribute):
    reader=pd.read_csv(source)
    arr1=reader[attribute].unique
    arr2=arr1.sort()
    encoded_frame=pd.DataFrame(np.zeros((reader.shape[0],len(arr1))),columns=arr1)
    for i,j in enumerate(reader['arr1']):
        encoded_frame.loc[i,j]=1
    reader=pd.concat([reader,encoded_frame],axis=1)
    print(reader)