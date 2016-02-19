# -*- coding: utf-8 -*-
import logging


class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width


s = Screen()

s.width = 1024
s.height = 768

print("s : %s : %s" % (s.width, s.height))
print("resolution: %d" % s.resolution)

try:
    pass
except:
    pass
finally:
    pass


logging.exception()