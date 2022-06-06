#!/usr/bin/env python
import rospy
import tf2_msgs.msg
import cv2
import numpy as np
import math
import tf

pt_size = 200
line_length = 50
screen_size = 500

def callback(msg):
    frame_id = msg.transforms[0].header.frame_id
    if frame_id == 'map':
        translation_x = msg.transforms[1].transform.translation.x
        translation_y = msg.transforms[1].transform.translation.y
        rotation_z = msg.transforms[1].transform.rotation.z
        rotation_w = msg.transforms[1].transform.rotation.w
        euler = tf.transformations.euler_from_quaternion((0, 0, rotation_z, rotation_w))
        euler_z = math.degrees(euler[2] * -1) 

        position_screen = np.full((screen_size, screen_size, 3), 255, dtype=np.uint8)
        pt_x = int(translation_x * pt_size) + int(screen_size/2)
        pt_y = int(translation_y * pt_size*-1) + int(screen_size/2)
        pt_x_screen = 'X : ' + str(pt_x -int(screen_size/2))
        pt_y_screen = 'Y : ' + str(pt_y -int(screen_size/2))
        translation_x_screen = 'translation_x : ' + str(round(translation_x, 3))
        translation_y_screen = 'translation_y : ' + str(round(translation_y, 3))
        euler_screen = 'degree : ' + str(int(euler_z))
        pt_x_e = int(math.cos(math.radians(euler_z)) *line_length)
        pt_y_e = int(math.sin(math.radians(euler_z)) *line_length)
        position_screen = cv2.putText(position_screen, pt_x_screen, (10,20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (250,50,50), 1, cv2.LINE_AA)
        position_screen = cv2.putText(position_screen, translation_x_screen, (100,20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (50,50,50), 1, cv2.LINE_AA)
        position_screen = cv2.putText(position_screen, pt_y_screen, (10,40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (250,50,50), 1, cv2.LINE_AA)
        position_screen = cv2.putText(position_screen, translation_y_screen, (100,40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (50,50,50), 1, cv2.LINE_AA)
        position_screen = cv2.putText(position_screen, euler_screen, (10,60), cv2.FONT_HERSHEY_DUPLEX, 0.5, (250,50,50), 1, cv2.LINE_AA)
        cv2.arrowedLine(position_screen, (pt_x, pt_y), ( pt_x + pt_x_e, pt_y + pt_y_e), (0, 0, 255), 2, cv2.LINE_4, 0, 0.3)
        cv2.imshow('position', position_screen)
        cv2.waitKey(1)

def listener():
    rospy.init_node('tf_subscribe_opencv', anonymous=True)
    rospy.Subscriber("/tf", tf2_msgs.msg.TFMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    