print('hello world!')

import pandas as pd
data = pd.read_json('/mnt/data/public/yelp/challenge12/'
                      'yelp_dataset/yelp_academic_dataset_photo.json',
                        lines=True, nrows=20)
x = data.groupby('business_id')['label'].apply(set)
print(x)