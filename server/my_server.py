import socket
import json
import RPC.server.callable as Call
import RPC.server.response as Response
import os

class MyServer:

    def __init__(self):
        # create socket
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

        # configure server address
        server_address = ''

        # bing socket to address
        sock.bing(server_address)

        self.socket = sock

    def start(self):
        
        #listen
        socket.listen(1)

        while True:
            conn, client_address = socket.accept()
            self.connList.push(conn)

            try:
                while True:

                    data = conn.recv(32)

                    data_str = data.Decode('utf-8')
                    print(data_str)

                    if data:
                        #parse json to dict
                        json_dict = json.loads(data_str)

                        method = json_dict.method
                        params = json_dict.params

                        try:
                            result = Call.callable_map[method](params)
                            resp = Response(result, None)
                            resp_json = resp.to_json()
                            conn.sendall(resp_json.encode())

                        except Exception as e:
                            resp = Response(None, e)
                            resp_json = resp.to_json()
                            conn.sendall(resp_json.encode())
                    
                    else:
                        break

            finally:
                conn.close()



                    
