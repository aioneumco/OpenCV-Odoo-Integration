# controllers/main.py

from odoo import http
from odoo.http import request
import base64

class OpenCVController(http.Controller):
    
    @http.route('/opencv/upload', type='json', auth='public')
    def upload_image(self, image):
   
        model = request.env['opencv.image.processing'].create({
            'name': 'New Image',
            'image': image,
        })
        model.process_image()
        return {
            'status': 'success',
            'processed_image_path': model.image_path
        }
