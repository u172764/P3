import os

# In this exercise I have tried to open a video with another computer in the same network.
# The command used is "ffmpeg -i INPUT -f mpegts udp://host:port" where the host is the receiving IP.
# The used IP is 127.0.0.1 because is a localhost, an equipment physically located in the same place as us.

command = 'ffmpeg -i video_cortado2.mp4 -f mpegts udp://127.0.0.1:1234'
os.system(command)

# This command pretends to play the video we have sent before (this part I have no exit)
command = 'ffplay -f mp4 -f mpegts udp://127.0.0.1:1234'
os.system(command)
