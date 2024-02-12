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

def process_dc(dc, filename, i, rps):
    dc['50th'] = round(dc['latencies']['50th'] / 1000000, 3)
    dc['95th'] = round(dc['latencies']['95th'] / 1000000, 3)
    dc['name'] = f"{filename}-{i}"
    dc['rps'] = rps

    return dc

res = []

location_mp = {"sea": "southeast-asia", "aus": "australia"}
# location_mp = {"sea": "sea", "aus": "aus"}

def process_multiple_dc(filename):
    for rps in [10, 50, 100]:
        i = 1
        while True:
            try:
                json_file = f"{filename}-{i}/{rps}.json"
                dc = process_dc(json.loads(open(json_file).read()), filename, i, rps)
                # print(f" & & {i} & {dc['rps']} & {dc['50th']} & {dc['95th']} \\\\ \\cline{{3-6}}")
                location = location_mp[filename.split('-')[1]]
                res.append([location, dc['rps'], dc['50th'], dc['95th'], "\\\\ \\cline{3-6}"])

                i += 1
            except Exception as e:
                # print(e)
                i -= 1
                break

dc = process_multiple_dc(mc_sea)

# aus

dc = process_multiple_dc(mc_aus)
# asm
# sea

dc = process_multiple_dc(asm_sea)

# aus

dc = process_multiple_dc(asm_aus)

res[8][-1] = "\\\\ \\cline{2-6}"
res[26][-1] = "\\\\ \\cline{2-6}"

res[17][-1] = "\\\\ \\hline"
res[-1][-1] = "\\\\ \\hline"

def debug_res(res):
    for r in res:
        # everything except last
        for i in range(len(r) - 2):
            print(r[i], end=" & ")
        print(r[-2], end=" ")
        print(r[-1])

# HEAD TO HEAD
mcs = res[:18]
asm = res[18:]

res = res[:18]
diff = 0
c = 0

diff2, c2 = 0, 0

for i in range(18):
    # append two spaces
    res[i].append("")
    res[i].append("")

    # res[i][-1] = res[i][-3]
    # res[i][-1] = "\\\\ \\cline{3-12}"
    res[i][-1] = "\\\\ \\cline{3-6}"
    l, r = 2, 3
    res[i][2:6] = [mcs[i][l], asm[i][r], mcs[i][r], asm[i][r]]
    

    if res[i][l] < res[i][r]:
        diff2 += res[i][r] - res[i][l]
        res[i][l] = "\\textbf{" + str(res[i][l]) + "}"
        c2 += 1
    else:
        res[i][r] = "\\textbf{" + str(res[i][r]) + "}"

    r, l = 4, 5
    if res[i][l] < res[i][r]:
        res[i][l] = "\\textbf{" + str(res[i][l]) + "}"
    else:
        diff += res[i][l] - res[i][r]
        c += 1
        res[i][r] = "\\textbf{" + str(res[i][r]) + "}"

diff /= c
diff2 /= c2
print(diff, c)
print(diff2, c2)

res[17][-1] = "\\\\ \\hline"

debug_res(res)

print("MEAN MIN MAX addition")

# MEAN MIN MAX

N_TESTCASES = 3

def process_dc(dc):
    dc['mean'] = dc['latencies']['mean'] / 1000000
    dc['min'] = dc['latencies']['min'] / 1000000
    dc['max'] = dc['latencies']['max'] / 1000000
    return dc

def process_multiple_dc(filename, rps, table_index, table_col):
    # try out every mc_sea file from mc_sea + '-1' and increment until file not exists
    i = 1
    dc = None
    while True:
        try:
            json_file = f"{filename}-{i}/{rps}.json"
            if i == 1:
                dc = process_dc(json.loads(open(json_file).read()))
            else:
                ndc = process_dc(json.loads(open(json_file).read()))

                dc['mean'] += ndc['mean']
                dc['min'] = min(dc['min'], ndc['min'])
                dc['max'] = max(dc['max'], ndc['max'])

            i += 1
        except:
            i -= 1
            break

    dc['mean'] /= i

    location = location_mp[filename.split('-')[1]]

    # limit min, mean, max to 3 decimal places
    dc['mean'] = round(dc['mean'], 3)
    dc['min'] = round(dc['min'], 3)
    dc['max'] = round(dc['max'], 3)

    if table_col == 0:
        for i in range(N_TESTCASES):
            prv_back = res[table_index + i][-1]
            res[table_index + i][-1] = ""
            res[table_index + i].extend(["", "", "", "", "", ""])
            res[table_index + i][-1] = prv_back

    res[table_index + N_TESTCASES // 2][-7 + table_col] = dc['min']
    res[table_index + N_TESTCASES // 2][-5 + table_col] = dc['mean']
    res[table_index + N_TESTCASES // 2][-3 + table_col] = dc['max']

    res[table_index + N_TESTCASES - 1][-1] = "\\\\ \\hline"
    if table_col == 1:
        if res[table_index + N_TESTCASES // 2][-7] < res[table_index + N_TESTCASES // 2][-6]:
            res[table_index + N_TESTCASES // 2][-7] = "\\textbf{" + str(res[table_index + N_TESTCASES // 2][-7]) + "}"
        else:
            res[table_index + N_TESTCASES // 2][-6] = "\\textbf{" + str(res[table_index + N_TESTCASES // 2][-6]) + "}"

        if res[table_index + N_TESTCASES // 2][-5] < res[table_index + N_TESTCASES // 2][-4]:
            res[table_index + N_TESTCASES // 2][-5] = "\\textbf{" + str(res[table_index + N_TESTCASES // 2][-5]) + "}"
        else:
            res[table_index + N_TESTCASES // 2][-4] = "\\textbf{" + str(res[table_index + N_TESTCASES // 2][-4]) + "}"

        if res[table_index + N_TESTCASES // 2][-3] < res[table_index + N_TESTCASES // 2][-2]:
            res[table_index + N_TESTCASES // 2][-3] = "\\textbf{" + str(res[table_index + N_TESTCASES // 2][-3]) + "}"
        else:
            res[table_index + N_TESTCASES // 2][-2] = "\\textbf{" + str(res[table_index + N_TESTCASES // 2][-2]) + "}"
    # res.append([location, rps, dc['min'], dc['mean'], dc['max'], "\\\\ \\cline{3-5}"])


process_multiple_dc(mc_sea, 10, 0, 0)
process_multiple_dc(mc_sea, 50, N_TESTCASES, 0)
process_multiple_dc(mc_sea, 100, 2 * N_TESTCASES, 0)

process_multiple_dc(asm_sea, 10, 0, 1)
process_multiple_dc(asm_sea, 50, N_TESTCASES, 1)
process_multiple_dc(asm_sea, 100, 2 * N_TESTCASES, 1)

process_multiple_dc(mc_aus, 10, 3 * N_TESTCASES, 0)
process_multiple_dc(mc_aus, 50, 4 * N_TESTCASES, 0)
process_multiple_dc(mc_aus, 100, 5 * N_TESTCASES, 0)

process_multiple_dc(asm_aus, 10, 3 * N_TESTCASES, 1)
process_multiple_dc(asm_aus, 50, 4 * N_TESTCASES, 1)
process_multiple_dc(asm_aus, 100, 5 * N_TESTCASES, 1)

debug_res(res)

# HEAD TO HEAD
# mcs = res[:6]
# asm = res[6:]

# res = res[:6]
# diff = 0
# c = 0

# diff2, c2 = 0, 0

# for i in range(6):
    # res[i].append("")
    # res[i].append("")
    # res[i].append("")

    # # 2 -> min
    # # 3 -> mean
    # # 4 -> max

    # # transform to
    # # 2 3 - min mcs, min asm
    # # 3 4
    # # 5 6 - max mcs, max asm
    # res[i][2:7] = [mcs[i][2], asm[i][2], mcs[i][3], asm[i][3], mcs[i][4], asm[i][4]]
    # # add bold to smaller value
    # if res[i][2] < res[i][3]:
        # res[i][2] = "\\textbf{" + str(res[i][2]) + "}"
    # else:
        # res[i][3] = "\\textbf{" + str(res[i][3]) + "}"

    # if res[i][4] < res[i][5]:
        # res[i][4] = "\\textbf{" + str(res[i][4]) + "}"
    # else:
        # res[i][5] = "\\textbf{" + str(res[i][5]) + "}"

    # if res[i][6] < res[i][7]:
        # res[i][6] = "\\textbf{" + str(res[i][6]) + "}"
    # else:
        # res[i][7] = "\\textbf{" + str(res[i][7]) + "}"

    # res[i][-1] = "\\\\ \\cline{3-8}"

# res[-1][-1] = "\\\\ \\hline"


# print()
# debug_res(res)
