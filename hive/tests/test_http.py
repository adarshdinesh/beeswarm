# Copyright (C) 2012 Aniket Panse <contact@aniketpanse.in
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gevent.monkey
gevent.monkey.patch_all()


from gevent.server import StreamServer
from hive.helpers.common import create_socket
from hive.capabilities import http


import unittest
import httplib

class HTTP_Test(unittest.TestCase):
    def test_connection(self):
        """ Tests if the capability is up, and sending
            HTTP 401 (Unauthorized) headers.
        """
        sessions = {}
        cap = http.http(sessions, {'enabled': 'True', 'port': 8080})
        socket = create_socket(("0.0.0.0", 8080))
        srv = StreamServer(socket, cap.handle_session)
        srv.start()

        client = httplib.HTTPConnection('127.0.0.1', 8080)
        client.request("GET", "/")
        response = client.getresponse()
        self.assertEquals(response.status, 401)
        
if __name__ == '__main__':
    unittest.main()
