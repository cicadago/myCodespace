import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(
    0, 2 * np.pi, 200
)  # generates 200 evenly spaced points between 0 and 2π
print(type(x), x.shape)  # <class 'numpy.ndarray'> (200,)
y = np.sin(x)
print(type(y), y.shape)  # <class 'numpy.ndarray'> (200,)

fig, ax = plt.subplots()  # return a tuple[Figure, Axes]
print(type(fig), type(ax))  # <class 'matplotlib.figure.Figure'> <class 'matplotlib.axes._axes.Axes'>

ax.plot(x, y)
plt.show()
