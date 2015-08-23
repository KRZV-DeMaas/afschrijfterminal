#!/usr/bin/python
from gi.repository import WebKit2
from gi.repository import Gtk

c = 0

def close(window):
        Gtk.main_quit()

def main():
        Gtk.init()

        view = WebKit2.WebView()
        view.load_uri("https://demaas.e-captain.nl/planner/planner.php")
        window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        window.fullscreen()
        window.add(view)
        window.connect("destroy", close)
        window.show_all()
        window.connect("key-press-event", onkeypress)
        window.connect("key-release-event", onkeyrelease)

        Gtk.main()

def onkeyrelease(window,ev):
    global c
    print "Rel"
    print ev.keyval
    if ev.keyval == 65507:
        c = 0

def onkeypress(window,ev):
    global c
    print ev.keyval
    if ev.keyval == 65507:
        c = 1
    if ev.keyval == 113 and c == 1:
#        window.hide_all()
        Gtk.main_quit()


main()

