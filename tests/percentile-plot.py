import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import sys
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('dir_name')
parser.add_argument('unbound', nargs='?', default=None)
args = parser.parse_args()

dir_name = args.dir_name
unbound = args.unbound != None

RPS = [10, 50, 100]

hgrm_files = [f"{args.dir_name}/{rps}.hgrm" for rps in RPS]
hgrm_df = None

# for hgrm_file in hgrm_files:
    # cur_df = pd.read_csv(hgrm_file, comment='#', skip_blank_lines=True, sep=r"\s+", engine='python', header=0, usecols=[0, 1])
    # cur_df['RPS'] = hgrm_file.split('/')[-1].split('.')[0]
    # print(cur_df.to_string())

# create a joint df from the files
for hgrm_file in hgrm_files:
    cur_df = pd.read_csv(hgrm_file, comment='#', skip_blank_lines=True, sep=r"\s+", engine='python', header=0, names=['Latency', 'Percentile'], usecols=[0, 3])
    cur_df['RPS'] = hgrm_file.split('/')[-1].split('.')[0]

    # cur_df = cur_df[cur_df['Percentile'] <= 100] # <= 99
    cur_df = cur_df[cur_df['Percentile'] <= 20] # <= 95

    # print(cur_df.to_string())
    if hgrm_df is None:
        hgrm_df = cur_df
    else:
        hgrm_df = hgrm_df.append(cur_df)

# print(hgrm_files)
# print(hgrm_df.to_string())

# Plot the latency distribution using Seaborn and save it as a png file.

sns.set_theme()
sns.set_style("dark")
sns.set_context("paper")
sns.set_color_codes("pastel")
# increase legend size
# plt.rcParams['legend.fontsize'] = 16

fig, ax = plt.subplots(1,1,figsize=(7.5,5))

# hgrm_df = pd.read_csv(hgrm_file, comment='#', skip_blank_lines=True, sep=r"\s+", engine='python', header=0, names=['Latency', 'Percentile'], usecols=[0, 3])
sns.lineplot(x='Percentile', y='Latency', data=hgrm_df, ax=ax, hue='RPS')

ax.set_title(f'{dir_name} Latency by Percentile Distribution')
ax.set_xlabel('Percentile (%)')
ax.set_ylabel('Latency (milliseconds)')
ax.set_xscale('log')
# ax.set_xticks([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
# ax.set_xticklabels(['0', '90', '99', '99.9', '99.99', '99.999', '99.9999', '99.99999'])

# ax.set_xticks([1, 2, 4, 10, 20, 100, 1000, 10000, 100000, 1000000, 10000000])
# ax.set_xticklabels(['0', '50', '75', '90', '95', '99', '99.9', '99.99', '99.999', '99.9999', '99.99999'])

# limit y axis to 10
if not unbound:
    ax.set_ylim(0, 10)

ax.set_xticks([1, 2, 4, 10, 20])
ax.set_xticklabels(['0', '50', '75', '90', '95'])

ax.axvline(x=2, color='r', linestyle='--')
ax.axvline(x=20, color='r', linestyle='--')

# when the axvline hits a data, annotate the y value
for rps in RPS:
    y_val_50 = hgrm_df[(hgrm_df['RPS'] == str(rps)) & (hgrm_df['Percentile'] == 2)]['Latency'].values[0]
    y_val_95 = hgrm_df[(hgrm_df['RPS'] == str(rps)) & (hgrm_df['Percentile'] == 20)]['Latency'].values[0]

    ax.annotate(f'{y_val_50:.2f}', xy=(2, y_val_50), xytext=(5, -10), textcoords='offset points', ha='left', 
                bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white', alpha=0.5))
    ax.annotate(f'{y_val_95:.2f}', xy=(20, y_val_95), xytext=(5, -10), textcoords='offset points', ha='left', 
                bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white', alpha=0.5))



fig.tight_layout()
fig.savefig(f"percentile-plots/percentile-{dir_name}.png")

