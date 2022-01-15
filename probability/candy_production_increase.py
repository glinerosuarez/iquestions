"""
The following dataset shows the U.S. candy industry's 'industrial production index'.
Given the above data, determine if the production in 2015 is significantly higher than in 2016.
Solution will run t-test in Python for premium users.
"""

import math
import pandas as pd
from scipy.stats import t


if __name__ == '__main__':

    df = pd.read_csv(
          "https://raw.githubusercontent.com/erood/interviewqs.com_code_snippets/master/Datasets/candy_production.csv",
          index_col="observation_date"
         )

    df_2015 = df["2015-01-01":"2015-12-31"]
    df_2016 = df["2016-01-01":"2016-12-31"]

    data = pd.DataFrame()
    data["2015"] = df_2015.reset_index()["IPG3113N"]
    data["2016"] = df_2016.reset_index()["IPG3113N"]

    # Dependent Samples T Test
    # null hypothesis: both means are equal
    # alternative hypothesis: means are different
    # Step 1 Subtract each 2016 score from each 2015 score.
    data["2015 - 2016"] = data["2015"] - data["2016"]

    # Step 2 Add up all the values from step 1
    sum = data["2015 - 2016"].sum()

    # Step 3 square the differences from step 1
    data["(2015 - 2016)**2"] = data["2015 - 2016"]**2

    # Step 4 Add up all the squared differences from step 3
    squared_sum = data["(2015 - 2016)**2"].sum()

    # Step 5 Compute t-score
    n = len(data)
    t_score = (sum / n) / math.sqrt((squared_sum - (sum**2/n)) / (n*(n - 1)))

    # Step 6 Get degrees of freedom
    df = n - 1

    # Step 7 Find t value from table
    t_table = t.ppf(0.975, df)

    # Step 8 Compare t values
    abs(t_score) > abs(t_table)

    # Step 9 Finde p value
    p_value = t.sf(t_score, df) * 2

    print(
        f"Since p_value = {p_value:0.4} is greater than 0.05 we cannot reject the null " 
        "hypothesis, we do not have enough evidence to say the production in 2016 "
        "was higher than in 2015.")

