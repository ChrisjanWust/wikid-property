from pathlib import Path
import pandas as pd
import lazy_object_proxy


PROPERTIES_CSV_PATH = Path(__file__).parent / "properties.csv"
properties_df = lazy_object_proxy.Proxy(
    lambda: pd.read_csv(PROPERTIES_CSV_PATH, index_col="ID")
)


def get_property_label(pid: str):
    return properties_df.loc[pid].label


def get_property_id(label: str):
    return properties_df[properties_df.label == label].iloc[0].name
