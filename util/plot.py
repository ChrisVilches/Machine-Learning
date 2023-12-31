import numpy as np
import matplotlib.pyplot as plt

def plot_fn(f, x_lo=-20, x_hi=20, linspace_n=100):
  x = np.linspace(x_lo, x_hi, linspace_n)
  y = np.vectorize(f)(x)
  plt.plot(x, y)

def plot_fn_2d(f, x_lo=-20, x_hi=20, y_lo=-20, y_hi=20, linspace_n=100):
  x = np.linspace(x_lo, x_hi, linspace_n)
  y = np.linspace(y_lo, y_hi, linspace_n)
  xs, ys = np.meshgrid(x, y, indexing='ij')
  zs = np.empty(xs.shape)

  for i, j in np.ndindex(xs.shape):
    zs[i][j] = f([xs[i][j], ys[i][j]])

  plt.contourf(xs, ys, zs, levels=30)
  plt.colorbar()

def plot_segment(p, q, color='red'):
  endpoints = np.array([p, q])
  plt.plot(endpoints[:, 0], endpoints[:, 1], color=color)
