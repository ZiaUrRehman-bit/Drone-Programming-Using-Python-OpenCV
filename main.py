from djitellopy import tello
import cv2

me = tello.Tello()

me.connect()
print(me.get_battery())

me.streamon()
while True:
    img = me.get_frame_read().frame
    cv2.imshow("Image", img)
    cv2.waitKey(1)
# tello.takeoff()
#
# tello.move_left(100)
# tello.rotate_counter_clockwise(90)
# tello.move_forward(100)
#
# tello.land()