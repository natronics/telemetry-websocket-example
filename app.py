import uwsgi
import json
import time


def application(env, sr):

    if env['PATH_INFO'] == '/':
        uwsgi.websocket_handshake(env['HTTP_SEC_WEBSOCKET_KEY'], env.get('HTTP_ORIGIN', ''))
        describe = json.dumps({
            'describe': {
                'stream': {
                    'timestamp': {'label': "Server Timestamp", 'units': "s"}
                }
            }
        })
        uwsgi.websocket_send(describe.encode('utf-8'))
        while True:
            message = json.dumps({'timestamp': time.time()})
            uwsgi.websocket_send(message.encode('utf-8'))
            yield uwsgi.async_sleep(1)
