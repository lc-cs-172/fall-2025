""" demo the curves of various logarithms, and how they relate to each other """

import numpy as np
import matplotlib.pyplot as plt

def demo_log_curves():
    x = np.linspace(1, 50)
    log2 = np.log2(x)
    logE = np.log(x)
    log10 = np.log10(x)

    ## logs are related by a CONSTANT factor
    log_2vE = log2 / logE
    log_Ev10 = logE / log10

    plt.close()
    plt.plot(x, log2, label="log2")
    plt.plot(x, logE, label="logE")
    plt.plot(x, log10, label="log10")
    
    plt.plot(x, log_2vE, label="log2/logE")
    plt.plot(x, log_Ev10, label="logE/log10")

    plt.title("compare logarithms of various bases")
    plt.xlabel("x")
    plt.ylabel("$y=f(x)$")
    plt.legend()
    plt.pause(0.001)

def demo_constants_matter():
    n = np.linspace(1, 50)
    lgln = 7 * n * np.log2(n)
    quad = n * n

    plt.close('all')
    plt.figure()
    plt.plot(n, lgln, label="$7 * n * \lg(n)$")
    plt.plot(n, quad, label="$n^2$")
    
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
    
    plt.title(title := "demo log2 curve")
    plt.xlabel("n")
    plt.ylabel("y")
    plt.legend()
    plt.pause(0.001)
    print(title)

    ##----------------

    plt.figure()
    n = np.linspace(1, 20)
    lg_n = np.log2(n)
    expn = 2 ** n
    plt.plot(n, lg_n, label="log2")
    plt.plot(n, expn, label="2**n")
    
    plt.title(title := "compare logarithm and exponential curves w/ knee near 17")
    plt.xlabel("n")
    plt.ylabel("y")
    plt.legend()
    plt.pause(0.001)
    print(title)

    ##----------------

    plt.figure()
    n = np.linspace(1, 100)
    lg_n = np.log2(n)
    expn = 2 ** n
    plt.plot(n, lg_n, label="log2")
    plt.plot(n, expn, label="2**n")
    
    plt.title(title := "compare logarithm and exponential curves w/ knee near 95")
    plt.xlabel("n")
    plt.ylabel("y")
    plt.legend()
    plt.pause(0.001)
    print(title)


plt.close('all')
print("""
==== ready ====
Menu:
    demo_log_curves()
    demo_constants_matter()
    demo_more_curves()
""")

##[]##
