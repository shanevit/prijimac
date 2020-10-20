radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        led.plotBarGraph(
        40 - (Math.abs(radio.receivedPacket(RadioPacketProperty.SignalStrength)) - 42),
        40
        )
    } else {
        basic.showNumber(receivedNumber)
        basic.pause(500)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(8)
    basic.showArrow(ArrowNames.South)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(9)
    basic.showArrow(ArrowNames.North)
})
basic.showIcon(IconNames.Sword)
basic.pause(1000)
radio.setGroup(1)
