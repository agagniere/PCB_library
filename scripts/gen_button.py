import cadquery
import math

# Constants
decinch = 2.54

# Parameters
bodyHeight = 8.13
bodyWidth = 2 * decinch
bodyLength = 2 * decinch + 4.01
bodyColor = (200, 20, 20)
neckDiameter = bodyWidth
neckLength = 5.59
faceThickness = 0.1
faceColor = (200, 200, 200)
pinLength = 4
pinWidth = 0.8
pinThickness = 0.5
pinPitch = 2 * decinch
pinColor = (200, 150, 60)
toggleDiameter = decinch
toggleLength = 3.53
toggleColor = (20, 20, 20)

button = cadquery.Assembly()

body = cadquery.Workplane().center(0, -bodyLength / 2).rect(bodyWidth, bodyLength).extrude(bodyHeight)
button.add(body, color = cadquery.Color(*(h/0xff for h in bodyColor)), name = 'body')

face = cadquery.Workplane(origin = (0, -bodyLength, 0)).rect(bodyWidth, faceThickness).extrude(bodyHeight)
face = face.faces('<Y').workplane().center(0,bodyHeight / 2).circle(neckDiameter / 2).extrude(neckLength)
button.add(face, color = cadquery.Color(*(h/0xff for h in faceColor)), name = 'face')

pins = cadquery.Workplane().pushPoints([(0, i * pinPitch) for i in range(-1, 2)]).rect(pinWidth, pinThickness).extrude(-pinLength)
button.add(pins, color = cadquery.Color(*(h/0xff for h in pinColor)), name = 'pins')

toggle = cadquery.Workplane("XZ", origin = (0, -bodyLength - neckLength, bodyHeight / 2)).circle(toggleDiameter / 2).extrude(toggleLength)
button.add(toggle, color = cadquery.Color(*(h/0xff for h in toggleColor)), name = 'toggle')

button.save(f"../cad/button.step")
