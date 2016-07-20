import uwsgi


def application(env, sr):

    if env['PATH_INFO'] == '/':
        uwsgi.websocket_handshake(env['HTTP_SEC_WEBSOCKET_KEY'], env.get('HTTP_ORIGIN', ''))
        while True:
            uwsgi.websocket_send(b"message")
            yield uwsgi.async_sleep(1)
