#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
from fms_agent.srv import Routing, RoutingRequest
from fms_agent.msg import Point

def client():
	# ROS节点初始化
    rospy.init_node('client')

	# 发现服务后，创建一个服务客户端，连接名为/spawn的service
    rospy.wait_for_service('/could/routing/routing_path')
    try:
        client = rospy.ServiceProxy('/could/routing/routing_path', Routing)

		# 请求服务调用，输入请求数据
        req = RoutingRequest()
        req.vehicle_id = "haha"
        req.task_id = 123456
        
        p = Point()
        p.x = 1.1
        p.y = 2.2
        
        req.current_pos = p
        req.target_pos = p
        
        response = client.call(req)
        return response
    except:
        pass

if __name__ == "__main__":
	#服务调用并显示调用结果
    print(client())


