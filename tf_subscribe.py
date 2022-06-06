#!/usr/bin/env python
import rospy
import tf2_msgs.msg

def callback(msg):
    frame_id = msg.transforms[0].header.frame_id
    if frame_id == 'map':
        rospy.loginfo("translation_x %f",msg.transforms[1].transform.translation.x)
        rospy.loginfo("translation_y %f",msg.transforms[1].transform.translation.y)
        rospy.loginfo("rotation_z %f",msg.transforms[1].transform.rotation.z)

def listener():
    rospy.init_node('tf_subscribe', anonymous=True)
    rospy.Subscriber("/tf", tf2_msgs.msg.TFMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    