import pytest, pandas as pd
from src.quality.validate_data import check_no_nulls, check_unique, check_non_negative, check_row_count
from src.transform.transform_data import standardize_column_names, filter_invalid_records, add_derived_columns

class TestQualityChecks:
    def test_no_nulls_passes(self):
        df = pd.DataFrame({"order_id":[1,2,3],"revenue":[10.,20.,30.]})
        assert all(c.passed for c in check_no_nulls(df,["order_id","revenue"]))
    def test_no_nulls_fails(self):
        df = pd.DataFrame({"order_id":[1,None,3]})
        assert not check_no_nulls(df,["order_id"])[0].passed
    def test_unique_passes(self):
        assert check_unique(pd.DataFrame({"order_id":[1,2,3]}),"order_id").passed
    def test_unique_fails(self):
        assert not check_unique(pd.DataFrame({"order_id":[1,1,3]}),"order_id").passed
    def test_non_negative_passes(self):
        assert check_non_negative(pd.DataFrame({"revenue":[0.,10.,100.]}),"revenue").passed
    def test_non_negative_fails(self):
        assert not check_non_negative(pd.DataFrame({"revenue":[10.,-5.,20.]}),"revenue").passed
    def test_row_count(self):
        assert check_row_count(pd.DataFrame({"a":range(100)}),50).passed

class TestTransforms:
    def test_standardize(self):
        df = pd.DataFrame({"Order ID":[1],"CustomerName":[2]})
        assert "order_id" in standardize_column_names(df).columns
    def test_filter_negative(self):
        df = pd.DataFrame({"revenue":[10.,-5.,20.],"quantity":[1,1,1]})
        assert len(filter_invalid_records(df)) == 2
    def test_derived_cols(self):
        df = pd.DataFrame({"order_date":["2024-01-15"],"revenue":[100.],"cost":[60.]})
        df = add_derived_columns(df)
        assert df["gross_profit"].iloc[0] == 40.
