import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped, PoseStamped
from turtlesim.srv import TeleportAbsolute
from tf2_geometry_msgs import do_transform_pose

def visualize():
    pup = rospy.Publisher ("visualize_topic", PoseStamped, queue_size=10)
    rospy.init_node('visualize_node' , anonymous= True)
    rate = rospy.Rate(10)
    tf_buffer = tf2_ros.Buffer()
    #tf_listener = tf2_ros.TransformListener(tf_buffer)

    # visualization_turtle_name = 'visualization_turtle'

    while not rospy.is_shutdown():
        try:
            # base_link_to_map_transform = tf2_ros.Buffer(rospy.Duration(1))
            base_link_to_map_transform = tf_buffer.lookup_transform("map", "base_link", rospy.Time(0))
        except tf2_ros.TransformException as ex:
            rospy.loginfo("tf2_ros.Buffer.lookup_transform failed: %s", ex)
            rospy.sleep(1.0)
            continue

        pose_base_link = PoseStamped()
        pose_base_link.header.stamp = rospy.Time.now()
        pose_base_link.header.frame_id = "base_link"
        pose_base_link.pose.position.x = 0.
        pose_base_link.pose.position.y = 0.
        pose_base_link.pose.position.z = 0.
        pose_base_link.pose.orientation.x = 0.
        pose_base_link.pose.orientation.y = 0.
        pose_base_link.pose.orientation.z = 0.
        pose_base_link.pose.orientation.w = 1.
        
        pose_map = do_transform_pose(pose_base_link, base_link_to_map_transform)

        rospy.loginfo(pose_map)
        pup.publish(pose_map)
        # visualize_current_pose = rospy.ServiceProxy(visualization_turtle_name + '/teleport_absolute', TeleportAbsolute)
        # visualize_current_pose(pose_map.pose.position.x, pose_map.pose.position.y, tf2_geometry_msgs.transformations.quaternion_to_angle(pose_map.pose.orientation))
        rate.sleep()

if __name__ == "__main__":
    try:
        visualize()
    except rospy.ROSInterruptException:
        pass

# import rospy
# from geometry_msgs.msg import TransformStamped, PoseStamped
# from turtlesim.srv import Spawn, SetPen, TeleportAbsolute
# import tf2_geometry_msgs
# import tf2_ros
# from tf.transformations import euler_from_quaternion, quaternion_from_euler

# def main():
#     rospy.init_node("transformation_visualization_node")

#     tf_buffer = tf2_ros.Buffer()
#     # tf_listener = tf2_ros.TransformListener(tf_buffer)

#     # # Spawn a new turtle and store its name.
#     # rospy.wait_for_service("spawn")
#     # spawn_visualization_turtle = rospy.ServiceProxy("spawn", Spawn)
#     # visualization_turtle_name = spawn_visualization_turtle(0, 0, 0).name

#     # # Set pen color to light blue.
#     # configure_visualization_turtle = rospy.ServiceProxy(visualization_turtle_name + "/set_pen", SetPen)
#     # configure_visualization_turtle(0, 255, 0, 3, 0)

#     # rospy.loginfo("Absolute position estimate visualized by '%s' using a green pen.", visualization_turtle_name)

#     rate = rospy.Rate(10.0)
#     while not rospy.is_shutdown():
#         try:
#             base_link_to_map_transform = tf_buffer.lookup_transform("map", "base_link", rospy.Time(0))
#         except tf2_ros.TransformException as ex:
#             rospy.loginfo("tf2_ros.Buffer::lookupTransform failed: %s", str(ex))
#             # rospy.Duration(1.0).sleep()
#             continue
        
#         pose_base_link = PoseStamped()
#         pose_base_link.header.stamp = rospy.Time.now()
#         pose_base_link.header.frame_id = "base_link"
#         pose_base_link.pose.position.x = 0.
#         pose_base_link.pose.position.y = 0.
#         pose_base_link.pose.position.z = 0.
#         pose_base_link.pose.orientation.x = 0.
#         pose_base_link.pose.orientation.y = 0.
#         pose_base_link.pose.orientation.z = 0.
#         pose_base_link.pose.orientation.w = 1.
        
#         pose_map = tf2_geometry_msgs.do_transform_pose(pose_base_link, base_link_to_map_transform)

#         visualize_current_pose = TeleportAbsolute()
#         visualize_current_pose.x = pose_map.pose.position.x
#         visualize_current_pose.y = pose_map.pose.position.y
#         _, _, theta = euler_from_quaternion([
#             pose_map.pose.orientation.x,
#             pose_map.pose.orientation.y,
#             pose_map.pose.orientation.z,
#             pose_map.pose.orientation.w
#         ])
#         visualize_current_pose.theta = theta

#         # rospy.ServiceProxy(visualization_turtle_name + "/teleport_absolute", TeleportAbsolute)(visualize_current_pose)
#         rospy.loginfo (pose_map)
#         rate.sleep()

# if __name__ == "__main__":
#     main()