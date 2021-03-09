# Monica Ly
# fall_greetings.py

# Problem: This program creates a greeting using graphics library
# for users to celebrate the arrival of fall/Halloween.

# Certification of Authenticity:
# I certify that this assignment is entirely my own work.
# All resources are referenced.
# xuk.people.cofc.edu/CSCI220/06_Reference/GraphicsDocumentation.pdf

from graphics import *
import time  # from HW 4 instructions


def main():
    print("Fall Greetings!")
    # set up canvas
    width, height = 900, 800
    win = GraphWin("Fall Greetings", width, height)

    # import a background
    fall_image = Image(Point(400, 400), "spooky.gif")
    fall_image.draw(win)

    # pikachu ghost
    # reference pic https://imgur.com/a/nonMUNF
    # draw the head (base)
    pika_head = Circle(Point(400, 400), 200)
    pika_head.setFill("white")
    pika_head.setOutline("white")
    pika_head.draw(win)

    # draw the rest of the body (ghost tail)
    # body inspired by Pac-Man ghosts https://imgur.com/nqZ14OY
    pika_tail = Polygon([Point(200, 407), Point(206, 656),
                         Point(288, 564)])
    pika_tail_2 = Polygon([Point(281, 556), Point(303, 668),
                         Point(350, 580)])
    pika_tail_3 = Polygon([Point(343, 589), Point(391, 670),
                           Point(460, 580)])
    pika_tail_4 = Polygon([Point(446, 588), Point(495, 670),
                           Point(519, 550)])
    pika_tail_5 = Polygon([Point(514, 557), Point(579, 664),
                           Point(600, 409)])
    # make the tail white
    pika_tail.setFill("white")
    # make the outline white
    pika_tail.setOutline("white")
    pika_tail_2.setFill("white")
    pika_tail_2.setOutline("white")
    pika_tail_3.setFill("white")
    pika_tail_3.setOutline("white")
    pika_tail_4.setFill("white")
    pika_tail_4.setOutline("white")
    pika_tail_5.setFill("white")
    pika_tail_5.setOutline("white")
    # draw the tails
    pika_tail.draw(win)
    pika_tail_2.draw(win)
    pika_tail_3.draw(win)
    pika_tail_4.draw(win)
    pika_tail_5.draw(win)

    # draw the eyes (base)
    # use black circles for the eyes
    eye_left = Circle(Point(300, 350), 40)
    eye_left.setFill("black")
    eye_left.setOutline("black")
    # make a separate copy with similar parameters
    eye_right = eye_left.clone()
    eye_right.move(200, 0)
    eye_left.draw(win)
    eye_right.draw(win)

    # draw the white of the eyes (goes on top of base)
    eye_white_left = Circle(Point(310, 340), 20)
    eye_white_left.setFill("white")
    eye_white_left.setOutline("white")
    eye_white_left.draw(win)
    eye_white_right = eye_white_left.clone()
    eye_white_right.move(180, 0)
    eye_white_right.draw(win)

    # draw the mouth (two arcs, but only have circles)
    # draw two black circles,
    # cover most of them with 2 white circles to form arc shape
    mouth_left = Circle(Point(385, 430), 20)
    mouth_left.setFill("black")
    mouth_left.setOutline("black")

    mouth_right = mouth_left.clone()
    mouth_right.move(39, 0)

    mouth_cover_left = Circle(Point(385, 420), 20)
    mouth_cover_left.setFill("white")
    mouth_cover_left.setOutline("white")
    mouth_cover_right = mouth_cover_left.clone()
    mouth_cover_right.move(39,0)

    mouth_left.draw(win)
    mouth_right.draw(win)
    mouth_cover_left.draw(win)
    mouth_cover_right.draw(win)

    # draw the nose (oval)
    # pika_nose = Oval(Point(120, 110), Point(150, 125))
    pika_nose = Oval(Point(390, 400), Point(420, 410))
    pika_nose.setFill("black")
    pika_nose.setOutline("black")
    pika_nose.draw(win)

    # draw the blush on cheeks (two circles)
    blush_left = Circle(Point(300, 450), 50)
    blush_left.setFill("red")
    blush_left.setOutline("red")
    blush_right = blush_left.clone()
    blush_right.move(210, -5)  # move up slightly
    blush_left.draw(win)
    blush_right.draw(win)

    # draw the right ear
    # use polygon
    right_ear = Polygon([Point(440, 250), Point(631, 128),
                         Point(570, 300)])
    right_ear.setFill("white")
    right_ear.setOutline("white")
    right_ear.draw(win)
    # add the black detail to right ear
    right_ear_tip = Polygon([Point(572, 165), Point(632, 126),
                             Point(610, 191)])
    right_ear_tip.setFill("black")
    right_ear_tip.setOutline("black")
    right_ear_tip.draw(win)

    # draw left ear, use polygon
    left_ear = Polygon([Point(302, 240), Point(160, 130),
                        Point(220, 330)])
    left_ear.setFill("white")
    left_ear.setOutline("white")
    left_ear.draw(win)
    # add black detail to left ear
    left_ear_tip = Polygon([Point(215, 170), Point(160, 130),
                            Point(181, 203)])
    left_ear_tip.setFill("black")
    left_ear_tip.setOutline("black")
    left_ear_tip.draw(win)

    # movement
    for j in range(3):
        for i in range(10):
            # move DOWN 15 pixels
            # have to move everything
            time.sleep(0.05)  # make animation slower
            pika_head.move(0, 15)
            pika_tail.move(0, 15), pika_tail_2.move(0, 15)
            pika_tail_3.move(0, 15), pika_tail_4.move(0, 15)
            pika_tail_5.move(0, 15)
            eye_left.move(0, 15), eye_right.move(0, 15)
            eye_white_left.move(0, 15), eye_white_right.move(0, 15)
            mouth_left.move(0, 15), mouth_right.move(0, 15)
            mouth_cover_left.move(0, 15), mouth_cover_right.move(0, 15)
            pika_nose.move(0, 15)
            blush_left.move(0, 15), blush_right.move(0, 15)
            right_ear.move(0, 15), right_ear_tip.move(0, 15)
            left_ear.move(0, 15), left_ear_tip.move(0, 15)
        for i in range(10):
            # move BACK UP 15 pixels
            time.sleep(0.05)  # make animation slower
            pika_head.move(0, -15)
            pika_tail.move(0, -15), pika_tail_2.move(0, -15)
            pika_tail_3.move(0, -15), pika_tail_4.move(0, -15)
            pika_tail_5.move(0, -15)
            eye_left.move(0, -15), eye_right.move(0, -15)
            eye_white_left.move(0, -15), eye_white_right.move(0, -15)
            mouth_left.move(0, -15), mouth_right.move(0, -15)
            mouth_cover_left.move(0, -15), mouth_cover_right.move(0, -15)
            pika_nose.move(0, -15)
            blush_left.move(0, -15), blush_right.move(0, -15)
            right_ear.move(0, -15), right_ear_tip.move(0, -15)
            left_ear.move(0, -15), left_ear_tip.move(0, -15)
    # box goes under text to make easier to see
    text_box = Rectangle(Point(290, 770), Point(610, 790))
    text_box.setFill("white")
    text_box.draw(win)
    # let user know to click to progress
    click_anywhere = Text(Point(450,780), "Click anywhere to continue")
    click_anywhere.setSize(15)
    click_anywhere.draw(win)
    # to help with getting precise points
    # click to print the clicked point
    # amount_clicks = int(input("How many points"))
    # for i in range(amount_clicks):
    #     p = win.getMouse()
    #     print(p)
    # p = win.getMouse()

    # pause
    win.getMouse()
    # draw a box under the text messages (october & halloween)
    text_box = Rectangle(Point(250, 25), Point(650, 130))
    # make the box white, but leave outline as black (default)
    text_box.setFill("white")
    text_box.draw(win)

    # message for happy thanksgiving
    fall_message = Text(Point(450, 50), "It's October!")
    fall_message.setTextColor("red")
    # change size to large
    # (36 is max "legal" according to documentation)
    fall_message.setSize(36)
    # message for Halloween, goes under fall message
    thx_message = Text(Point(450, 100), "Happy Halloween!")
    # change color to orange for Halloween
    thx_message.setTextColor("orange")
    thx_message.setStyle("italic")
    thx_message.setSize(36)
    # draw the text
    fall_message.draw(win)
    thx_message.draw(win)

    # pause
    win.getMouse()
    # change to another background
    # animate background movement coming in?
    pumpkin_image = Image(Point(500, 400), "stay-safe.gif")
    pumpkin_image.draw(win)
    # text_box_2 = text_box.clone()
    # text_box_2.draw(win)
    # click_anywhere_2 = click_anywhere.clone()
    # click_anywhere_2.draw(win)
    # instructions
    click_message = Text(Point(450, 780), "Click anywhere to continue")
    click_message.setSize(20)
    click_message.draw(win)

    # pause
    win.getMouse()
    click_message.undraw()  # gets rid of instruction message
    # text_box_2.undraw(win) # removes box
    # click_anywhere_2.undraw(win) # removes click message
    safety_message = Text(Point(450, 200), "Please stay safe")
    safety_message.setSize(36)
    # safety_message.setTextColor("white")
    safety_message.draw(win)

    # draw a box under the text message (close message)
    # text_box = Rectangle(Point(250, 750), Point(650, 790))
    # text_box.setFill("white")
    # text_box.draw(win)

    win.getMouse()
    # instructions for interaction
    close_message = Text(Point(450, 780), "Click anywhere to close")
    close_message.setSize(20)  # change size
    close_message.draw(win)
    # print(close_message.getText())
    win.getMouse()
    win.close()


main()
