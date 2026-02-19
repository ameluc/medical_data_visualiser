"""
 ===============================================================
 test_module.py
 ===============================================================

 This module file is used to test the function.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-17
 Version : 0.5.0
"""

import unittest
import matplotlib as mpl
import medical_data_visualiser

class CatPlotTestCase(unittest.TestCase):
    """
     A class to group the unit tests about the categorial plot visualisation
    """

    def setUp(self):
        self.fig = medical_data_visualiser.draw_cat_plot()
        self.ax = self.fig.axes.flat[0]

    def test_line_plot_labels(self):
        """
         This test checks the labels for the categorial plot visualisation.
        """

        actual = self.ax.get_xlabel()
        expected = "variable"
        info = "Expected line plot xlabel to be \"variable\"."

        self.assertEqual(actual, expected, info)

        actual = self.ax.get_ylabel()
        expected = "total"
        info = "Expected line plot ylabel to be \"total\"."

        self.assertEqual(actual, expected, info)

        actual = [
            label.get_text()
            for label in self.ax.get_xaxis().get_majorticklabels()
        ]

        expected = [
            "active",
            "alco",
            "cholesterol",
            "gluc",
            "overweight",
            "smoke"
        ]
        info = """Expected bar plot secondary x labels to be
            "active",
            "alco",
            "cholesterol",
            "gluc",
            "overweight",
            "smoke"
        """

        self.assertEqual(actual, expected, info)

    def test_bar_plot_number_of_bars(self):
        """
         This test checks the numbers of bars in our visualisation.
        """

        actual = len([
            rect
            for rect in self.ax.get_children()
            if isinstance(rect, mpl.patches.Rectangle)
        ])
        expected = 13
        info = "Expected a different number of bars chart."

        self.assertEqual(actual, expected, info)
