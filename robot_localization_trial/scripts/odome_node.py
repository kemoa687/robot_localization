#!/usr/bin/env python
import rospy
from geometry_msgs.msg import TwistWithCovarianceStamped
from tf.transformations import quaternion_from_euler
# import random

frame_sequence = 0
def odometry():
    pup = rospy.Publisher ("odom_topic", TwistWithCovarianceStamped, queue_size=10)
    rospy.init_node ('odom_node', anonymous= True)
    rate = rospy.Rate(10)


    robot_odom = TwistWithCovarianceStamped()

    robot_odom.header.seq = frame_sequence+1 
    robot_odom.header.stamp= rospy.Time.now()
    robot_odom.header.frame_id = "base_link"
    robot_odom.twist.twist.linear.x = 3
    robot_odom.twist.twist.linear.y = 0
    robot_odom.twist.twist.linear.z = 0
    robot_odom.twist.twist.angular.x = 0
    robot_odom.twist.twist.angular.y = 0
    robot_odom.twist.twist.angular.z = 3
    robot_odom.twist.covariance = [
                0.1, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0.1
            ]
    
    while not rospy.is_shutdown():
        my_msg = robot_odom
        rospy.loginfo (my_msg)
        pup.publish (my_msg)
        rate.sleep()

    
if __name__ == "__main__":
    try:
        odometry()
    except rospy.ROSInterruptException:
        pass