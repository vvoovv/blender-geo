#!/usr/bin/env python3

import math

# see conversion formulas at
# http://en.wikipedia.org/wiki/Transverse_Mercator_projection
# and
# http://mathworld.wolfram.com/MercatorProjection.html
class TransverseMercator:
	radius = 6378137
	lat = 0 # in degrees
	lon = 0 # in degrees
	k = 1 # scale factor

	def __init__(self, **kwargs):
		for attr in kwargs:
			setattr(self, attr, kwargs[attr])
		self.latInRadians = math.radians(self.lat)

	def fromGeographic(self, coords):
		lat = math.radians(coords[0])
		lon = math.radians(coords[1]-self.lon)
		B = math.sin(lon) * math.cos(lat)
		x = 0.5 * self.k * self.radius * math.log((1+B)/(1-B))
		y = self.k * self.radius * ( math.atan(math.tan(lat)/math.cos(lon)) - self.latInRadians )
		return [x,y]

	def toGeographic(self, x, y):
		x = x/(self.k * self.radius)
		y = y/(self.k * self.radius)
		D = y + self.latInRadians
		lon = math.atan(math.sinh(x)/math.cos(D))
		lat = math.asin(math.sin(D)/math.cosh(x))

		lon = self.lon + math.degrees(lon)
		lat = math.degrees(lat)
		return [lat, lon]