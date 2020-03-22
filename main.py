"""
Name: main.py
Description:
Created by: Masato Shima
Created on: 2020/03/22
"""

# **************************************************
# ----- Import Library
# **************************************************
import pandas as pd
import numpy as np
from metaflow import FlowSpec, step


# **************************************************
# ----- Constants & Variables
# **************************************************
DIR_ROOT = "./"
DIR_DATA = f"{DIR_ROOT}data/"
FILE_PRICE = "price.tsv"


# **************************************************
# ----- Main Process
# **************************************************
class Main(FlowSpec):
	price = None

	@step
	def start(self):
		self.next(self.read_data)

	@step
	def read_data(self):
		self.price = pd.read_csv(
			f"{DIR_DATA}{FILE_PRICE}",
			sep="¥t",
			header=0,
			index_col=0,
			encoding="utf-8"
		)

		self.next(self.end)

	@step
	def end(self):
		pass


# **************************************************
# ----- Main
# **************************************************
if __name__ == "__main__":
	Main()


# **************************************************
# ----- End
# **************************************************
