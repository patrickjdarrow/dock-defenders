import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image

# identify output folder and video names
train = '/path_to_folder'
v1 = '/path_to_video1.mp4'
v2 = '/path_to_video2.mp4'
save_frequency = 15

# list of video names (str)
for v in [v1, v2]:
  cap = cv2.VideoCapture(v)

  i = 0
  while cap.isOpened():

    ret,frame = cap.read()
    # save every nth frame
    if i % save_frequency == 0:
      impath = 'train/{}_{}.png'.format(v.split('.')[0], i)
      # ignore frame failures with try loop
      # TODO: update error handling to differentiate between end-of-video-
      # error and failed-frame-error
      try:
        cv2.imwrite(impath, frame)
        print('saving: {}'.format(impath))
      except:
        print('failed: {}'.format(impath))
    
    i += 1
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break    

  cap.release()
  cv2.destroyAllWindows()
