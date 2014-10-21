#!/usr/bin/env python

# This example demonstrates the use of multiline 2D text using
# vtkTextMappers.  It shows several justifications as well as
# single-line and multiple-line text inputs.

import vtk

from numpy import random


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

iren.AddObserver("KeyPressEvent", Keypress)

iren.Initialize()
renWin.Render()
iren.Start()
