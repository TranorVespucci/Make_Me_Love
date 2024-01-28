label scene_cynthia_introduction:

window hide
$ quick_menu = False

scene bar bright
with Dissolve(3.0)

$ renpy.pause()

$ quick_menu = True
window show

show i_cynthia blushing
with dissolve

cynthia "you made it to scene 2"

return