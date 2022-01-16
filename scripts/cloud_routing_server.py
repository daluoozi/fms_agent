#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
#print(__file__)
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)
#sys.path.append(BASE_DIR)

import rospy
from fms_agent.msg import Point
from fms_agent.srv import Routing, RoutingRequest, RoutingResponse
from utils.MqttClient import MqttClient

class Client(MqttClient):
    def on_message(self, client, userdata, msg):
        super().on_message(client, userdata, msg)
        print("haha"+ " " + str(msg.payload))
        

mqtt_response = Client()

def funCallback(req):
	# 显示请求数据
    print(111111)
    print(req.vehicle_id, req.task_id, req.current_pos)
    
    mqtt_request = Client()
    mqtt_request.publish("cloud/A01/routing_request", req.vehicle_id)
    
    path = get_tmp_path()
    rrs = RoutingResponse()
    rrs.vehicle_id = req.vehicle_id
    rrs.task_id = req.task_id
    
    current_x = req.current_pos.x
    current_y = req.current_pos.y
    
    path_first_px = path[0][0]
    path_first_py = path[0][1]
    
    for node in path:
        p = Point()
        p.x = node[0] + (current_x-path_first_px)
        p.y = node[1] + (current_y-path_first_py)
        rrs.path_points.append(p)

	# 反馈数据
    return rrs
    
def get_tmp_path():
    filename = os.path.dirname(os.path.dirname(__file__)) + "/data/tmp_path.txt"
    ret = list()
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(',')
            ret.append([float(line[0]), float(line[1])])
    return ret
    
def routing_server():
	# ROS节点初始化
    rospy.init_node('cloud_routing_server')

	# 创建一个名为/show_person的server，注册回调函数personCallback
    s = rospy.Service('/could/routing/routing_path', Routing, funCallback)

	# 循环等待回调函数
    print("cloud_routing_server is running...")
    rospy.spin()

if __name__ == "__main__":
    routing_server()


