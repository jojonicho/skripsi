RPS_LIST=(10 50 100)
OUTPUT_DIR=$1

for RPS in "${RPS_LIST[@]}"
do
  vegeta report -type=hdrplot $OUTPUT_DIR/results.${RPS}rps.bin > $OUTPUT_DIR/${RPS}.hgrm
  #python3.8 plot.py $OUTPUT_DIR/${RPS}.hgrm $OUTPUT_DIR/${RPS}.png
done

python3.8 plot.py $OUTPUT_DIR
