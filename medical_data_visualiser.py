"""
 ===============================================================
 medical_data_visualiser.py
 ===============================================================

 This module file is meant to help us compute and visualise the
 medical data.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-17
 Version : 1.0.0
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df: pd.DataFrame = pd.read_csv("medical_examination.csv")

df["overweight"] = (df["weight"] / ((df["height"] /100)**2) > 25).astype(int)
df["cholesterol"] = (df["cholesterol"]  > 1).astype(int)
df["gluc"] = (df["gluc"]  > 1).astype(int)

def draw_cat_plot():
    """
     This function draws a categorical plot after making some adjustment to to data.

     Returns
     -------
         A visualisation figure
    """

    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    df_cat = (
        df_cat
            .groupby(by=["cardio", "variable", "value"])
            .size()
            .reset_index()
            .rename(columns={0:"total"})
    )

    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar"
    )

    fig.savefig("catplot.png")

    return fig

def draw_heat_map():
    """
     This function draws a heat map after making some adjustment to to data.

     Returns
     -------
         A heat map to see correlations inside the data.
    """

    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.95)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.95))
    ]
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", ax=ax)
    fig.savefig("heatmap.png")

    return fig
