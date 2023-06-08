import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import sys
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('dir_name')
parser.add_argument('dir_name2', nargs='?', default=None)
parser.add_argument('unbound', nargs='?', default=None)
args = parser.parse_args()

dir_name = args.dir_name
dir_name2 = args.dir_name2
unbound = args.unbound != None

n1, n2 = dir_name, dir_name2

dir_names = [dir_name, dir_name2] if dir_name2 else [dir_name]

RPS = [10, 50, 100]

hgrm_dfs = []
for dir_name in dir_names:
    hgrm_files = [f"{dir_name}/{rps}.hgrm" for rps in RPS]
    hgrm_df = None

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
    
    hgrm_dfs.append(hgrm_df)


# Plot the latency distribution using Seaborn and save it as a png file.

sns.set_theme()
sns.set_style("dark")
sns.set_context("paper")
sns.set_color_codes("pastel")
# increase legend size
# plt.rcParams['legend.fontsize'] = 16

fig, ax = plt.subplots(1,2,figsize=(7.5,5))

# hgrm_df = pd.read_csv(hgrm_file, comment='#', skip_blank_lines=True, sep=r"\s+", engine='python', header=0, names=['Latency', 'Percentile'], usecols=[0, 3])

for i in range(len(dir_names)):
    sns.lineplot(x='Percentile', y='Latency', data=hgrm_dfs[i], ax=ax[i], hue='RPS')
    name = dir_names[i]

    splt = name.split('-')
    if splt[0] == 'mc':
        splt[0] = 'mcs'
    name = '-'.join(splt)

    ax[i].set_title(f'{name} Latency by Percentile Distribution')
    ax[i].set_xlabel('Percentile (%)')
    ax[i].set_ylabel('Latency (milliseconds)')
    ax[i].set_xscale('log')

    # limit y axis to 10
    if not unbound:
        ax[i].set_ylim(0, 10)

    ax[i].set_xticks([1, 2, 4, 10, 20])
    ax[i].set_xticklabels(['0', '50', '75', '90', '95'])

    ax[i].axvline(x=2, color='r', linestyle='--')
    ax[i].axvline(x=20, color='r', linestyle='--')

    # when the axvline hits a data, annotate the y value
    for rps in RPS:
        y_val_50 = hgrm_df[(hgrm_df['RPS'] == str(rps)) & (hgrm_df['Percentile'] == 2)]['Latency'].values[0]
        y_val_95 = hgrm_df[(hgrm_df['RPS'] == str(rps)) & (hgrm_df['Percentile'] == 20)]['Latency'].values[0]

        ax[i].annotate(f'{y_val_50:.2f}', xy=(2, y_val_50), xytext=(5, -10), textcoords='offset points', ha='left', 
                    bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white', alpha=0.5))
        ax[i].annotate(f'{y_val_95:.2f}', xy=(20, y_val_95), xytext=(5, -10), textcoords='offset points', ha='left', 
                    bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white', alpha=0.5))



fig.tight_layout()
fig.savefig(f"h2h-percentile-plots/percentile-{n1}-{n2}.png")

