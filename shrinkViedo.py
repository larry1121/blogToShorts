import subprocess


cmd="ffmpeg -hide_banner -loglevel error -i temp2/avatar.mp4 -s 170x170 -c:a copy temp2/avatar170_2.mp4"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
for line in process.stdout:
    print(line)