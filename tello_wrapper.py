
import sys
import threading
import time


from djitellopy import Tello
import math
import numpy as np
import io
import cv2
import random
from PIL import Image


BOX_TRESHOLD = 0.25
TEXT_TRESHOLD = 0.25



class TelloWrapper:
    def __init__(self):
        self.client = Tello()
        self.client.connect()


        # Start video stream
        self.client.streamon()  # Enable video transmission
        t = threading.Thread(target=self.get_stream)
        t.setDaemon(True)
        t.start()

        self.head_img = None # Tello front camera



    def get_stream(self):
        while True:
            self.head_img = self.client.get_frame_read().frame
            time.sleep(0.01)

    def takeoff(self):
        self.client.takeoff()

    def land(self):
        self.client.land()


    def turn_left(self,degree=10):
        """
        Turn left by degree degrees
        :return:
        """
        degree = 10*degree # tello base is 0.1 degrees
        self.client.rotate_counter_clockwise(degree)


    def turn_right(self,degree=10):
        """
        Turn right by degree degrees
        :return:
        """
        degree = 10*degree # tello base is 0.1 degrees
        self.client.rotate_clockwise(degree)


    def forward(self, distance):
        """
        Move forward, too small movements won't work
        distance: distance in meters
        :return:
        """
        distance = distance*100 # tello base is 1cm
        self.client.move_forward(distance) # Move forward


    def back(self, distance):
        """
        Move backward, too small movements won't work
        distance: distance in meters
        :return:
        """
        distance = distance*100 # tello base is 1cm
        self.client.move_back(distance) # Move backward


    def up(self, distance):
        """
        Move up, too small movements won't work
        distance: distance in meters
        :return:
        """
        distance = distance*100 # tello base is 1cm
        self.client.move_up(distance) # Move up


    def down(self, distance):
        """
        Move down, too small movements won't work
        distance: distance in meters
        :return:
        """
        distance = distance*100 # tello base is 1cm
        self.client.move_down(distance) # Move down
        
        
    def get_image(self):
        """
        Get front camera rendered image
        :return:
        """
        return self.head_img

    def get_drone_state(self):
        """
        Get drone state
        :return:{'pitch': int, 'roll': int, 'yaw': int}
        """
        return self.client.query_attitude()



        
    

    
    def ob_objects(self,obj_name_list):
        """
        Note: need to execute get_image first,
        Run object detection model on image img, get target list [<object_name, distance, angle_in_degrees>,...]
        :return: object name list, object info list, bbox image
        """
        pass


    def ob_objects_llm(self,obj_name_list):
        """
        Note: need to execute get_image first, provide observation results for llm
        Run object detection model on image img, get target list [<object_name, distance, angle_in_degrees>,...] for llm reasoning
        :return: [<object_name, distance, angle_in_degrees>,...] e.g. [(door, 0.53, 22), (chair, 4.84, -21)]
        """
        # Get recognition results
        ob_list, final_obj_list, annotated_frame = self.ob_objects(obj_name_list)

        final_result = []

        for obj_info in final_obj_list:
            item = (obj_info[0], obj_info[1], obj_info[3]) #obj_name, camera_distance, angel_degree
            final_result.append(item)

        return final_result








