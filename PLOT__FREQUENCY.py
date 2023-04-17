#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import pandas as pd
    import matplotlib.pyplot as plt

    from matplotlib.ticker import MaxNLocator
    ax = plt.figure().gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    clip_items = pyperclip.paste().strip().splitlines()
    clip_items.sort()

    series = pd.Series(clip_items)
    value_count = series.value_counts(sort=False)
    value_count.sort_index(inplace=True)
    value_count.plot(kind='bar')

    plt.show()

except:
    base_func.display_error_message()
