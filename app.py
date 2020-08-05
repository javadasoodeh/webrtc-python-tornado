import json
import os
from abc import ABC

import tornado.ioloop
import tornado.web
import tornado.websocket

class MainHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.render("index.html")


class WebSocketSignalServer(tornado.websocket.WebSocketHandler, ABC):
    users = set()

    def open(self):
        print("open")
        self.users.add(self)

    def broadcast_message(self,msg=None, ignore_sender=True):
        for user in self.users:
            if user != self:
                user.write_message(msg)

    # called when message receive from socket
    def on_message(self, message):

        pack = json.loads(message)

        # print("message : ", message)
        # _type = msg.get('type', '')
        # _message = msg.get('message', '')
        # _room = msg.get("room", '')
        #
        # if _type == "chat":
        #     self.broadcast_message(json.dumps(msg))
        #
        # elif _type in ["user_here", "SDP", "candidate"]:
        #     pack = {'type': _type, 'message': _message, 'room': _room}
        #     self.broadcast_message(json.dumps(pack))
        self.broadcast_message(json.dumps(pack))


    def on_close(self):
        print("close")
        self.users.remove(self)

    def check_origin(self, origin):

        return True


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", WebSocketSignalServer),
    ],
        autoreload=True,
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8383)
    tornado.ioloop.IOLoop.current().start()
