from typing import List
from Linear_Algebra.Vectors.vectorProperties import dot
from Statistics.single_data_discr.CentralTendencies import mean
from Statistics.single_data_discr.Dispersion import _mean_dif, standard_deviation


#1. Covariance
#Formula: Cov(X, Y) = Σ (xᵢ - x̄)(yᵢ - ȳ) / (n - 1)
def covariance (dataset1: List[float], dataset2: List[float]) -> float:
    """Returns the covariance of the dataset1 & dataset2"""
    assert len(dataset1) == len(dataset2), "Both dataset lengths should be same"
    return dot(_mean_dif(dataset1), _mean_dif(dataset2)) / (len(dataset1) - 1)

#2. Correlation 
#Formula: r = Cov(X, Y) / (σₓσᵧ)
def correlation(dataset1: List[float], dataset2: List[float]) -> float:
    """Measures how much dataset1 and dataset ]2 vary in tandem about their means"""
    stdev_dataset1 = standard_deviation(dataset1)
    stdev_dataset2 = standard_deviation(dataset2)
    if stdev_dataset1> 0 and stdev_dataset2 > 0:
        return covariance(dataset1, dataset2) / stdev_dataset1/ stdev_dataset2
    else:
        return 0