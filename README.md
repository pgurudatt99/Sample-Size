# Sample-Size
Calculating minimum required Sample size for research study
#Calculation of Sample Size by using population mean

import math
import numpy as np
from scipy import stats
import pandas as pd

def calculate_sample_size(population_std_dev, confidence_level, margin_of_error):
    sample_size = ((z_score * population_std_dev) / margin_of_error) ** 2
    return math.ceil(sample_size)
z_score = 1.96
population_std_dev = float(input ('Enter SD: '))
margin_of_error = float(input ('Enter Margin of Error: ')) # use 5%, 10%, 15% or max 20% of mean
confidence_level = 0.95
sample_size = calculate_sample_size(population_std_dev, confidence_level, margin_of_error)
print(f"Sample size: {sample_size}")
Output-
Enter SD: 7
Enter Margin of Error: 2
Sample size: 48

#Calculation of Sample Size by using population proportion or prevalence
import math
import numpy as np
from scipy import stats
import pandas as pd

def calculate_sample_size(population_proportion, confidence_level, margin_of_error):
    sample_size = (z_score * z_score * population_proportion * (100-population_proportion)) / (margin_of_error*margin_of_error)
    return math.ceil(sample_size)

population_proportion = float(input ('Enter population proportion or prevalance: ')) # value in terms of percentage
margin_of_error = float(input ('Enter Margin of Error: ')) # use 5%, 10%, 15% or max 20% of proportion
confidence_level = 0.95
z_score = 1.96
sample_size = calculate_sample_size(population_proportion, confidence_level, margin_of_error)
print(f"Sample size: {sample_size}")
Output-
Enter population proportion or prevalance: 30
Enter Margin of Error: 6
Sample size: 225
#Calculation of Sample Size to test the difference between two population means
#Objective: Testing null hypothesis: M1=M2

import math
import numpy as np
from scipy import stats 
import pandas as pd

def calculate_sample_size(pooled_std_dev, confidence_level, margin_of_error):
    numerator = 2*((z_score_alpha + z_score_bita)*pooled_std_dev)**2
 denominator = (margin_of_error)**2
    sample_size = numerator/denominator   
    return math.ceil(sample_size)
z_score_alpha = 1.96
z_score_bita = 0.84
confidence_level = 0.95
n1=float(input('Number in first group: '))
n2=float(input('Number in second group: '))
SD1=float(input ('Enter SD for first group: '))
SD2=float(input('Enter SD for second group: '))
pooled_std_dev = (((n1-1)*SD1**2+(n2-1)*SD2**2)/(n1+n2-2))**0.5
margin_of_error = float(input ('Enter Margin of Error: ')) # use value less than or equal to difference of two means m1-m2
sample_size = calculate_sample_size(pooled_std_dev, confidence_level, margin_of_error)
print(f"Pooled SD: {pooled_std_dev}")
print(f"Sample size: {sample_size}")
Output-
Number in first group: 100
Number in second group: 50
Enter SD for first group: 2
Enter SD for second group: 3
Enter Margin of Error: 1
Pooled SD: 2.37810962855067
Sample size: 89 (in each group)

#Calculation of Sample Size to test the difference between two population proportions
#Objective: Testing null hypothesis: P1=P2

import math
import numpy as np
from scipy import stats 
import pandas as pd

def calculate_sample_size(proportion, margin_of_error):
    numerator = (p1*(100-p1)+p2*(100-p2))*((z_score_alpha + z_score_bita)**2)
    denominator = (margin_of_error)**2
    sample_size = numerator/denominator   
    return math.ceil(sample_size)
z_score_alpha = 1.96
z_score_bita = 0.84
confidence_level = 0.95
p1=float(input('Proportion in first group: '))
p2=float(input('Proportion in second group: '))
proportion=abs((p1+p2)/2)
margin_of_error = float(input ('Enter Margin of Error: ')) # use value less than or equal to difference of two means p1-p2
sample_size = calculate_sample_size(proportion, margin_of_error)
print(f"Sample size: {sample_size}")
Output-
Proportion in first group: 80
Proportion in second group: 60
Enter Margin of Error: 20
Sample size: 79 (in each group)
