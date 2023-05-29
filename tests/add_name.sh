RPS_LIST=(10 50 100)
OUTPUT_DIR=$1
TITLE=$2

echo $OUTPUT_DIR
echo $TITLE

for i in {1..3}
do
  for RPS in "${RPS_LIST[@]}"
    do
      #echo $OUTPUT_DIR-$i/results.${RPS}rps.bin
      cat $OUTPUT_DIR-$i/results.${RPS}rps.bin | ./vegeta encode --output=$OUTPUT_DIR-$i/$RPS.bin
    done
  vegeta plot -title="$TITLE" $OUTPUT_DIR-$i/10.bin $OUTPUT_DIR-$i/50.bin $OUTPUT_DIR-$i/100.bin > $OUTPUT_DIR-$i/plot.html
done

