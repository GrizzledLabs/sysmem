'''
Keeps track of your RAM and warns you if running 90% or more
'''

import psutil, time, datetime
while True:
	time.sleep(2)
	mem = psutil.virtual_memory()
	if mem.percent > 90:
		print(f'LOW RAM -- {mem.percent} --  {datetime.datetime.now().strftime("%H:%M:%S")}')
	else:
		print(f'{mem.percent} -- {datetime.datetime.now().strftime("%H:%M:%S")}')