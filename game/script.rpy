image mint LegalNotice = "images/LegalNotice.png"
image mint AgeVari = "images/AgeVar.png"
image mint brand = "images/Brand.png"
image mint table = "images/Main Menu.png"

screen age_varification :

    frame :
        at transform:
            size(400, 200)
            align (0.5, 0.7)
    vbox:
        at transform:
            align (0.5, 0.68)
        textbutton "Yes I'm 18":
            xalign 0.5
            yalign 0.0
            action [Jump("Single_Entry_Interface")]

        textbutton  "No I'm not":
            xalign 0.5
            yalign 1.0
            action Function(renpy.quit)

label start:

    scene mint brand
    with long_fade
    pause(2.0)

    scene mint LegalNotice
    with medium_fade
    pause

    show mint AgeVari
    with medium_fade
    pause

    call screen age_varification

label Single_Entry_Interface:

    scene mint table
    with long_fade
    call screen Books
    return
