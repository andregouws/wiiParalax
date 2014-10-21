#sudo modprobe uinput
#hcitool scan

import cv
import cwiid
import time

wiimote1 = cwiid.Wiimote()
#wiimote2 = cwiid.Wiimote()


wiimote1.rpt_mode = cwiid.RPT_IR
#wiimote2.rpt_mode = cwiid.RPT_IR
print wiimote1.state
#print wiimote2.state

cam1_x1 = []
cam1_y1 = []
cam1_x2 = []
cam1_y2 = []
cam1_x3 = []
cam1_y3 = []
cam1_x4 = []
cam1_y4 = []

cam2_x1 = []
cam2_y1 = []
cam2_x2 = []
cam2_y2 = []
cam2_x3 = []
cam2_y3 = []
cam2_x4 = []
cam2_y4 = []

#for i in range(100):
while True:
    time.sleep(0.1)
    print 'getting data'
    try:
	t=wiimote1.state
	#print t
	#print t['ir_src'][0]['pos'], t['ir_src'][1]['pos'], t['ir_src'][2]['pos'], t['ir_src'][3]['pos']
	print t['ir_src'][0]['pos'], t['ir_src'][1]['pos']
	print (t['ir_src'][0]['pos'][0] - t['ir_src'][1]['pos'][0], t['ir_src'][0]['pos'][1] - t['ir_src'][1]['pos'][1])
	#cam1_x1.append(t['ir_src'][0]['pos'][0])
	#cam1_y1.append(t['ir_src'][0]['pos'][1])
	#cam1_x2.append(t['ir_src'][1]['pos'][0])
	#cam1_y2.append(t['ir_src'][1]['pos'][1])
	#cam1_x3.append(t['ir_src'][2]['pos'][0])
	#cam1_y3.append(t['ir_src'][2]['pos'][1])
	#cam1_x4.append(t['ir_src'][3]['pos'][0])
	#cam1_y4.append(t['ir_src'][3]['pos'][1])
	#t=wiimote2.state
	#print t
	#cam2_x1.append(t['ir_src'][0]['pos'][0])
	#cam2_y1.append(t['ir_src'][0]['pos'][1])
	#cam2_x2.append(t['ir_src'][1]['pos'][0])
	#cam2_y2.append(t['ir_src'][1]['pos'][1])
	#cam2_x3.append(t['ir_src'][2]['pos'][0])
	#cam2_y3.append(t['ir_src'][2]['pos'][1])
	#cam2_x4.append(t['ir_src'][3]['pos'][0])
	#cam2_y4.append(t['ir_src'][3]['pos'][1])
	time.sleep(0.1)
    except:
	pass



