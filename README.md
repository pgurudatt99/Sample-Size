# Sample-Size
Calculating minimum required Sample size for research study
#Calculation of Sample Size by using population mean

import math
import numpy as np
from scipy import stats
import pandas as pd

def calculate_sample_size(population_std_dev, confidence_level, margin_of_error):
    z_score = abs(stats.norm.ppf((1 - confidence_level) / 2))
    sample_size = ((z_score * population_std_dev) / margin_of_error) ** 2
    return math.ceil(sample_size)

population_std_dev = float(input ('Enter SD: '))
margin_of_error = float(input ('Enter Margin of Error: '))
confidence_level = 0.95
sample_size = calculate_sample_size(population_std_dev, confidence_level, margin_of_error)
print(f"Sample size: {sample_size}")
Output: Enter SD: 7
Enter Margin of Error: 2
Sample size: 48
#Calculation of Sample Size by using population proportion or prevalance
import math
import numpy as np
from scipy import stats
import pandas as pd

def calculate_sample_size(population_proportion, confidence_level, margin_of_error):
    z_score = abs(stats.norm.ppf((1 - confidence_level) / 2))
    sample_size = (z_score * z_score * population_proportion * (100-population_proportion)) / (margin_of_error*margin_of_error)
    return math.ceil(sample_size)

population_proportion = float(input ('Enter population proportion or prevalance: '))
margin_of_error = float(input ('Enter Margin of Error: '))
confidence_level = 0.95
sample_size = calculate_sample_size(population_proportion, confidence_level, margin_of_error)
print(f"Sample size: {sample_size}")
Output: Enter population proportion or prevalance: 30
Enter Margin of Error: 6
Sample size: 225
