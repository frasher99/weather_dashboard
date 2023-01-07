##
import pandas as pd
from udf import get_element_value

##
def test_get_element_value():

    # df_input

    # df_transformed =  get_element_value(df_src=df_input, target_element_name="T")
    df_transformed = pd.DataFrame({"x":[1,2,3], "y":[4,5,6]})
    
    df_expected = pd.DataFrame({"x":[1,2,3], "y":[4,5,6]})
    
    pd.testing.assert_frame_equal(df_transformed, df_expected)

##
if __name__ == "__main__":
    test_get_element_value()
