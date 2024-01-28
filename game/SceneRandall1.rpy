label scene_randall_1:

    window hide
    $ quick_menu = False

    scene road_day
    with Fade

    $ renpy.pause()

    $ quick_menu = True
    window show