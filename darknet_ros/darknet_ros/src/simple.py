#! /usr/bin/env python
import rospy
from darknet_ros_msg.msg import BoundingBoxes
from std_msg.msg import Header
from std_msg.msg import String



def callback(data):
	for box in data.bounding_boxes:
		rospy.loginfo("Xmin: {}, Xmax: {}".format(box.xmin , box.xmax))

def main():
	rospy.init_node('dorrr')
	rate= rospy.Rate(2)
	while not rospy.is_shutdown():
		print "helpp"
	rate.sleep()
	rate= rospy.Rate(2)
	while not rospy.is_shutdown():
		rospy.init_node('dorrr')
		rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes , callback)
		rospy.spin()
		

#rospy.init_node('dorrr')
#rate= rospy.Rate(2)
#while not rospy.is_shutdown():
#	print "helpp"
#	rate.sleep()




