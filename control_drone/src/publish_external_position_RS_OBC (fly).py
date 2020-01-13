#!/usr/bin/env python
import rospy
import roslib
import tf
from nav_msgs.msg import Odometry
import time

from std_msgs.msg import Empty



def takeoff():

   
   pub_takeoff.publish(Empty())	
   #rospy.init_node('takeoff', anonymous=True)

   i = 1
   rate = rospy.Rate(10) # 10hz
   while i<100:
       
       rate.sleep()
       print("hhhh")	
       i+=1



def land():
   pub_land.publish(Empty())
   
   i = 1
   rate = rospy.Rate(10) # 10hz
   while i<100:
       rate.sleep()
       i+=1











X0 = 0
Y0 = 0
Z0 = 0

out = False


firstTransform = True




if __name__ == '__main__':
    rospy.init_node('publish_external_position_RS_OBC', anonymous=True)

    print("aaaa")
    #msg = PointStamped()
    #msg.header.seq = 0
    #msg.header.stamp = rospy.Time.now()

    #pub = rospy.Publisher("external_position", PointStamped, queue_size=1)
    pub_takeoff = rospy.Publisher("bebop/takeoff", Empty, queue_size=10 )
    pub_land = rospy.Publisher("bebop/land", Empty, queue_size=10 )
    takeoff()
    print("success")
    land()   
	
    
    #rospy.Subscriber("/darknet_ros/bounding_boxes", PoseWithCovarianceStamped, takeoff) # Change this according to your topic
    rospy.spin()




