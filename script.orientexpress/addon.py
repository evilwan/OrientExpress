# Main entryoint for addon
#
# Copyright (c) 2021 Eddy Vanlerberghe.  All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of Eddy Vanlerberghe shall not be used to endorse or promote
#    products derived from this software without specific prior written
#    permission.

# THIS SOFTWARE IS PROVIDED BY EDDY VANLERBERGHE ''AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL EDDY VANLERBERGHE BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

import sys
import requests
import json

import resources.lib.kodistuff as kodi
import resources.lib.orientexpress as vpn

#
# Where to get our current publicly visible IP address info from
#
GEOLOCATION_URL = "https://ipinfo.io/json"
#
# Use application specific solution for toggling debug output
# (logging service uses a Kodi global configuration setting, we want
# something that allows debug output for this addon alone)
#
DEBUGLOG = kodi.setting("printdebug") == "true"
#
# Shortcut for printing debug logs
#
def dbg(s):
    #
    # For now, use severity "INFO" rather than "DEBUG" (which is managed
    # at global Kodi level, not just in this addon)
    #
    # kodi.debug(s)
    if DEBUGLOG:

        kodi.log(s)


#
# Give some sign of life...
#
kodi.log("Addon Id:   [{}]".format(kodi.id()))
kodi.log("Addon Name: [{}]".format(kodi.name()))
kodi.log("Version:    [{}]".format(kodi.version()))
#
# Find out what IP address we are using to access the interwebs
#
def where_am_i():
    try:
        res = requests.get(GEOLOCATION_URL, headers={"Accept": "application/json"})
        dbg("where_am_i() -- res: {}".format(res.text))
        return json.loads(res.text)
    except BaseException as err:
        dbg("where_am_i() -- caught: {}".format(err))
        return None


#
# Briefly show user where we are
#
def show_my_country():
    dbg("show_my_country() -- entered...")
    here_info = where_am_i()
    dbg("show_my_country() -- here_info={}".format(here_info))
    if here_info is not None and "country" in here_info:
        filnam = kodi.path(
            "{}{}{}".format("resources/images/", here_info["country"].lower(), ".png")
        )
        dbg("show_my_country() -- filnam={}".format(filnam))
        fmtstr = kodi.string(32008)
        dbg("show_my_country() -- fmtstr={}".format(fmtstr))
        kodi.gui_notify(
            kodi.name(),
            fmtstr.format(here_info["ip"], here_info["country"]),
            image=filnam,
        )
    dbg("show_my_country() -- done.")


#
# Disconnect from VPN
#
def disconnect_orientexpress():
    dbg("disconnect_orientexpress() -- entered")
    try:
        response = vpn.is_running()
        dbg("disconnect_orientexpress() -- response={}".format(response))
        if response:
            vpn.disconnect()
    except BaseException as err:
        dbg("disconnect_orientexpress() -- caught={}".format(err))
        kodi.gui_ok(kodi.string(32002), kodi.string(32009), err.string)


#
# Reconnect to latest used VPN exit point
#
def connect_orientexpress():
    dbg("connect_orientexpress() -- entered")

    try:
        if vpn.is_running():
            dbg("connect_orientexpress() -- vpn.is_running")
            vpn.disconnect()
        dbg("connect_orientexpress() -- (re)connecting...")
        res = vpn.connect()
        show_my_country()
    except vpn.ExpressvpnError as exception:
        dbg("connect_orientexpress() -- caught={}".format(exception))
        if exception.errno == 1:
            if kodi.gui_ask_yes_no(
                kodi.string(32000),
                kodi.string(32011),
                kodi.string(32012),
            ):
                connect_orientexpress()
        else:
            kodi.gui_ok(
                kodi.string(32000),
                kodi.string(32009),
                exception.string,
            )


#
# Show list of available VPN exit nodes and select one to connect to
#
def select_exit_node():
    dbg("select_exit_node() -- entered")
    list = vpn.get_all_exitnodes_for_display()
    choice = kodi.gui_select(kodi.string(32013), list)
    dbg("select_exit_node() -- choice={}".format(choice))
    if choice >= 0:
        node = list[choice]
        idx = node.index(" ")
        alias = node[0:idx]
        if vpn.is_running():
            vpn.disconnect()
        vpn.connect_specific(alias)
    #
    # Show current location info, regardless of fact if user selected a (new) exit node or not
    #
    show_my_country()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "select":
            select_exit_node()
        elif sys.argv[1] == "connect":
            connect_orientexpress()
        elif sys.argv[1] == "location":
            show_my_country()
        elif sys.argv[1] == "disconnect":
            disconnect_orientexpress()
        else:
            select_exit_node()
    else:
        select_exit_node()
