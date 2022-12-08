import os
import shutil
from pathlib import Path

# We have created 4 videos with different resolutions, we can extract information of all with mp4info.

# Get fragmented videos
command = 'mp4fragment --fragment-duration 4000 myvideo_1920x1080.mp4 myvideo_1920x1080_frag.mp4'
os.system(command)

# We encrypt at the same time we dash the file
if os.path.exists('output'):
    shutil.rmtree('output')
command = 'mp4dash --mpd-name myvideo.mpd --encryption-key=121a0fca0f1b475b8910297fa8e0a07e' \
          ':a0a1a2a3a4a5a6a7a8a9aaabacadaeaf myvideo_1920x1080_frag.mp4 '
os.system(command)

# I have tried to decrypt the video, but I have no enough time to finish this part. I have created an HTML file to try
# to open the video decrypted, but the video decrypted I don't know why does not contain any information.
data_folder = Path("./output/")
file_to_open = data_folder / "myvideo.mpd"

# If the decrypted video al ready exists from previous executions we erase it.
if os.path.exists('myvideo_decrypted.mpd'):
    os.remove('myvideo_decrypted.mpd')

# To decrypt the video we use the KID and the key, that have used previously to encrypy the video.
command = 'mp4decrypt --key 121a0fca0f1b475b8910297fa8e0a07e:a0a1a2a3a4a5a6a7a8a9aaabacadaeaf ' \
          '{} myvideo_decrypted.mpd'.format(file_to_open)
print('DECRYPTED')
os.system(command)
