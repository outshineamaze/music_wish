# -*- coding: utf-8 -*-

from qiniu import Auth
# Create your tests here.
q = Auth('ToNLYIGLfHy5tpKSsRcBV2pw18b20LrYuBdvHaA_', 'rrD25c6RoHoMajmLR8lSz9wW4FcGEHvGMDL4l2zV')
print q
token = q.upload_token('outshineamazing', 'outshine')
print token