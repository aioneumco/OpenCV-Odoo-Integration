# models/opencv_model.py

import cv2
from odoo import models, fields, api
import base64
import os

class OpenCVImageProcessing(models.Model):
    _name = 'opencv.image.processing'
    _description = 'OpenCV Image Processing'

    name = fields.Char(string='Image Name')
    image = fields.Binary(string='Image')
    image_path = fields.Char(string='Image Path')

    def process_image(self):
        if self.image:
            image_data = base64.b64decode(self.image)
            image_path = "/tmp/processed_image.jpg"
            
            with open(image_path, 'wb') as f:
                f.write(image_data)
            
            img = cv2.imread(image_path)

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            processed_image_path = "/tmp/gray_image.jpg"
            cv2.imwrite(processed_image_path, gray_img)

            with open(processed_image_path, 'rb') as f:
                self.image = base64.b64encode(f.read())
                self.image_path = processed_image_path
            return True
        else:
            return False
