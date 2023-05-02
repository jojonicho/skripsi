import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import sys
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('mc_sea')
parser.add_argument('mc_aus')
parser.add_argument('asm_sea')
parser.add_argument('asm_aus')
args = parser.parse_args()

mc_sea = args.mc_sea
mc_aus = args.mc_aus
asm_sea = args.asm_sea
asm_aus = args.asm_aus

# JSON_FILES = [f for rps in RPS]]
# create latex table for each 

# EXAMPLE JSON
'''{"latencies":{"total":181370729,"mean":3627414,"50th":2249552,"90th":3489329,"95th":3910717,"99th":52527168,"max":52527168,"min":1782431},"bytes_in":{"total":480,"mean":9.6},"bytes_out":{"total":0,"mean":0},"earliest":"2023-03-31T23:29:16.087472255Z","latest":"2023-03-31T23:29:20.987394359Z","end":"2023-03-31T23:29:20.990598847Z","duration":4899922104,"wait":3204488,"requests":50,"rate":10.20424385097531,"throughput":4.079029905659022,"success":0.4,"status_codes":{"0":30,"200":20},"errors":["Get \"http://ta-server-service.sharedvpc:8080/todos\": dial tcp 0.0.0.0:0-\u003e10.68.9.33:8080: connect: connection refused"]}z
'''

# for json_file in JSON_FILES:

TEMPLATE = '''
               &                & 10 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{3-7}
               & southeast-asia & 50 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{3-7}
MCS with       &                & 100 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{2-7}
MCI            &                & 10 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{3-7}
               & australia      & 50 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{3-7}
               &                & 100 &1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \hline
               &                & 10 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{3-7}
               & southeast-asia & 50 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{3-7}
Istio /       &                & 100 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{2-7}
ASM            &                & 10 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{3-7}
               & australia      & 50 & 1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \cline{3-7}
               &                & 100 &1.486ms & 2.866ms & 33.373ms & 71.60\% \\ \hline
'''


#repeat the template line by line

# mc
# sea

def process_dc(dc):
    dc['latencies']['mean'] = dc['latencies']['mean'] / 1000000
    dc['latencies']['min'] = dc['latencies']['min'] / 1000000
    dc['latencies']['max'] = dc['latencies']['max'] / 1000000
    return dc

json_file = f"{mc_sea}/{10}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f" & & 10 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{3-7}}")

json_file = f"{mc_sea}/{50}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f" & southeast-asia & 50 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{3-7}}")

json_file = f"{mc_sea}/{100}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f"MCS with & & 100 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{2-7}}")

# aus

json_file = f"{mc_aus}/{10}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f"MCI & & 10 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{3-7}}")

json_file = f"{mc_aus}/{50}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f" & australia & 50 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{3-7}}")

json_file = f"{mc_aus}/{100}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f" & & 100 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\hline")

# asm
# sea

json_file = f"{asm_sea}/{10}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f" & & 10 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{3-7}}")

json_file = f"{asm_sea}/{50}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f" & southeast-asia & 50 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{3-7}}")

json_file = f"{asm_sea}/{100}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f"Istio / & & 100 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{2-7}}")

# aus

json_file = f"{asm_aus}/{10}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f"ASM & & 10 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{3-7}}")

json_file = f"{asm_aus}/{50}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f" & australia & 50 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\cline{{3-7}}")

json_file = f"{asm_aus}/{100}.json"
dc = process_dc(json.loads(open(json_file).read()))
print(f" & & 100 & {dc['latencies']['min']} & {dc['latencies']['mean']} & {dc['latencies']['max']} & {dc['success'] * 100:.2f}\% \\\\ \\hline")
