#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from gi.repository import Gtk as gtk
from gi.repository import Gdk
from gi.repository import WebKit as webkit
DEBUG = False
WEBMAIL_URL = "https://webmail.famaf.unc.edu.ar/"


class Webmail:

    def __init__(self):
        self.window = gtk.Window()
        self.window.connect ('delete_event', self.close_app)
        self.window.set_default_size(1210,600)
        
        vbox = gtk.VBox(spacing=0)
        vbox.set_border_width(0)
        
        self.scrolled_window = gtk.ScrolledWindow()
        self.webview = webkit.WebView ()
        self.webview.connect ('resource-request-starting', self.on_link_request)
        self.scrolled_window.add (self.webview)
        
        vbox.pack_start(self.scrolled_window, True, True,0)
        self.window.add(vbox)
        
        
    def load (self, url):
        self.webview.open(url)
        
    def show (self):
        self.window.show_all()
        
    def close_app(self, widget, event, data=None):
        gtk.main_quit()
        
    def on_link_request(self, view, frame, res, req, response):
        if DEBUG:
            print "link -> %s" % self.webview.get_uri()
        
if __name__ == '__main__':
    Gdk.threads_init()
    webmail = Webmail()
    webmail.load(WEBMAIL_URL)
    webmail.show()
    gtk.main()
    
