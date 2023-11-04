import cv2
import numpy as np
import random

def create_video(file, output):
    vidcap = cv2.VideoCapture(file)
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    assert frame_width % 10 != 0
    assert frame_height % 10 != 0

    buffer = np.empty(shape=(frame_count, frame_height, frame_width, 3), dtype=np.uint8)

    for i in range(frame_count):
        success, frame = vidcap.read()
        if not success:
            raise Exception(f"Failed to read frame {i}")
        buffer[i] = frame

    buffer = buffer.reshape((frame_count * frame_height * frame_width, 3))
    buffer = buffer.ravel()
    buffer = buffer[:-random.randint(0, 100)]
    buffer.tofile(output)


if __name__ == "__main__":
    with open("video.bin", "wb") as output:
        create_video("video.mp4", output)