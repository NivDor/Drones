#!/usr/bin/env python
import rospy
import roslib
import tf
from nav_msgs.msg import Odometry
import time
from darknet_ros_msgs.msg import BoundingBoxes
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist, Point, Vector3



def takeoff():
   
   	
   #rospy.init_node('takeoff', anonymous=True)

   i = 1
   rate = rospy.Rate(10) # 10hz

   #pub_takeoff.publish(Empty())
   while i<50:
       pub_takeoff.publish(Empty())
       rate.sleep()
       print("hhhh")	
       i+=1

def stayInAir():
   i = 1
   while i<50:
       rate.sleep()
       print("hhhh")	
       i+=1


def land():
   
   
   i = 1
   rate = rospy.Rate(10) # 10hz
   while i<50:
       pub_land.publish(Empty())
       rate.sleep()
       i+=1


def callback(data):
    print("after")
    for box in data.bounding_boxes:
        rospy.loginfo(
            "{}  Xmin: {}, Xmax: {} Ymin: {}, Ymax: {}".format(box.Class,
                box.xmin, box.xmax, box.ymin, box.ymax
            )
        )
		

def movement():
    print("move")
    velocity_publisher=rospy.Publisher("/bebop/cmd_vel", Twist , queue_size=10)		
    vel_msg = Twist()
    print(vel_msg.linear.x)
    vel_msg.linear.x = 0.1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    print(vel_msg.linear.x)
    i = 1
    rate = rospy.Rate(10) # 10hz
    while i<20:
        velocity_publisher.publish(vel_msg)
        rate.sleep()
        i+=1
	
    #while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        #t0 = rospy.Time.now().to_sec()
        #current_distance = 0
 
        ##Loop to move the drone in an specified distance
        #while(current_distance < 3):
            ##Publish the velocity
            #velocity_publisher.publish(vel_msg)
            ##Takes actual time to velocity calculus
            #t1=rospy.Time.now().to_sec()
            ##Calculates distancePoseStamped
            #current_distance= 1*(t1-t0)
    ##After the loop, stops the drone
    #vel_msg.linear.x = 0
    ##Force the robot to stop
    #velocity_publisher.publish(vel_msg)


	

if __name__ == '__main__':
    rospy.init_node('publish_external_position_RS_OBC', anonymous=True)

    print("aaaa")
    #msg = PointStamped()
    #msg.header.seq = 0
    #msg.header.stamp = rospy.Time.now()
    #pub = rospy.Publisher("external_position", PointStamped, queue_size=1)

    pub_takeoff = rospy.Publisher("/bebop/takeoff", Empty, queue_size=10 )
    pub_land = rospy.Publisher("/bebop/land", Empty, queue_size=10 )
    rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes , callback) 

    #rospy.Subscriber("/bebop/cmd_vel", Point , movement)	
    #pub_move=rospy.Publisher("/bebop/cmd_vel", Point , queue_size=10)		
    
    takeoff()
    movement()
    print("successTakeOff")
    #stayInAir()
    print("successStaying")
    land()   	
    print("successLand")
    
    rospy.spin()




