import os, sys, shutil

filename = sys.argv[1]

def main(filepath):
    if filename.endswith(".mp4") == False:
        print("File must be an .MP4 file")
        return
    if os.path.isfile("part1.mp4") == True:
        os.remove("part1.mp4")
    if os.path.isfile("crasher.mp4") == True:
        os.remove("crasher.mp4")
    shutil.copy(filepath, "part1.mp4")
    os.system("ffmpeg -i part1.mp4 -pix_fmt yuv422p output_1.mp4")
    os.system("ffmpeg -f concat -i test.txt -codec copy crasher.mp4")
    if os.path.isfile("output_1.mp4") == True:
        os.remove("output_1.mp4")

main(filename)