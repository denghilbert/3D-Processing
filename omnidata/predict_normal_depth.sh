#! /bin/bash


#python resize.py --path /home/youming/Desktop/osr/europa/final/rgb/ --shared_height 864
#echo 'finish stupid matting'
FILES="/home/youming/Desktop/osr/*/"
rgb_file="final/rgb"
depth_file="final/depth"
normal_file="final/normal"

for f in $FILES
do
python ~/Desktop/monosdf/preprocess/extract_monocular_cues.py --task depth --img_path "${f}${rgb_file}" --output_path "${f}${depth_file}" --omnidata_path ~/Desktop/omnidata/omnidata_tools/torch/ --pretrained_models ~/Desktop/omnidata/omnidata_tools/torch/pretrained_models/
echo 'finish depth generation'

python ~/Desktop/monosdf/preprocess/extract_monocular_cues.py --task normal --img_path "${f}${rgb_file}" --output_path "${f}${normal_file}" --omnidata_path ~/Desktop/omnidata/omnidata_tools/torch/ --pretrained_models ~/Desktop/omnidata/omnidata_tools/torch/pretrained_models/
echo 'finish normal generation'

done


