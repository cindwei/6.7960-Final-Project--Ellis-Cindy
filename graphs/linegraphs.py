import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

types=("Baseline","Magnitude","Energy","Activation","Energy and Magnitude", "Activation and Magnitude")

    b_flop=[12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336,12336]
    m_flop=[124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,124080]
    e_flop=[124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,117838,111600,99136,86688,74256,61840,49440,43246,37056,30870,24688,24688,18510,18510,18510,18510,18510,18510,12336,12336]
    a_flop=[124080,124080,124080,124080,124080,124080,124080,124080,124080,124080,117838,111600,99136,86688,74256,61840,49440,43246,37056,30870,24688,24688,18510,18510,18510,18510,18510,18510,12336,12336]
    em_flop=[124080,124080,124080,124080,124080,124080,124080,124080,124080,117838,105366,92910,80470,68046,55638,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246]
    am_flop=[124080,124080,124080,124080,124080,124080,124080,124080,124080,117838,105366,92910,80470,68046,55638,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246,43246]

epochs = np.arange(30)

# ------------------------------
# STYLE
# ------------------------------
sns.set_theme(style="whitegrid")

plt.rcParams["font.size"] = 14
plt.rcParams["axes.labelsize"] = 16
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["legend.fontsize"] = 12
plt.rcParams["lines.linewidth"] = 3.2   # <--- THICK LINES
plt.rcParams["figure.figsize"] = (12, 7)

colors = sns.color_palette("bright", 7)

# ------------------------------
# PLOT
# ------------------------------
fig, ax = plt.subplots()

ax.plot(epochs, b_flop, label="Baseline", color=colors[0], linestyle="-")
ax.plot(epochs, m_flop, label="Magnitude", color=colors[1], linestyle="-")

# Use dash vs solid for overlapping pairs
ax.plot(epochs, e_flop,  label="Energy",                 color=colors[2], linestyle="-")
ax.plot(epochs, a_flop,  label="Activation",             color=colors[3], linestyle="--")

ax.plot(epochs, em_flop, label="Energy + Magnitude",     color=colors[4], linestyle="-")
ax.plot(epochs, am_flop, label="Activation + Magnitude", color=colors[5], linestyle="--")

# ------------------------------
# LABELS & LEGEND
# ------------------------------
ax.set_xlabel("Epoch")
ax.set_ylabel("FLOPs")
ax.set_title("FLOPs Over Training for Six Pruning Strategies")

ax.grid(True, linestyle="--", alpha=0.6)

ax.legend(frameon=True, fancybox=True, shadow=False, borderpad=0.4, ncol=2)

plt.tight_layout()
plt.show()


#loss, val acc on each individual
b_=[]
m_=[]
e_=[]
a_=[]
em_=[]
am_=[]
