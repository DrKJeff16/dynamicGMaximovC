#!/usr/bin/env python3
"""Iterating through value `a`."""


import sys
import numpy as np

import matplotlib.pyplot as plt


def f(x: float, a: float, b: float) -> float:
    """Dynamic System function."""
    return (a * x) + b


def main() -> int:
    """Execute main workflow."""
    # plt.plot([0, 1], [0, 1])
    # plt.show()

    # Initial Conditions
    A = np.arange(0, 50, 1)
    for a in A:
        # a = 1.
        b = 2.
        x_0 = .5
        N = 100

        i = np.arange(0, N, 1)
        x = x_0
        X = list()

        for _ in i:
            print(x)
            X.append(x)
            x = f(x, a, b)

        plt.plot(X)

    plt.yscale('log')
    plt.show()

    return 0


if __name__ == '__main__':
    # print('Hola Mundo')
    sys.exit(main())
