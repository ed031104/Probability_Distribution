import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import models.StudentTcalculations as StudentTcalculations
import chart.StudentTChart as StudentTChart


def DistribucionTStudent(NivelDeConfianza, n, MediaMuetral, DesviacionEstandar, MediaHipotetica):
    x= np.linspace(-5, 5, 1000)
    StudentTChart.GraficarDistribucionTStudent(x,
                                     stats.t.pdf(x,StudentTcalculations.GradosDeLibertad(n)),
                                     StudentTcalculations.ValorCritico(n,NivelDeConfianza),
                                     StudentTcalculations.PruebaZ(n,MediaMuetral,DesviacionEstandar,MediaHipotetica),
                                     StudentTcalculations.GradosDeLibertad(n)
                                     )
       
