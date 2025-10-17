import numpy as np
import matplotlib.pyplot as plt

def plot_slice(ax, size):
    global x, y0, y1, y2, yT
    debug = 0

    ax.plot(x[:size], y0[:size], label='constant 30')
    ax.plot(x[:size], y1[:size], label='20 * n')
    ax.plot(x[:size], y2[:size], label='n*n/2')
    ax.plot(x[:size], yT[:size], label='Total')

    ## NB: works perfectly because size is odd
    half = size//2
    full = size
    scale = yT[full] / yT[half]
    if debug: print(f'{(half, scale, yT[full], yT[half])=}')

    list_of_tuples = [ (x[p],yT[p]) for p in [half, full] ]
    if debug: print(f'DEBUG: {list_of_tuples=}')

    tuple_of_lists = zip(*list_of_tuples)
    if debug: print(f'DEBUG: {tuple_of_lists=}')

    (lx, ly) = tuple_of_lists
    ax.plot(lx, ly, label=f'{scale=:4.2f}')

    ax.legend()

def demo():
    global x, y0, y1, y2, yT

    print('''
================================
==== [!Bang!] and we're off ====
================================
''')

    size = 200
    x = np.linspace(0, size, size+1)
    assert len(x) == size+1 and x[0] == 0

    y0 = x*0 + 30
    y1 = 20*x
    y2 = x*x/2
    yT = y2+y1+y0

    plt.close('all')
    fig, axs = plt.subplots(ncols = 3, clear=True, figsize=(12,7))
    fig.suptitle('demo that n**2 term dominates n*n/2+20*n+30 -- EVENTUALLY')
    fig.supxlabel('n')
    fig.supylabel('cost')

    szs = [ size//10, size//3, size ]
    for (ax,sz) in zip(axs,szs):
        plot_slice(ax,sz)

    plt.tight_layout()
    plt.pause(0.001)

demo()

##[]##
