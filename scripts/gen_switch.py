import cadquery
import math

# Constants
decinch = 2.54

# Parameters
bodyHeight = 5 * decinch
bodyWidth = 6.6
bodyLength = 10
bodyColor = (200, 20, 20)
neckDiameter = 5.5
neckLength = 5.9
faceWidth = 7
faceThickness = 0.4
faceColor = (200, 200, 200)
facePinWidth = 1.22
facePinLength = 2.84
facePinPitch = 2 * decinch
pinLength = 3.18
pinWidth = decinch / 2
pinThickness = 0.3 * decinch
toggleDiameter = 2.67
toggleLength = 3 * decinch
toggleAngle = 12

# Computed
offset = (2 * neckLength / 3) * math.sin(math.radians(toggleAngle))

switch = cadquery.Assembly()

body = cadquery.Workplane().rect(bodyWidth, bodyLength - faceThickness / 2).extrude(bodyHeight)
body = body.faces('<Y').workplane(centerOption='CenterOfMass').circle(neckDiameter/2).extrude(neckLength)
switch.add(body, color = cadquery.Color(*(h/0xff for h in bodyColor)), name = 'body')

face = cadquery.Workplane(origin = (0, -bodyLength / 2, 0)).rect(faceWidth, faceThickness).extrude(bodyHeight)
face = face.faces('<Z').workplane().pushPoints([(s * facePinPitch / 2, 0) for s in (-1, 1)]).rect(facePinWidth, faceThickness).extrude(facePinLength)
face = face.faces('<Y').workplane().center(0,bodyHeight / 2 + offset).transformed(rotate=cadquery.Vector(toggleAngle, 0, 0)).circle(toggleDiameter / 2).extrude(neckLength + toggleLength)
switch.add(face, color = cadquery.Color(*(h/0xff for h in faceColor)), name = 'face')

switch.save(f"../cad/switch.step")
