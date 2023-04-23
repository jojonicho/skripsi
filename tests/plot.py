import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('hgrm_file')
parser.add_argument('png_file')
args = parser.parse_args()

png_file = args.png_file
hgrm_file = args.hgrm_file

hgrm_df = pd.read_csv(hgrm_file, comment='#', skip_blank_lines=True, sep=r"\s+", engine='python', header=0, names=['Latency', 'Percentile'], usecols=[0, 3])

# Plot the latency distribution using Seaborn and save it as a png file.

sns.set_theme()
sns.set_style("dark")
sns.set_context("paper")
sns.set_color_codes("pastel")

fig, ax = plt.subplots(1,1,figsize=(20,10))
# fig.suptitle('Latency Results')

sns.lineplot(x='Percentile', y='Latency', data=hgrm_df, ax=ax)
ax.set_title('Latency by Percentile Distribution')
ax.set_xlabel('Percentile (%)')
ax.set_ylabel('Latency (milliseconds)')
ax.set_xscale('log')
ax.set_xticks([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
ax.set_xticklabels(['0', '90', '99', '99.9', '99.99', '99.999', '99.9999', '99.99999'])

fig.tight_layout()
fig.savefig(png_file)
