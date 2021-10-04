import os 
os.system('ffmpeg -framerate 1/26 pattern_type glob -i "img*.png" -r 26 Glacier.mp4')