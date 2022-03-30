import cv2 as cv
import os
import pandas as pd

if __name__ == '__main__':
    '''Creating frames with the coordinates of the eye tracking as a dot on them'''

    image_names = os.listdir('frames')
    data = pd.read_excel('coordinates.xlsx')
    data = pd.DataFrame(data)

    for image_name in image_names:
        print(image_name)
        name_split = image_name.split('me_')[1].split('.')[0]
        i=int(name_split)
        image_path = 'frames/' + image_name
        image = cv.imread(image_path)
        height = image.shape[0]
        x = int(data['X'][i])
        y = height - (int(data['Y'][i]) -23)
        centerOfCircle = (x,y)
        red = (0, 140, 255)
        thickness = 5
        image = cv.circle(image, centerOfCircle, radius = 10, color = red , thickness = -1)
        path = 'frames_and_eye_tracking/' + image_name
        cv.imwrite(path, image)
        i += 1