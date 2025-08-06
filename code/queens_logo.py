import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, t

x = np.linspace(0, 1, 1001)

beta_1 = beta.pdf(x, a=5, b=1.2)
beta_2 = beta.pdf(x, a=5, b=2.2)
t_student = t.pdf(x, df=3, loc=0.5, scale=0.1)
t_student = t_student - np.min(t_student)

height_1 = 0.7
height_2 = 0.6
height_3 = 1

beta_1 = beta_1 / np.max(beta_1) * height_1
beta_2 = beta_2 / np.max(beta_2) * height_2
t_student = t_student / np.max(t_student) * height_3


color_1 = 'white'
color_2 = '#2C6572'
linestyle = {"linewidth": 11, "solid_capstyle": "round"}

fig = plt.figure(figsize=[6, 6], facecolor=color_2)
plt.subplots_adjust(left=0., right=1, top=1, bottom=0.)
plt.plot(x, beta_1, color_1, **linestyle)
plt.plot(x, np.flip(beta_1), color_1, **linestyle)
plt.plot(x, beta_2, color_1, **linestyle)
plt.plot(x, np.flip(beta_2), color_1, **linestyle)
plt.plot(x, t_student, color_1, **linestyle)
plt.axis("off")
plt.savefig("queens_crown.pdf")
plt.savefig("queens_crown.svg")
plt.savefig("queens_crown.png")
