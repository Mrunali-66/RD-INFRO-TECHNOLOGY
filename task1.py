import numpy as np
import pandas as pd
import matplotlib
import requests
import flask
import sklearn

def test_installations():
    print("Virtual Environment & Packages Installed Successfully!\n")
    print("Numpy version:", np.__version__)
    print("Pandas version:", pd.__version__)
    print("Matplotlib version:", matplotlib.__version__)
    print("Requests version:", requests.__version__)
    print("Flask version:", flask.__version__)
    print("Scikit-learn version:", sklearn.__version__)

if __name__ == "__main__":
    test_installations()
