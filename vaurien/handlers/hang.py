import gevent
from vaurien.handlers.base import BaseHandler


class Hang(BaseHandler):
    """Reads the packets that have been sent then hangs.

    Acts like a *pdb.set_trace()* you'd forgot in your code ;)
    """
    name = 'hang'
    options = {}

    def ___call__(self, client_sock, backend_sock, to_backend):
        # consume the socket and hang
        data = self._get_data(client_sock, backend_sock, to_backend)
        while data:
            data = self._get_data(client_sock, backend_sock, to_backend)

        while True:
            gevent.sleep(1.)