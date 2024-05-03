import cadquery

# Constants
decinch = 2.54

# Parameters
bodyHeight = 2 * decinch
bodyWidth = 2.49
bodyColor = (0xBB, 0x6D, 0x0A)
pinDiameter = decinch / 5
pinLength = 3.3

for pinCount in range(4, 15):
    resArray = cadquery.Assembly()
    body = cadquery.Workplane().rect(pinCount * decinch, bodyWidth).extrude(bodyHeight).fillet(.9)
    resArray.add(body, color = cadquery.Color(*(h/0xff for h in bodyColor)), name = 'body')
    pinPos = [((x - (pinCount - 1) / 2) * decinch, 0) for x in range(pinCount)]
    pins = cadquery.Workplane().pushPoints(pinPos).circle(pinDiameter/2).extrude(-pinLength)
    resArray.add(pins, color = cadquery.Color(.5, .5, .5), name = 'pins')
    resArray.save(f"../cad/resArray{pinCount}.step")
