RPS_LIST=(10 50 100)
OUTPUT_DIR=$1
TITLE=$2

echo $OUTPUT_DIR
echo $TITLE

for i in {1..3}
do
  ./vegeta plot -title="$TITLE" $OUTPUT_DIR-$i/10.bin $OUTPUT_DIR-$i/50.bin $OUTPUT_DIR-$i/100.bin > debug/$OUTPUT_DIR-$i.html
  chromium --headless --disable-gpu --hide-scrollbars --window-size=1100,610 --screenshot=debug/$OUTPUT_DIR-$i.png debug/$OUTPUT_DIR-$i.html
done

