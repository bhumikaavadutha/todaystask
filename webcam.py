import cv2
import argparse

parser = argparse.ArgumentParser(description="Save a video using OpenCV")
parser.add_argument("--output", type=str, help="Output file name")
parser.add_argument("--cam", type=str, help="cam to use for video compression")
    

args = parser.parse_args() 

# Create an object to read from camera
video = cv2.VideoCapture(0)

# We need to check if camera is opened previously or not
if not video.isOpened():
    print("Error reading video file")

# We need to set resolutions, so convert them from float to integer
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)

# Create VideoWriter object to write video
result = cv2.VideoWriter(args.output, cv2.VideoWriter_fourcc(*args.cam), 10, size)

while True:
    ret, frame = video.read()

    if ret:
        # Write the frame into the file
        result.write(frame)

        # Display the frame
        cv2.imshow('Frame', frame)

        # Press 's' to stop the process
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else:
        break

# Release video capture and video write objects
video.release()
result.release()

# Close all frames
cv2.destroyAllWindows()

print("The video was successfully saved to", args.output)