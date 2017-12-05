from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import os
import logging
import time
import json

# Dummy Web serer class.
class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):        
        #--- logging ---#
        logging.info('[Request method] GET')
        logging.info('[Request url]' + str(self.path))
        logging.info('[Request headers]\n' + str(self.headers))
        
        self.send_response(200)
        ### URL Routing ###
        resfilename = ''
        if self.path.startswith("/service/storage"):
          logging.info('[Response for GET /service/storage] 200 OK\n--------------------\n\n\n--------------------')
          resfilename = 'get_response_storage.json'
          self.send_header('Content-type', 'application/json')
        elif self.path.startswith("/service/projection"):
          logging.info('[Response for GET /service/projection] 200 OK\n--------------------\n\n\n--------------------')
          resfilename = 'get_response_projection.json'
          self.send_header('Content-type', 'application/json')
        elif self.path.startswith("/property"):
          logging.info('[Response for GET /property] 200 OK\n--------------------\n\n\n--------------------')
          resfilename = 'get_response_property_1.json'
          self.send_header('Content-type', 'application/json')
        elif self.path.startswith("/state"):
          logging.info('[Response for GET /state] 200 OK\n--------------------\n\n\n--------------------')
          resfilename = 'get_response_state_on.json'
          self.send_header('Content-type', 'application/json')
        elif self.path.startswith("/debug_log"):
          logging.info('[Response for GET /debug_log] 200 OK\n--------------------\n\n\n--------------------')
          resfilename = 'log.tar'
          self.send_header('Content-type', 'application/octet-stream')
        elif self.path.startswith("/logout"):
          logging.info('[Response for GET /logout] 200 OK\n--------------------\n\n\n--------------------')
          resfilename = 'get_response_logout.json'
          self.send_header('Content-type', 'text/html')
        else:
          logging.info('[Response for GET common] 200 OK\n--------------------\n\n\n--------------------')
          resfilename = 'get_response_common.json'
          self.send_header('Content-type', 'application/json')
        
        txt = os.path.join(os.path.dirname(__file__), resfilename)
        f = open(txt)
        response_body = f.read()
        
        self.send_header('Content-length', len(response_body))
        self.end_headers()
        self.wfile.write(response_body)
        
    def do_POST(self):
        #--- logging ---#
        logging.info('[Request method] POST')
        logging.info('[Request url]' + str(self.path))
        logging.info('[Request headers]\n' + str(self.headers))
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        if content_len<=1024:
          logging.info('[Request body]\n' + post_body)
        
        ### URL Routing ###
        if self.path.startswith("/service/projection"):
          logging.info('[Response for POST /service/projection] 201 Created\n--------------------\n\n\n--------------------')
          self.send_response(201)
          self.send_header('Location', 'http://localhost:80/service/projection/1')
          self.send_header('Content-type', 'application/json')
        elif self.path.startswith("/logout"):
          logging.info('[Response for POST /logout] 200 OK\n--------------------\n\n\n--------------------')
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
        elif self.path.startswith("/bmenu4"):
          logging.info('[Response for POST /bmenu4] 200 OK\n--------------------\n\n\n--------------------')
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
        else:
          logging.info('[Response for POST common] 201 Created\n--------------------\n\n\n--------------------')
          self.send_response(201)
          self.send_header('Content-type', 'application/json')
        
        self.send_header('Content-length', 0)
        self.end_headers()
        
    def do_PUT(self):
        
        #--- logging ---#
        logging.info('[Request method] PUT')
        logging.info('[Request url]' + str(self.path))
        logging.info('[Request headers]\n' + str(self.headers))
        content_len = int(self.headers.getheader('content-length', 0))
        put_body = self.rfile.read(content_len)
        if content_len<=1024:
          logging.info('[Request body]\n' + put_body)
        
        ### URL Common ###
        logging.info('[Response for PUT common] 200 OK\n--------------------\n\n\n--------------------')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-length', 0)
        self.end_headers()
        
    def do_DELETE(self):
        #--- logging ---#
        logging.info('[Request method] DELETE')
        logging.info('[Request url]' + str(self.path))
        logging.info('[Request headers]\n' + str(self.headers))
        
        ### URL Common ###
        logging.info('[Response for DELETE common] 204 No Content\n--------------------\n\n\n--------------------')
        self.send_response(204)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-length', 0)
        self.end_headers()
        


# Start the server.
script_dir = os.path.dirname(__file__)
logging.basicConfig(filename=script_dir + '/server.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

host = ''
port = 80
httpd = HTTPServer((host, port), MyHTTPRequestHandler)

logging.info('Server Starting...')
logging.info('Listening at port :%d', port)

try:
    httpd.serve_forever()
except:
    logging.info('Server Stopped')