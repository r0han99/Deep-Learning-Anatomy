#!/opt/anaconda3/bin/python
import sys
import datetime


def write_worklog(filename):
	print('log written')
	



def getepoch(objtype='default'):
	if objtype=='default':
		print('Epoch ~ ({})'.format(datetime.datetime.now()))
	else:
		print('Epoch ~ ({})'.format(datetime.datetime.now()))
		print('Decomposed Date ~  {};'.format(datetime.datetime.now().strftime("%B %d, %Y")))


if len(sys.argv) == 1:
	print('No args!')

elif sys.argv[1] == 'epochf' or sys.argv[1] == 'ef':
	getepoch(objtype = 'full')

elif sys.argv[1] == 'epoch' or sys.argv[1] == 'e':
	getepoch(objtype = 'default')


elif sys.argv[1] == 'ew' or sys.argv[1] == 'epoch-write':
	write_worklog()

elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
	print('- epochf | e for full timedelta, Decomposed Date,\n- epoch | e for only timedelta,\n- ew | epoch-write for printing the timedelta and writing the worklog,\n- -h | --help for Help.')

else:
	print('Invalid args!')










