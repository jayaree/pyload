#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#   Copyright(c) 2008-2012 pyLoad Team
#   http://www.pyload.org
#
#   This file is part of pyLoad.
#   pyLoad is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   Subjected to the terms and conditions in LICENSE
#
#   @author: RaNaN
###############################################################################

from mod_pywebsocket.msgutil import receive_message, send_message

class EventHandler:

    def __init__(self, api):
        self.api = api

    def do_extra_handshake(self, req):
        pass

    def transfer_data(self, req):

        while True:
            try:
                line = receive_message(req)
            except TypeError: # connection closed
                return

            print "Got", line
            send_message(req, "You send: %s" % line)

    def passive_closing_handshake(self, req):
        print "Closed", req