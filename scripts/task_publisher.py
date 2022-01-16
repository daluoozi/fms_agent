#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from fms_agent.msg import TaskInfo
from utils.MqttClient import MqttClient
from rospy_message_converter import json_message_converter

class Client(MqttClient):
    def on_message(self, client, userdata, msg):
        print("haha"+ " " + str(msg.payload.decode()))
        json_str = str(msg.payload.decode())
        task_info = json_message_converter.convert_json_to_ros_message('fms_agent/TaskInfo', json_str)
        global task_pub
        task_pub.publish(task_info)

# ROS节点初始化
rospy.init_node('could_task_publisher', anonymous=True)

task_pub = rospy.Publisher('/cloud/task/task_info', TaskInfo, queue_size=10)


if __name__ == '__main__':
    try:
        c = Client()
        c.subscribe("cloud/A01/task_info")
    except rospy.ROSInterruptException:
        pass


