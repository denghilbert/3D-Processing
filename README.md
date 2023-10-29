# 3D-Processing
shell for multi-view images preprocessing
ffmpeg -framerate 30 -pattern_type glob -i './house_cat/*.png' -c:v libx264 -pix_fmt yuv420p house_cat_long.mp4
