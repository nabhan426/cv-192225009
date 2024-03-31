import cv2

# Function to manipulate video speed
def manipulate_video_speed(video_path, speed_factor=1):
    video_capture = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(int(25 * speed_factor)) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

# Read the captured video
video_path = 'C:\\Users\\ADMIN\\Downloads\\walk.mp4'  # Change this to your video file path

# Display the original video
manipulate_video_speed(video_path)

# Rewind video to the beginning
# Play video in slow motion
manipulate_video_speed(video_path, 2)

# Rewind video to the beginning
# Play video in fast motion
manipulate_video_speed(video_path, 0.5)
