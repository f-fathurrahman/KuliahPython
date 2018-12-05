import numpy as np
from matplotlib import rcParams

rcParams["font.serif"] = ["DejaVu Serif"]
rcParams["font.family"] = ["serif"]

import matplotlib.pyplot as plt
plt.style.use("classic")

Nbins = 20

mu = -0.2
sigma = 0.2
s = np.random.normal(mu, sigma, 1000)

cnt, bins, ignored = plt.hist(s, Nbins, density=True)
yline = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2))
plt.plot(bins, yline, linewidth=2, color="r", label="1st")

mu = 0.3
sigma = 0.3
s = np.random.normal(mu, sigma, 1000)

cnt, bins, ignored = plt.hist(s, Nbins, density=True)
yline = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2))
plt.plot(bins, yline, linewidth=2, color="magenta", label="2nd")

plt.suptitle("Histogram Bilangan Acak Gaussian", fontsize=18)
plt.legend()
plt.title("Oleh: Jojo Sujojo (A016099)")
plt.savefig("../images/normal_v1.pdf")
