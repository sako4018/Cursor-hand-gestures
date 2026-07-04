import cv2
import numpy as np
import time
import autopy
import pyautogui
import HandTrackingModule as htm

# ================= SETTINGS =================
wCam, hCam = 640, 480
frameR = 80
clickCooldown = 0.35
scrollSensitivity = 30
# ===========================================

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)

wScr, hScr = autopy.screen.size()

# ================= SMOOTHING =================
alpha = 0.25
smoothX, smoothY = 0, 0
# ============================================

pTime = 0
plocX, plocY = 0, 0

lastClick = 0
dragging = False
prevScrollY = 0


def adaptive_smooth(prev, target):
    speed = abs(target - prev)

    if speed < 10:
        smooth = 10
    elif speed < 40:
        smooth = 6
    else:
        smooth = 3

    return prev + (target - prev) / smooth


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:

        x1, y1 = lmList[8][1:]
        fingers = detector.fingersUp()

        # ================= MOVE =================
        if fingers == [0, 1, 0, 0, 0]:

            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            smoothX = adaptive_smooth(smoothX, x3)
            smoothY = adaptive_smooth(smoothY, y3)

            autopy.mouse.move(smoothX, smoothY)

            plocX, plocY = smoothX, smoothY

        # ================= CLICK =================
        elif fingers == [0, 1, 1, 0, 0]:
            length = detector.findDistance(8, 12)

            if length < 35:
                now = time.time()
                if now - lastClick > clickCooldown:
                    pyautogui.click()
                    lastClick = now

        # ================= SCROLL =================
        elif fingers == [0, 1, 1, 1, 1]:

            currentY = y1

            if prevScrollY != 0:
                delta = currentY - prevScrollY

                if abs(delta) > 2:
                    pyautogui.scroll(-int(delta * scrollSensitivity))

            prevScrollY = currentY

        # ================= DRAG =================
        elif fingers == [0, 0, 0, 0, 0]:

            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            smoothX = adaptive_smooth(smoothX, x3)
            smoothY = adaptive_smooth(smoothY, y3)

            if not dragging:
                pyautogui.mouseDown()
                dragging = True

            pyautogui.moveTo(smoothX, smoothY)

        else:
            prevScrollY = 0

            if dragging:
                pyautogui.mouseUp()
                dragging = False

    # ================= FPS =================
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime != pTime else 0
    pTime = cTime

    cv2.putText(img, str(int(fps)), (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("Ultra AI Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()