# https://github.com/aslushnikov/getting-started-with-cdp
import json, websocket

class WebsocketConnection():

    def __init__(self, port):
        try:
            import thread
        except ImportError:
            import _thread as thread

        import time

        def on_message(ws, message):
            print(message)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")

        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close

    def connect(self, _ws):
        print("Connecting to ws on " + _ws)
        def on_open(ws):
            def run(*args):
                print("hallo")
                x = json.dumps({
                    "id": 1,
                    'method': 'Target.setDiscoverTargets',
                    'params': {
                      'discover': True
                    },
                }, separators=(',', ':'))
                print(x)
                ws.send(x)
            run()

        self.on_open = on_open
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(_ws,
                                  on_message = self.on_message,
                                  on_error = self.on_error,
                                  on_close = self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()
