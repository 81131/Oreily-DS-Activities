from typing import List
from Linear_Algebra.Vectors.vectorProperties import dot
from Statistics.single_data_discr.CentralTendencies import mean
from Statistics.single_data_discr.Dispersion import _mean_dif

def covariance (dataset1: List[float], dataset2: List[float]) -> float:
    assert len(dataset1) == len(dataset2), "Both dataset lengths should be same"

    return dot(_mean_dif(dataset1), _mean_dif(dataset2)) / (len(dataset1) - 1)