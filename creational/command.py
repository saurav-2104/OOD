"""
Encapsulates the request as an object, thus enables performing different acctions on the same object.
"""

import abc

"""
Use case:
A Home automation system has a remote with several slots to manage multiple appliances.
"""


class Light:
    def __init__(self, name):
        self.name = name

    def turn_off(self):
        print("Turning off the {} light".format(self.name))

    def turn_on(self):
        print("Turning on the {} light".format(self.name))


class MusicPlayer:
    def __init__(self, name):
        self.name = name

    def turn_off(self):
        print("Turning off the {} music player".format(self.name))

    def turn_on(self):
        print("Turning on the {} music player".format(self.name))


class CeilingFan:
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __init__(self, location):
        self.location = location
        self.speed = CeilingFan.OFF

    def high(self):
        print("Turning the {} fan to high".format(self.location))
        self.speed = CeilingFan.HIGH

    def medium(self):
        print("Turning the {} fan to medium".format(self.location))
        self.speed = CeilingFan.MEDIUM

    def low(self):
        print("Turning the {} fan to low".format(self.location))
        self.speed = CeilingFan.LOW

    def off(self):
        print("Turning the {} fan to off".format(self.location))
        self.speed = CeilingFan.OFF


class Command(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError

    @abc.abstractmethod
    def undo(self):
        raise NotImplementedError


class MusicOnCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.turn_on()

    def undo(self):
        self.player.turn_off()


class MusicOffCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.turn_off()

    def undo(self):
        self.player.turn_on()


class CeilingFanBaseCommand(Command):

    def __init__(self, fan):
        self.fan = fan
        self.previous_speed = None

    def execute(self):
        raise NotImplementedError

    def undo(self):
        if self.previous_speed == CeilingFan.HIGH:
            self.fan.high()
        elif self.previous_speed == CeilingFan.MEDIUM:
            self.fan.medium()
        elif self.previous_speed == CeilingFan.LOW:
            self.fan.low()
        elif self.previous_speed == CeilingFan.OFF:
            self.fan.off()


class CeilingFanHighCommand(CeilingFanBaseCommand):

    def execute(self):
        self.previous_speed = self.fan.speed
        self.fan.high()


class CeilingFanMediumCommand(CeilingFanBaseCommand):

    def execute(self):
        self.previous_speed = self.fan.speed
        self.fan.medium()


class CeilingFanLowCommand(CeilingFanBaseCommand):

    def execute(self):
        self.previous_speed = self.fan.speed
        self.fan.low()


class CeilingFanOffCommand(CeilingFanBaseCommand):

    def execute(self):
        self.previous_speed = self.fan.speed
        self.fan.off()


class LightsOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class LightsOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()


class PartyOnMacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()


class PartyOffMacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()


class RemoteControl:

    def __init__(self, slots=1):
        self.on_button_slots = [None] * slots
        self.off_button_slots = [None] * slots
        self.undo_command = None

    def set_command(self, slot_index, on_command, off_command):
        self.on_button_slots[slot_index] = on_command
        self.off_button_slots[slot_index] = off_command

    def press_on_button(self, slot_index):
        self.on_button_slots[slot_index].execute()
        self.undo_command = self.on_button_slots[slot_index]

    def press_off_button(self, slot_index):
        self.off_button_slots[slot_index].execute()
        self.undo_command = self.off_button_slots[slot_index]

    def undo_button(self):
        self.undo_command.undo()


if __name__ == '__main__':
    remote = RemoteControl(slots=5)
    kitchen = Light("Kitchen")
    fan = CeilingFan("Bathroom")
    lights_on = LightsOnCommand(kitchen)
    lights_off = LightsOffCommand(kitchen)
    fan_low = CeilingFanLowCommand(fan)
    fan_medium = CeilingFanMediumCommand(fan)
    fan_high = CeilingFanHighCommand(fan)
    fan_off = CeilingFanOffCommand(fan)
    remote.set_command(0, lights_on, lights_off)
    remote.set_command(1, fan_low, fan_off)
    remote.set_command(2, fan_medium, fan_off)
    remote.set_command(3, fan_high, fan_off)
    remote.press_on_button(0)
    remote.undo_button()
    remote.press_off_button(0)
    remote.undo_button()
    remote.press_on_button(1)
    remote.press_on_button(3)
    remote.press_on_button(2)
    remote.undo_button()
    print("--- Get ready to Party!!! ----")
    music_player = MusicPlayer("CD Player")
    music_on = MusicOnCommand(music_player)
    music_off = MusicOffCommand(music_player)
    party_on_commands = [lights_on, fan_high, music_on]
    party_off_commands = [lights_off, fan_off, music_off]
    party_on = PartyOnMacroCommand(party_on_commands)
    party_off = PartyOffMacroCommand(party_off_commands)
    remote.set_command(4, party_on, party_off)
    remote.press_on_button(4)
    remote.press_off_button(4)
