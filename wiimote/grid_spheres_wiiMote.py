#!/usr/bin/env python
import vtk

from numpy import random




### wiimote stuff
#sudo modprobe uinput
#hcitool scan
# run this script, and while it executes press the red wii sync button.

#import cv
import cwiid
import time

wiimote1 = cwiid.Wiimote()
wiimote1.rpt_mode = cwiid.RPT_IR

#set an initial position
t=wiimote1.state

refPosSet = 0


global depthScalar


while refPosSet == 0:
    try:
        print 'trying'
        t=wiimote1.state
        preLed1x = t['ir_src'][0]['pos'][0]
        print preLed1x
        preLed1y = t['ir_src'][0]['pos'][1]
        print preLed1y
        preLed2x = t['ir_src'][1]['pos'][0]
        print preLed2x
        preLed2y = t['ir_src'][1]['pos'][1]
        print preLed1x, preLed1y, preLed2x, preLed2y
        print preLed1x-preLed2x, preLed1y-preLed2y

        depthScalar = preLed1x-preLed2x
        print 'got it .. starting!'
        print 'set depthScalar: ', depthScalar
        time.sleep(2)
        refPosSet = 1

    except:
        pass







# Set up the necessary points.
ren = vtk.vtkRenderer()


actors = []

dists = [0.9, 0.7,0.625,0.575, 0.525,0.5]

for i in dists:
    Pts = vtk.vtkPoints()
    print 1.0/i
    Pts.InsertNextPoint(i,1-i, 0.0)
    Pts.InsertNextPoint(1-i,1-i, 0.0)
    Pts.InsertNextPoint(1-i,i, 0.0)
    Pts.InsertNextPoint(i,i, 0.0)

    # Set up the lines that use these points.
    Lines = vtk.vtkCellArray()
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(0)
    Lines.InsertCellPoint(1)
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(1)
    Lines.InsertCellPoint(2)
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(2)
    Lines.InsertCellPoint(3)
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(3)
    Lines.InsertCellPoint(0)

    Grid = vtk.vtkPolyData()
    Grid.SetPoints(Pts)
    Grid.SetLines(Lines)
    # Set up the coordinate system.
    normCoords = vtk.vtkCoordinate()
    normCoords.SetCoordinateSystemToNormalizedViewport()

    # Set up the mapper and actor (2D) for the grid.
    mapper = vtk.vtkPolyDataMapper2D()
    mapper.SetInput(Grid)
    mapper.SetTransformCoordinate(normCoords)
    gridActor = vtk.vtkActor2D()
    gridActor.SetMapper(mapper)
    gridActor.GetProperty().SetColor(0.1, 0.1, 0.1)
    ren.AddActor(gridActor)

    #print gridActor
    
    
posns = []

for i in range(20):
    posns.append(((random.rand()-0.5)*5, (random.rand()-0.5)*5,random.rand()*5))
     
        
for thisPos in posns:

    disk = vtk.vtkSphereSource()
    disk.SetRadius(random.rand()/3.0)
    disk.SetCenter(thisPos)

    diskMapper = vtk.vtkPolyDataMapper()
    diskMapper.SetInputConnection(disk.GetOutputPort())
    diskActor = vtk.vtkActor()
    diskActor.SetMapper(diskMapper)
    # Add the actors to the renderer, set the background and size
    #
    ren.AddActor(diskActor)


    
# Create the Renderer, RenderWindow, and RenderWindowInteractor

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)


ren.SetBackground(0.5,0.5,0.5)
renWin.SetSize(500, 300)
#ren.GetActiveCamera().Reset()
cam = ren.GetActiveCamera()
cam.SetFocalPoint(0,0,-100)
cam.SetPosition(0,0,30)
cam.Modified()

def Keypress(obj, event):
    key = obj.GetKeySym()
    print cam.GetDistance()
    if key == "Right":
        cam.Azimuth(1)
        renWin.Render()
    elif key == "Left":
        cam.Azimuth(-1)
        renWin.Render()
    elif key == "Up":
        cam.Elevation(1)
        renWin.Render()
    elif key == "Down":
        cam.Elevation(-1)
        renWin.Render()            
    elif key == "comma":
        cam.Dolly(0.95)
        renWin.Render()            
    elif key == "period":
        cam.Dolly(1.05)
        renWin.Render()
    obj.SetKeySym('None') #reset


def Motion(obj, event):
    global depthScalar
    
    print 'doin motion'
    
    try:
        t=wiimote1.state
        currDepth = t['ir_src'][0]['pos'][0] - t['ir_src'][1]['pos'][0]
        print currDepth
        print 'rescale = ', currDepth/float(depthScalar)
        if currDepth < depthScalar:
            cam.Dolly(currDepth/float(depthScalar))
            renWin.Render()
            #depthScalar = currDepth     
        elif currDepth > depthScalar:
            cam.Dolly(currDepth/float(depthScalar))
            renWin.Render()
            #depthScalar = currDepth  
    except:
        pass
    
    
iren.AddObserver("KeyPressEvent", Keypress)
iren.AddObserver("TimerEvent", Motion)

iren.Initialize()
renWin.Render()
iren.CreateRepeatingTimer(200) #1000/200 times a sec
iren.Start()
