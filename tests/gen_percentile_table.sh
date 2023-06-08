RPS_LIST=(10 50 100)
#directories
MC_SEA=$1
MC_AUS=$2
ASM_SEA=$3
ASM_AUS=$4

#turn this to list
OUTPUT_DIRS=($MC_SEA $MC_AUS $ASM_SEA $ASM_AUS)
#
# REMOVE THIS BLOCK AFTER vegeta report is integrated while testing
#for OUTPUT_DIR in "${OUTPUT_DIRS[@]}"
#do
  #for RPS in "${RPS_LIST[@]}"
  #do
    ##vegeta report -type=json $OUTPUT_DIR/results.${RPS}rps.bin > $OUTPUT_DIR/${RPS}.json
    #for i in {1..3}
      #do
        #echo $OUTPUT_DIR-$i/results.${RPS}rps.bin
        #vegeta report -type=json $OUTPUT_DIR-$i/results.${RPS}rps.bin > $OUTPUT_DIR-$i/${RPS}.json
      #done
  #done
#done


python3.8 percentile-table.py $MC_SEA $MC_AUS $ASM_SEA $ASM_AUS
