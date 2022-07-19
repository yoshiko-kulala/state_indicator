#!/usr/bin/env python
import rospy
import datetime
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge
from std_msgs.msg import Int8
import cv2
import getpass

def process_image(msg):
    try:
        bridge = CvBridge()
        dt_now = datetime.datetime.now()
        if msg.data==0:
            if dt_now.second%2==0:
                img = cv2.imread("/home/"+getpass.getuser()+"/catkin_ws/src/state_indicator/scripts/img/04.png", -1)
            else:
                img = cv2.imread("/home/"+getpass.getuser()+"/catkin_ws/src/state_indicator/scripts/img/02.png", -1)
        elif msg.data<4:
            img = cv2.imread("/home/"+getpass.getuser()+"/catkin_ws/src/state_indicator/scripts/img/01.png", -1)
        else:
            if dt_now.microsecond>500000:
                img = cv2.imread("/home/"+getpass.getuser()+"/catkin_ws/src/state_indicator/scripts/img/03.png", -1)
            else:
                img = cv2.imread("/home/"+getpass.getuser()+"/catkin_ws/src/state_indicator/scripts/img/02.png", -1)
        imgMsg = bridge.cv2_to_imgmsg(img, "bgra8")
        pub = rospy.Publisher('state_img', Image, queue_size=10)
        pub.publish(imgMsg)
        cv2.waitKey(1)
    except Exception as err:
        print err

def start_node():
    rospy.init_node('emer_dis')
    rospy.loginfo('img_proc node started')
    rospy.Subscriber("robot_state", Int8, process_image)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass