#!/usr/bin/env python
import rospy
import roslib
import tf
from nav_msgs.msg import Odometry
import time
from darknet_ros_msgs.msg import BoundingBoxes
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist, Point, Vector3
import tkMessageBox

class stopMoving:
    stopMove = 0
instance = stopMoving()

#drone takes off
def takeoff():
   i = 1
   rate = rospy.Rate(10)

   while i<50:
       pub_takeoff.publish(Empty())
       rate.sleep()	
       i+=1

#drone stays in place
def stayInAir():
   i = 1
   while i<50:
       rate.sleep()
       i+=1

#drone lands
def land(): 
   i = 1
   rate = rospy.Rate(10)
   while i<50:
       pub_land.publish(Empty())
       rate.sleep()
       i+=1
   print("successLand")

#drone object recognition
def callback(data):

    i = 1
    j = 1
    rate2 = rospy.Rate(1)
    rate = rospy.Rate(10) 

    for box in data.bounding_boxes:
	#if we found a chair stop
	if (str(box.Class) == "chair"):
            print("found a chair")
	    sub.unregister()
            instance.stopMove = 1
	    print("Start Landing");
            while j<8:
                rate2.sleep()
                j+=1
	    land()

#angular counter clock wise short move 
def movement():
    velocity_publisher=rospy.Publisher("/bebop/cmd_vel", Twist , queue_size=10)		
    vel_msg = Twist()

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.z = 0.2
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    i = 1
    rate = rospy.Rate(10)
    while i<5:
        velocity_publisher.publish(vel_msg)
        rate.sleep()
        i+=1
	

if __name__ == '__main__':
    rospy.init_node('publish_external_position_RS_OBC', anonymous=True)

    print("Searchinng for a chair")

    #publishers and subscribers definistions
    pub_takeoff = rospy.Publisher("/bebop/takeoff", Empty, queue_size=10 )
    pub_land = rospy.Publisher("/bebop/land", Empty, queue_size=10 )
    sub = rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes , callback) 
    
    takeoff()
 
    i = 1
    rate = rospy.Rate(1)
    while i<50 and instance.stopMove == 0: 
        movement()
        rate.sleep()
        i+=1
    
    rospy.spin()




