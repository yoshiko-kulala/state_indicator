#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

def twist_callback(msg):
    robo_vel=math.sqrt(msg.linear.x*msg.linear.x+msg.linear.y*msg.linear.y)
    pub.publish(robo_vel)


pub = rospy.Publisher('robot_velocity', Float32, queue_size=10)
rospy.init_node('robot_velocity')

scan_sub = rospy.Subscriber('cmd_vel', Twist, twist_callback)

rospy.spin()