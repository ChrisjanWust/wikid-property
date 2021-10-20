# wikid-property

Super simple interface to all of WikiData's properties

```python
from wikid_property import get_property_label, get_property_id, properties_df

get_property_id("spouse")
# 'P26'

get_property_label("P26")
# 'spouse'

properties_df.columns
# Index(['label', 'description', 'aliases', 'Data type', 'Count'], dtype='object')

properties_df
#                              label  ...  Count
# ID                                  ...
# P6              head of government  ...  35568
# P10                          video  ...   5506
# P14                   traffic sign  ...  19476
# P15                      route map  ...  22784
# P16                 highway system  ...  51367
#                             ...  ...    ...
# P9982     IGI Global Dictionary ID  ...      0
# P9983  Enciclopedia dei ragazzi ID  ...      0
# P9984                    CANTIC ID  ...      0
# P9985               EMBO member ID  ...      0
# P9986           NDL earlier law ID  ...      0
# [9266 rows x 5 columns]
```
