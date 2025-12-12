print("""
==== Purpose: demo various curves ====
""")

import numpy as np
import matplotlib.pyplot as plt

def demo_various_curves():

    plt.figure()
    n = np.linspace(1, 50)
    n_lg_n = n * np.log2(n)
    n_n = n * n

    plt.plot(n, n, label="$n$")
    plt.plot(n, n_lg_n, label="$n*lg(n)$")
    plt.plot(n, n_n, label="$n*n$")
    
    plt.title(title := "demo various curves for small n")
    plt.xlabel("n")
    plt.ylabel("y")
    plt.legend()
    plt.savefig(title.replace(' ','_')+'.png')
    plt.pause(0.001)
    print(title)

    ##----

    plt.figure()
    n = np.linspace(1, 5000)
    n_n = n * n

    plt.plot(n, n, label="$n$")
    plt.plot(n, n_lg_n, label="$n*lg(n)$")
    plt.plot(n, n_n, label="$n*n$")
    
    plt.title(title := "demo various curves for large n")
    plt.xlabel("n")
    plt.ylabel("y")
    plt.legend()
    plt.savefig(title.replace(' ','_')+'.png')
    plt.pause(0.001)
    print(title)

def main():
    plt.close('all')
    demo_various_curves()

##[]##
