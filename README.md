awayemail
=========

awayemail is a [python3 module](http://wiki.znc.in/Modpython) for [znc](http://wiki.znc.in/ZNC "ZNC")
which will send you missed mentions or private messages by e-mail when you are not connected.

*Note* I have decided not to finish this, as I have started using [znc-push](https://github.com/jreese/znc-push) instead.
The "difference" is that instead of going to an e-mail znc-push sends it to a notification service,
I have it setup with [PushBullet](https://www.pushbullet.com/).

If someone wants to finish this module, the only stuff that should be left to do is write the Python code to
actually send the e-mail messages.


## Installation

* You must have ZNC setup with [Modpython enabled](http://wiki.znc.in/Modpython).
* place [awayemail.py](awayemail.py) in `<ZNC DIR>/modules/` (`<ZNC DIR>` is probably `/var/lib/znc/` unless you set it elsewhere)
* enable `awayemail` module
