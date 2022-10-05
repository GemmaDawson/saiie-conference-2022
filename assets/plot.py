import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, MultipleLocator

X = np.linspace(0.001, 50, 10000)
figure = plt.figure(figsize=(3,3))

# Style
# -----------------------------------------------------------------------------
plt.rc("font", family="IBM Plex Sans")
plt.rc("xtick", labelsize="medium")
plt.rc("ytick", labelsize="medium")
plt.rc("axes", labelsize="large", titlesize="large")

# Plot
# -----------------------------------------------------------------------------
ax1 = plt.subplot(1, 1, 1, xlim=(0.0, 50), ylim=(0.0, 100))

ax1.plot(X, np.full(10000, 25), color="#7030A0")
ax1.plot(X, 1.21 ** X, color="#82CFFF")
ax1.plot(X, X, color="#C00000")
ax1.plot(X, np.log2(X), color="#00B050")

ax1.text(37, 30, "Constant", color="#7030A0")
ax1.text(X[4700] + 1.5, 1.21 ** X[4700], "Exponential", color="#82CFFF")
ax1.text(X[8000], X[8000] + 10, "Linear", color="#C00000")
ax1.text(X[6000], np.log2(X[6000]) + 5, "Logarithmic", color="#00B050")

ax1.set_ylabel("Time taken by algorithm $(t)$")
ax1.set_xlabel("Size of problem $(n)$")

#ax1.grid(True, "minor", alpha=0.85, linewidth=0.50, zorder=-20)
#ax1.grid(True, "major", alpha=0.85, linewidth=0.75, zorder=-10)

ax1.tick_params(which="both", labelbottom=False, bottom=False, left=False,
        labelleft=False)
# Show
# -----------------------------------------------------------------------------
plt.tight_layout()
plt.savefig("algorithm.pdf", dpi=900, transparent=True)
plt.show()
