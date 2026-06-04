import numpy as np
import pandas as pd

from src.data.clean import drop_id, flag_impossible, missing_summary


def test_drop_id_removes_patient_id():
    df = pd.DataFrame({"patient_id": [1, 2], "age": [50, 60]})
    out = drop_id(df)
    assert list(out.columns) == ["age"]


def test_drop_id_ok_when_missing():
    df = pd.DataFrame({"age": [50, 60]})
    assert list(drop_id(df).columns) == ["age"]


def test_flag_impossible_sets_out_of_range_to_nan():
    df = pd.DataFrame({"creatinine": [1.0, -0.5, 2.0, 99.0]})
    out = flag_impossible(df)
    assert np.isnan(out.loc[1, "creatinine"])
    assert np.isnan(out.loc[3, "creatinine"])
    assert out.loc[0, "creatinine"] == 1.0
    assert out.loc[2, "creatinine"] == 2.0


def test_flag_impossible_ignores_unknown_columns():
    df = pd.DataFrame({"foo": [1, 2, 3]})
    assert flag_impossible(df).equals(df)


def test_missing_summary_counts():
    df = pd.DataFrame({"a": [1, np.nan, 3], "b": [1, 2, 3]})
    rep = missing_summary(df)
    assert set(rep.columns) == {"missing", "pct"}
    assert rep.loc["a", "missing"] == 1
    assert rep.loc["b", "missing"] == 0
