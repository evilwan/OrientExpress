#
# Glue for Kodi specific stuff
#

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs


def itsme():
    """
    Return current addon object
    """
    return xbmcaddon.Addon()


def id():
    """
    Get localized string for integer code
    """
    return itsme().getAddonInfo("id")


def log(s):
    """
    Log a debug string
    """
    xbmc.log("~~~~~ {} -- {}".format(id(), s), xbmc.LOGINFO)


def debug(s):
    """
    Log a debug string
    """
    xbmc.log("~~~~~ {} -- {}".format(id(), s), xbmc.LOGDEBUG)


def error(s):
    """
    Log an error
    """
    xbmc.log("~~~~~ {} -- {}".format(id(), s), xbmc.LOGERROR)


def fatal(s):
    """
    Log a fatal error
    """
    xbmc.log("~~~~~ {} -- {}".format(id(), s), xbmc.LOGFATAL)


def string(id):
    """
    Get localized string for integer code
    """
    return itsme().getLocalizedString(id)


def setting(id):
    """
    Get value as a string for named setting
    """
    return itsme().getSetting(id)


def name():
    """
    Get addon name
    """
    return itsme().getAddonInfo("name")


def version():
    """
    Get addon version
    """
    return itsme().getAddonInfo("version")


def icon():
    """
    Get addon icon name
    """
    return itsme().getAddonInfo("icon")


def path(path=""):
    """
    Get addon path
    """
    return xbmcvfs.translatePath("{}{}".format(itsme().getAddonInfo("path"), path))


#
# GUI interaction stuff
#
def gui_notify(hdr, msg, tim=5000, image=""):
    """
    Show briefly a notification message
    """
    xbmc.executebuiltin('Notification({}, "{}", {}, {})'.format(hdr, msg, tim, image))


def gui_ok(hdr, l1, l2="", l3=""):
    """
    Ask user for an acknowledgement before continuing
    """
    xbmcgui.Dialog().ok(hdr, l1, l2, l3)


def gui_select(hdr, the_list):
    """
    Present user a list of choices to choose one.
    """
    return xbmcgui.Dialog().select(hdr, the_list)


def gui_ask_yes_no(hdr, l1, l2="", l3=""):
    return xbmcgui.Dialog().yesno(hdr, l1, l2, l3) == 1
