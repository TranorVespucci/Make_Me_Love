style the_bars:
    right_bar "bar empty idle.png"
    xysize (200, 25)



screen bars:
    bar:
        bar_vertical True
        value romance_points
        range 10
        xalign 0.25
        yalign 0.5
        xysize(25,200)

    
    bar:
        style "the_bars"
        value romance_points
        range 10
        left_bar "bar full idle.png"
        xalign 0.5