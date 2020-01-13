#!/usr/bin/env python
import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PointStamped, TransformStamped, PoseStamped, PoseWithCovarianceStamped #PoseStamped added to support vrpn_client
from crazyflie_driver.srv import UpdateParams
import time
from std_msgs.msg import String

X0 = 0
Y0 = 0
Z0 = 0

out = False


firstTransform = True


def onNewTransform(pose):
    global msg
    global pub
    global firstTransform

    global X0
    global Y0
    global Z0


        X2 = pose.pose.pose.position.x;
        Y2 = pose.pose.pose.position.y;
        Z2 = pose.pose.pose.position.z;

        msg.point.x = (X2 - X0)*3.4
        msg.point.y = (Y2 - Y0)*3.4
        msg.point.z = (Z2 - Z0)*3.4

        pub.publish(msg)


if __name__ == '__main__':
    rospy.init_node('publish_external_position_RS_OBC', anonymous=True)

    
    #msg = PointStamped()
    #msg.header.seq = 0
    #msg.header.stamp = rospy.Time.now()

    pub = rospy.Publisher("external_position", PointStamped, queue_size=1)
    
    rospy.Subscriber("/darknet_ros/bounding_boxes", PoseWithCovarianceStamped, onNewTransform) # Change this according to your topic
    rospy.spin()


