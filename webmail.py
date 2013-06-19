#!/usr/bin/env python
#-*- coding:utf-8 -*-

import config
import sys
from gi.repository import Gtk as gtk
from gi.repository import Gdk
from gi.repository import WebKit as webkit

WEBMAIL_URL = "https://webmail.famaf.unc.edu.ar/"

def log (string):
    if DEBUG:
        print string

def usage():
    print """
    Usage: webmail [options]
    Where the options are:
        -h, --help      Print this help
        -d, --debug     Turn on the debug
        -a, --account   create a new account for an automatic login.
        
    The account option must be:
        -a username/password
        --account=username/password"""

class Webmail:

    def __init__(self):
        self.window = gtk.Window()
        self.window.connect ('delete_event', self.close_app)
        
        # Some settings
        self.window.set_icon_from_file("/usr/share/pixmaps/famaf-webmail.png")
        self.window.set_title("Webmail FaMAF")
        self.window.set_default_size(1210,600)
        
        vbox = gtk.VBox(spacing=0)
        vbox.set_border_width(0)
        
        self.scrolled_window = gtk.ScrolledWindow()
        self.webview = webkit.WebView ()
        self.webview.connect ('load-finished', self._exec_login_script)
        self.scrolled_window.add (self.webview)
        
        vbox.pack_start(self.scrolled_window, True, True,0)
        self.window.add(vbox)

        self.status_icon = gtk.StatusIcon()
        self.status_icon.set_from_file ("/usr/share/pixmaps/famaf-webmail.png")
        self.status_icon.connect ('popup-menu', self._status_icon_right_click)
        self.status_icon.connect ('activate', self._status_icon_left_click)

        self._start_cache()

    def _start_cache(self):
        webkit.set_cache_model(webkit.CacheModel.WEB_BROWSER)
        log ("Cache model changed")
        
    def _exec_login_script(self, widget, event, data=None):
        if self.webview.get_uri() == WEBMAIL_URL:
            if config.exists_config_file ():
                data = config.get_user_data ()
                self.webview.execute_script (""" 
                    $(document).ready(function (){
                        var usr = $("#rcmloginuser");
                        var pwd = $("#rcmloginpwd");

						if ( usr != '' && pwd != '' )
						{
							usr.val("%s");
							pwd.val("%s");

                            $("form").submit();
						}
                    });""" % data)
                log ("Exito!")
            else:
                log ("No existe el archivo de configuracion")
        else:
            log ("No estamos en la pagina de inicio")
                
        
    def load (self, url):
        self.webview.open(url)
        
    def show (self):
        self.window.show_all()
        
    def close_app(self, widget, event, data=None):
        self.window.hide_on_delete()
        return True

    def _status_icon_right_click (self, icon, button, time):
        self.menu = gtk.Menu()

        quit = gtk.MenuItem()
        quit.set_label("Quit")

        quit.connect("activate", gtk.main_quit)

        self.menu.append(quit)

        self.menu.show_all()

        def pos (menu, icon):
            return (gtk.StatusIcon.position_menu(menu, icon))
        self.menu.popup (None, None, pos, self.status_icon, button, time)

    def _status_icon_left_click (self, widget):
        if self.window.get_visible():
            self.window.hide()
        else:
            self.window.show_all()
        return True

if __name__ == '__main__':
    DEBUG = False
    
            
    Gdk.threads_init()
    webmail = Webmail()
    webmail.load(WEBMAIL_URL)
    webmail.show()
    gtk.main()
    
