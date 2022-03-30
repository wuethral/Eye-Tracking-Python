import cv2

if __name__ == '__main__':
    '''Converting the frames into mp4 video'''

    image_folder = 'frames_and_eye_tracking'
    video_name = 'operation_video_eye_tracking.mp4'

    images = []

    for i in range(700):
        print(i)
        image_path = image_folder + '/frame_' + str(i) + '.png'

        frame = cv2.imread(image_path)
        images.append(frame)
        height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 15, (width,height))

    for image in images:
        video.write(image)

    cv2.destroyAllWindows()
    video.release()