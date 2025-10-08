""" demo the curves of various logarithms, and how they relate to each other """

import numpy as np
import matplotlib.pyplot as plt

def demo_log_curves():
    x = np.linspace(1, 50)
    log2 = np.log2(x)
    logE = np.log(x)
    log10 = np.log10(x)

    ## logs are related by a CONSTANT factor
    log2vE = log2 / logE
    logEv10 = logE / log10

    plt.close()
    plt.plot(x, log2, label="log2")
    plt.plot(x, logE, label="logE")
    plt.plot(x, log10, label="log10")
    
    plt.plot(x, log2vE, label="log2vE")
    plt.plot(x, logEv10, label="logEv10")

    plt.title("compare logarithms of various bases")
    plt.xlabel("x")
    plt.ylabel("logarithm values")
    plt.legend()
    plt.pause(0.001)

def demo_constants_matter():
    n = np.linspace(1, 50)
    lgln = 7 * n * np.log2(n)
    quad = n * n

    plt.close('all')
    plt.figure()
    plt.plot(n, lgln, label="n log n")
    plt.plot(n, quad, label="n ** 2")
    
    plt.title("constants matter")
    plt.xlabel("n")
    plt.ylabel("various curves")
    plt.legend()
    plt.pause(0.001)
    
def demo_more_curves():
    plt.figure()
    n = np.linspace(1, 1000)
    lg_n = np.log2(n)
    plt.plot(n, lg_n, label="log2")
    
    plt.title("demo log2 curve")
    plt.xlabel("n")
    plt.ylabel("y")
    plt.legend()
    plt.pause(0.001)

    ##----------------

    plt.figure()
    n = np.linspace(1, 20)
    lg_n = np.log2(n)
    expn = 2 ** n
    plt.plot(n, lg_n, label="log2")
    plt.plot(n, expn, label="2**n")
    
    plt.title("compare logarithm and exponential curves")
    plt.xlabel("n")
    plt.ylabel("y")
    plt.legend()
    plt.pause(0.001)

    ##----------------

    plt.figure()
    n = np.linspace(1, 100)
    lg_n = np.log2(n)
    expn = 2 ** n
    plt.plot(n, lg_n, label="log2")
    plt.plot(n, expn, label="2**n")
    
    plt.title("compare logarithm and exponential curves")
    plt.xlabel("n")
    plt.ylabel("y")
    plt.legend()
    plt.pause(0.001)

plt.close('all')
print("""
==== ready ====
demo_log_curves()
demo_constants_matter()
demo_more_curves()
""")

##[]##
