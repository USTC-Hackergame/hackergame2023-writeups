import cv2
import numpy as np

def restore_video(input_file, output_file, frame_width, frame_height, frame_count):
    with open(input_file, "rb") as input:
        buffer = np.fromfile(input, dtype=np.uint8)

    buffer = buffer[:frame_count * frame_height * frame_width * 3]

    buffer = buffer.reshape((frame_count, frame_height, frame_width, 3))

    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), 15, (frame_width, frame_height))

    for i in range(frame_count):
        frame = buffer[i]
        out.write(frame)

    out.release()

if __name__ == "__main__":
    input_file = "video.bin"
    
    frame_width = 427 # Replace with the correct frame width
    frame_height = 759 # Replace with the correct frame height
    frame_count = 138  # Replace with the correct frame count

    output_file = "restored_video1_"+str(frame_width)+"_"+str(frame_height)+"_"+str(frame_count)+".mp4"

    restore_video(input_file, output_file, frame_width, frame_height, frame_count)
