#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
margin_of_error = float(input ('Enter Margin of Error: ')) # use 5%, 10%, 15% or max 20% of mean
confidence_level = 0.95
sample_size = calculate_sample_size(population_std_dev, confidence_level, margin_of_error)
print(f"Sample size: {sample_size}")


# In[4]:


#Calculation of Sample Size by using population proportion or prevalance
import math
import numpy as np
from scipy import stats
import pandas as pd

def calculate_sample_size(population_proportion, confidence_level, margin_of_error):
    z_score = abs(stats.norm.ppf((1 - confidence_level) / 2))
    sample_size = (z_score * z_score * population_proportion * (100-population_proportion)) / (margin_of_error*margin_of_error)
    return math.ceil(sample_size)

population_proportion = float(input ('Enter population proportion or prevalance: ')) # value in terms of percentage
margin_of_error = float(input ('Enter Margin of Error: ')) # use 5%, 10%, 15% or max 20% of proportion
confidence_level = 0.95
sample_size = calculate_sample_size(population_proportion, confidence_level, margin_of_error)
print(f"Sample size: {sample_size}")


# In[ ]:




