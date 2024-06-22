import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize the hand detector
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Try different camera indices if the current one doesn't work
camera_index = 0
video = cv2.VideoCapture(camera_index)

# Check if the camera is opened successfully
if not video.isOpened():
    print(f"Error: Could not open camera with index {camera_index}")
    exit()

while True:
    ret, img = video.read()
    if not ret:
        print("Error: Failed to capture image")
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=False)  # Update to get both hands and image

    # Default image with 0 fingers up
    fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\0.png")

    if hands:
        hand = hands[0]
        lmlist = hand["lmList"]
        hand_type = hand["type"]
        if lmlist:
            fingerup = detector.fingersUp(hand)
            if fingerup == [0, 1, 0, 0, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\1.png")
            elif fingerup ==[1, 0, 0, 0, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\1.png")
            elif fingerup ==[1, 0, 0, 0, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\1.png")
            elif fingerup ==[0, 0, 1, 0, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\1.png")
            elif fingerup ==[0, 0, 0, 1, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\1.png")
            elif fingerup ==[0, 0, 0, 0, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\1.png")
            elif fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [1, 1, 0, 0, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [1, 0, 1, 0, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [1, 0, 0, 1, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [1, 0, 0, 0, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [0, 1, 0, 1, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [0, 1, 0, 0, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [0, 0, 1, 1, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [0, 0, 1, 0, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")
            elif fingerup == [0, 0, 0, 1, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\2.png")   
            elif fingerup == [0, 1, 1, 1, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\3.png")
            elif fingerup == [1, 1, 1, 0, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\3.png")
            elif fingerup == [1, 1, 0, 1, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\3.png")
            elif fingerup == [1, 1, 0, 0, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\3.png")
            elif fingerup == [1, 0, 1, 1, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\3.png")
            elif fingerup == [1, 0, 0, 1, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\3.png")
            elif fingerup == [0, 1, 0, 1, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\3.png")
            elif fingerup == [0, 1, 1, 0, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\3.png")
            elif fingerup == [0, 0, 1, 1, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\3.png")     
            elif fingerup == [0, 1, 1, 1, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\4.png")
            elif fingerup == [1, 1, 1, 1, 0]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\4.png")
            elif fingerup == [1, 0, 1, 1, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\4.png")
            elif fingerup == [1, 1, 0, 1, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\4.png")
            elif fingerup == [1, 1, 1, 0, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\4.png")   
            elif fingerup == [1, 1, 1, 1, 1]:
                fing = cv2.imread(r"C:\Users\AgentM7\Documents\finger detector\5.png")

    if fing is not None:
        fing = cv2.resize(fing, (220, 280))
        img[50:330, 20:240] = fing
    else:
        print("Error: Could not load finger image")

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
