"""
 ===============================================================
 medical_data_visualiser.py
 ===============================================================

 This module file is meant to help us compute and visualise the
 medical data.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-17
 Version : 0.5.0
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df: pd.DataFrame = pd.read_csv("medical_examination.csv")

df["overweight"] = (df["weight"] / ((df["height"] /100)**2) > 25).astype(int)
df["cholesterol"] = (df["cholesterol"]  > 1).astype(int)
df["gluc"] = (df["gluc"]  > 1).astype(int)
