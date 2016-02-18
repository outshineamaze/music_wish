# -*- coding: utf-8 -*-

# from qiniu import Auth
# # Create your tests here.
# q = Auth('ToNLYIGLfHy5tpKSsRcBV2pw18b20LrYuBdvHaA_', 'rrD25c6RoHoMajmLR8lSz9wW4FcGEHvGMDL4l2zV')
# print q
# token = q.upload_token('outshineamazing', 'outshine')
# print token

if __name__ == '__main__':


	e='\u559c\u6b22\u4e00\u4e2a\u4eba'
	print type(e)
	print type(e.decode("utf-8"))
	print type(e.decode("raw_unicode_escape").encode("utf-8"))
	print type(e.decode("raw_unicode_escape"))
	x = '\xe4\xbd\xa0'
	print repr(x)