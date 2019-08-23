'''
Keeps track of your RAM and warns you if running 90% or more
'''

import psutil, time, datetime
while True:
	time.sleep(5)
	mem = psutil.virtual_memory()
	if mem.percent >= 85:
		print(f'LOW RAM -- {mem.percent} --  {datetime.datetime.now().strftime("%H:%M:%S")}')
	else:
		print(f'{mem.percent} -- {datetime.datetime.now().strftime("%H:%M:%S")}')