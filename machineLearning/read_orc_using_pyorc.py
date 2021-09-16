import pyorc
import pandas as pd

filename = "/Users/manikandan.kk/hello_world_orc/part-00000-b6e99eb9-cf0c-4b0b-b627-d1dcddb42dfc-c000.snappy.orc"

with open(filename, "rb") as data:
    reader = pyorc.Reader(data)
    columns = reader.schema.fields
    # sort by column id to ensure correct order (since "fields" is a dict, order may not be correct)
    columns = [y for x, y in sorted([(reader.schema.find_column_id(c), c) for c in columns])]
    df = pd.DataFrame(reader, columns=columns)
    print(type(df))
    print(df)
