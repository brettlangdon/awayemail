import re
import time

import znc

email_regex = re.compile(r'^[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$')
space_regex = re.compile(r'\s+')


class emailtimer(znc.Timer):
    def RunJob(self):
        pass


class awayemail(znc.Module):
    description = "Send mentions and private messages to e-mail when your away"
    module_types = [znc.CModInfo.UserModule]

    def OnLoad(self, args, message):
        args = space_regex.split(args)
        self.interval = 60

        # make sure we have at least 1 arg
        if not args:
            message = 'Must provide arguments: <email:required> <interval:default=60 sec>'
            return False
        # make sure first arg is an e-mail address
        if not email_regex.match(args[0]):
            message = 'Invalid E-Mail Address: %s' % args
            return False
        # is we have a second argument, make sure it is a digit
        if len(args) >= 2:
            if not args[1].isdigit():
                message = 'Interval must be a digit not %s' % args[1]
                return False
            self.interval = int(args[1])

        self.email = args
        self.timer = znc.CreateTimer(emailtimer, interval=self.interval, cycles=0)
        self.timer.msg = ''
        return True

    def _queue_msg(self, channel, nick, message):
        user = self.GetUser()
        # is there is no message then we probably
        if self.timer.msg:
            self.timer.msg += '\r\n'
        ts_format = user.GetTimestampFormat()
        now = time.time()
        self.timer.msg += '[%s] %s %s: %s' % (time.strftime(ts_format, now),
                                              channel, nick, message)

    def OnPrivMsg(self, nick, message):
        user = self.GetUser()

        # private message and user is not connected
        if not user.IsUserAttached():
            self._queue_msg('PRIVMSG', nick, message)
        return znc.CONTINUE

    def OnChanMsg(self, nick, channel, message):
        user = self.GetUser()
        if not user.IsUserAttached():
            # user is not connected and user was mentioned
            if user.GetNick().lower() in message.lower():
                self._queue_msg(channel, nick, message)
        return znc.CONTINUE
