import cadquery
import math

decinch = 2.54

LED_7segments_display = cadquery.Assembly()

body = cadquery.Workplane().rect(5 * decinch, 7.5 * decinch).extrude(7.8)
LED_7segments_display.add(body, color = cadquery.Color(.99, .99, .99), name = 'body')

face = cadquery.Workplane().transformed(offset=(0,0,7.8)).rect(5 * decinch, 7.5 * decinch).extrude(.2)
LED_7segments_display.add(face, color = cadquery.Color(.4, .4, .4), name = 'face')

pinPos = [((x-2) * decinch, (y-.5)*6*decinch) for x in range(5) for y in range(2)]
pins = cadquery.Workplane().pushPoints(pinPos).circle(.5/2).extrude(-4)
LED_7segments_display.add(pins,color = cadquery.Color(.5, .5, .5),name = 'pins')

H = 14.4    # Character height
W = 8.2        # Character width, not taking skew into account
LW = 1.7     # Segment width
G = 0.4      # Gap between segments
Skew_deg = 8 # Angle of skew

Cx = W/2 - LW/2
Cy = H/2 - LW/2
A = Cx - G/2
B = W/2 - LW - G/2
skew = Cy * math.sin(math.radians(Skew_deg))

on  = cadquery.Workplane().transformed(offset=(0,0,7.9))
off = cadquery.Workplane().transformed(offset=(0,0,7.9))
on  = on.polyline([(skew-A,Cy),(skew-B,H/2),(skew+B,H/2), (skew+A,Cy),(skew+B,H/2-LW),(skew-B,H/2-LW)]).close()
on  = on.polyline([(Cx,G/2),(W/2,LW/2+G/2),(skew+W/2,H/2-LW-G/2),(skew+Cx,Cy-G/2),(skew+Cx-LW/2,Cy-LW/2-G/2),(Cx-LW/2, LW/2+G/2)]).close()
off = off.polyline([(Cx,-G/2),(W/2,-LW/2-G/2),(-skew+W/2,-H/2+LW+G/2),(-skew+Cx,-Cy+G/2),(-skew+Cx-LW/2,-Cy+LW/2+G/2),(Cx-LW/2, -LW/2-G/2)]).close()
on  = on.polyline([(-skew-A,-Cy),(-skew-B,-H/2),(-skew+B,-H/2), (-skew+A,-Cy),(-skew+B,-(H/2-LW)),(-skew-B,-(H/2-LW))]).close()
on  = on.polyline([(-Cx,-G/2),(-W/2,-LW/2-G/2),(-skew-W/2,-H/2+LW+G/2),(-skew-Cx,-Cy+G/2),(-skew-Cx+LW/2,-Cy+LW/2+G/2),(-Cx+LW/2, -LW/2-G/2)]).close()
off = off.polyline([(-Cx,G/2),(-W/2,LW/2+G/2),(skew-W/2,H/2-LW-G/2),(skew-Cx,Cy-G/2),(skew-Cx+LW/2,Cy-LW/2-G/2),(-Cx+LW/2, LW/2+G/2)]).close()
on  = on.polyline([(-A,0),(-B, LW/2),(B,LW/2),(A,0),(B,-LW/2),(-B,-LW/2)]).close()
off = off.center(W/2+skew/2,-H/2+LW/2).circle(LW/2)
on  = on.extrude(.3)
off = off.extrude(.3)

LED_7segments_display.add(on,color = cadquery.Color(.95, .3, .3),name = 'on')
LED_7segments_display.add(off,color = cadquery.Color(.7, .7, .7),name = 'off')

LED_7segments_display.save("../cad/LED7seg.step")
