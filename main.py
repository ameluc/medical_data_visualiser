"""
 ===============================================================
 main.py
 ===============================================================

 This entrypoint file is to be used in development
 for testing purposes.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-17
 Version : 1.0.0
"""

from unittest import main
import medical_data_visualiser

# Testing the function
medical_data_visualiser.draw_cat_plot()
medical_data_visualiser.draw_heat_map()

# Running unit tests automatically
main(module="test_module", exit=False)
