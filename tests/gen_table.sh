RPS_LIST=(10 50 100)
#directories
MC_SEA=$1
MC_AUS=$2
ASM_SEA=$3
ASM_AUS=$4

#turn this to list
OUTPUT_DIRS=($MC_SEA $MC_AUS $ASM_SEA $ASM_AUS)


for OUTPUT_DIR in "${OUTPUT_DIRS[@]}"
do
  for RPS in "${RPS_LIST[@]}"
  do
    vegeta report -type=json $OUTPUT_DIR/results.${RPS}rps.bin > $OUTPUT_DIR/${RPS}.json
  done
done

python3.8 table.py $MC_SEA $MC_AUS $ASM_SEA $ASM_AUS
