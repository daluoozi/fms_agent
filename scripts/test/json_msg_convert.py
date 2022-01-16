#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
####          Copyright 2020 GuYueHome (www.guyuehome.com).          ###
########################################################################

# 该例程将发布turtle1/cmd_vel话题，消息类型geometry_msgs::Twist

import rospy
from geometry_msgs.msg import Twist
from rospy_message_converter import json_message_converter
from std_msgs.msg import String
from learning_topic.msg import TaskInfo, TaskStatus, RoutingPath
import json

tmp_str1='''
{
	"timestamp_msec":111,          
    "task_from": "FMS",            
    "task_id": 20221111,            
	"task_type": 1,                
	"task_op": 1,                   
	"target_info": {
		"area_type": 1,             
		"dest_x": 335.309999973,    
		"dest_y": 1358.43399705,    
		"heading": 0                
	}
}
'''

tmp_str2='''
{
    "timestamp_msec":111,           
    "vehicle_id": "AAA",
    "task_info": {
        "timestamp_msec":111,           
        "vehicle_id": "AAA",            
        "task_from": "FMS",            
        "task_id": 20221111,          
        "task_type": 1,                 
        "task_op": 1,                   
        "target_info": {
            "area_type": 1,             
            "dest_x": 335.309999973,   
            "dest_y": 1358.43399705,    
            "heading": 0                
        }
    },
    "procedure": 1,                    
    "fail_code": 1001,                  
    "fail_reason": ""                   
}
'''

tmp_str3='''
{
	"timestamp_msec": 1234,
    "vehicle_id": "AAA",
    "task_id": 234,
    "path_points": [
        {
           "x": 418.74,
           "y": 1262.46
        }
    ]
}
'''

def velocity_publisher():
	# ROS节点初始化
    rospy.init_node('velocity_publisher', anonymous=True)

	# 创建一个Publisher，发布名为/turtle1/cmd_vel的topic，消息类型为geometry_msgs::Twist，队列长度10
    turtle_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

	#设置循环的频率
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
		# 初始化geometry_msgs::Twist类型的消息
        vel_msg = Twist()
        vel_msg.linear.x = 0.5
        vel_msg.angular.z = 0.2

		# 发布消息
        turtle_vel_pub.publish(vel_msg)
    	#rospy.loginfo("Publsh turtle velocity command[%0.2f m/s, %0.2f rad/s]", vel_msg.linear.x, vel_msg.angular.z)
		# 按照循环频率延时
        rate.sleep()
def converter():    
    json_str = json.dumps(json.loads(tmp_str3))
    print(json_str)
    message = json_message_converter.convert_json_to_ros_message('learning_topic/RoutingPath', json_str)
    print(message)
    print(type(message))

if __name__ == '__main__':
    try:
        #velocity_publisher()
        converter()
    except rospy.ROSInterruptException:
        pass


