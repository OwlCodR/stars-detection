# Copyright (c) 2022 Kandakov Danil (p2034 or the_lll_end)
# https://github.com/p2034

import lightkurve as lk
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('MacOSX')
# matplotlib.rcParams['interactive'] == True

# lightkurve data getter
pixelfile = lk.search_targetpixelfile("Trappist-1")[1].download()
lc = pixelfile.to_lightcurve(method="pld").remove_outliers().flatten()

lc.plot()
plt.show()