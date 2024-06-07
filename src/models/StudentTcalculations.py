import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def  NivelDeSignificancia(NivelDeConfianza):
    return 1-NivelDeConfianza

def PruebaZ(n, MediaMuestal, DesviacionEstandar, MediaHipotetica):
    return (MediaMuestal-MediaHipotetica)/(DesviacionEstandar/np.sqrt(n))

def  GradosDeLibertad(n):
    return n-1

def ValorCritico(n, NivelDeConfianza):
    df = GradosDeLibertad(n)
    return stats.t.ppf(1 - NivelDeConfianza/2, df)