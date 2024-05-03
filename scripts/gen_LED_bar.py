import cadquery

decinch = 2.54

LEDbar10 = cadquery.Assembly()

body = cadquery.Workplane().rect(10 * decinch, 4 * decinch).extrude(7.8).pushPoints([(-5 * decinch, -2 * decinch)]).polygon(4,2).cutThruAll()
LEDbar10.add(body, color = cadquery.Color(.99, .99, .99), name = 'body')

face = cadquery.Workplane().transformed(offset=(0,0,7.8)).rect(10 * decinch, 4 * decinch).extrude(.2).pushPoints([(-5 * decinch, -2 * decinch)]).polygon(4,2).cutThruAll()
LEDbar10.add(face, color = cadquery.Color(.4, .4, .4), name = 'face')

pinGx = decinch
pinGy = 7.5
pinPos = [(x * pinGx - 9*pinGx/2,y * pinGy - pinGy/2) for y in range(2) for x in range(10)]
pins = cadquery.Workplane().pushPoints(pinPos).circle(.5/2).extrude(-4)
LEDbar10.add(pins, color = cadquery.Color(.5, .5, .5), name = 'pins')

segPos = [(x * pinGx - 9*pinGx/2,0) for x in range(10)]
segments = cadquery.Workplane().transformed(offset=(0,0,7.9)).pushPoints(segPos).rect(.7 * decinch, 2 * decinch).extrude(.3)
LEDbar10.add(segments, color = cadquery.Color(.7,.7,.7), name = 'segments')

LEDbar10.save("../cad/LED10Bar.step")
