# -*- coding: utf-8 -*-


L = ['Hello', 'World', 18, 'Apple', None]

m = [s.lower() for s in L if isinstance(s, str) ]

print(m)

