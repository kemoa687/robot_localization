#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler
# import random

frame_sequence = 0
def positioning():
    pup = rospy.Publisher ("pose_topic", PoseWithCovarianceStamped, queue_size=10)
    rospy.init_node ('pose_node', anonymous= True)
    rate = rospy.Rate(10)

    q = quaternion_from_euler(0.0, 0.0, 45)

    robot_pose = PoseWithCovarianceStamped()

    robot_pose.header.seq = frame_sequence+1 
    robot_pose.header.stamp= rospy.Time.now()
    robot_pose.header.frame_id = "map"
    robot_pose.pose.pose.position.x = 3
    robot_pose.pose.pose.position.y = 3
    robot_pose.pose.pose.position.z = 0
    robot_pose.pose.pose.orientation.x = q[0]
    robot_pose.pose.pose.orientation.y = q[1]
    robot_pose.pose.pose.orientation.z = q[2]
    robot_pose.pose.pose.orientation.w = q[3]
    robot_pose.pose.covariance = [
                0.1, 0, 0, 0, 0, 0,
                0, 0.1 , 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0.1]
    
    while not rospy.is_shutdown():
        my_msg = robot_pose
        rospy.loginfo (my_msg)
        pup.publish (my_msg)
        rate.sleep()

    
if __name__ == "__main__":
    try:
        positioning()
    except rospy.ROSInterruptException:
        pass