#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 23:45:51 2019

@author: yu-minchen
"""

import pandas as pd

df = pd.read_csv('itcont.txt', usecols=[0,3,4])

table = df.groupby(['drug_name'])
res = table.count()
res['drug_cost'] = table.sum()['drug_cost']
res = res.rename(columns = {"id": "num_prescriber"})

res.to_csv('top_cost_drug.txt')