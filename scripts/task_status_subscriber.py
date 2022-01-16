#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from fms_agent.msg import TaskInfo, TaskStatus
from rospy_message_converter import json_message_converter
from utils.MqttClient import MqttClient

def funCallback(msg):
    rospy.loginfo("task_status poseCallback")
    json_str = json_message_converter.convert_ros_message_to_json(msg)
    print(json_str)
    mqtt_client = MqttClient()
    mqtt_client.publish("cloud/A01/task_status", json_str)

def status_subscriber():
	# ROS节点初始化
    rospy.init_node('task_status_subscriber', anonymous=True)

	# 创建一个Subscriber，订阅名为/turtle1/pose的topic，注册回调函数poseCallback
    rospy.Subscriber("/cloud/task/task_status", TaskStatus, funCallback)

	# 循环等待回调函数
    rospy.spin()

if __name__ == '__main__':
    status_subscriber()


