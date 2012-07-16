# encoding: utf-8
"""
mprnlri.py

Created by Thomas Mangin on 2009-11-05.
Copyright (c) 2009-2012 Exa Networks. All rights reserved.
"""

from exabgp.protocol.ip.address import Address
from exabgp.message.update.attribute import AttributeID,Flag,Attribute

# =================================================================== MP NLRI (14)

class MPURNLRI (Attribute):
	FLAG = Flag.OPTIONAL
	ID = AttributeID.MP_UNREACH_NLRI
	MULTIPLE = True

	def __init__ (self,routes):
		self.routes = routes

	def pack (self,with_path_info):
		return self._attribute(self.routes[0].nlri.afi.pack() + self.routes[0].nlri.safi.pack() + ''.join([route.nlri.pack(with_path_info) for route in self.routes]))

	def __len__ (self):
		return len(self.pack())

	def __str__ (self):
		return "MP_UNREACH_NLRI Family %s %d NLRI(s)" % (Address.__str__(self.routes[0]),len(self.routes))

	def __repr__ (self):
		return str(self)
