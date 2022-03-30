import cv2

if __name__ == '__main__':

    vidcap = cv2.VideoCapture('operation_video.mp4')
    success,image = vidcap.read()
    count = 0

    while success:
      cv2.imwrite("frames/frame_%d.png" % count, image)
      success,image = vidcap.read()
      print(count)
      count += 1