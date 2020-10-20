def on_received_number(receivedNumber):
    if receivedNumber == 0:
        led.plot_bar_graph(86 - (abs(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)) - 42),
            86)
    else:
        basic.show_number(receivedNumber)
        basic.pause(1000)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(8)
    basic.show_arrow(ArrowNames.SOUTH)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(9)
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.SWORD)
basic.pause(1000)
radio.set_group(1)