class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        """Creates the class variables and sets their default values"""
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL

    def power(self) -> None:
        """Checks whether the TV is on or off and changes its status to the opposite"""
        self.status = not self.status

    def mute(self) -> None:
        """Checks whether the TV is muted or not muted.
        If it's muted, this function wll unmute it and set it to its original volume.
        If it's not muted, then it sets the volume to zero"""

        if self.status == False:
            pass
        else:
            original_volume = self.volume
            self.muted = not self.muted
            if self.muted == False:
                self.volume = original_volume
            else:
                self.volume = self.MIN_VOLUME

    def channel_up(self) -> None:
        """Increases the channel number by one.
        If the TV is already at the maximum channel, it changes to the minimum channel"""

        if self.status == False:
            pass
        else:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self) -> None:
        """Decreases the channel number by pne.
        If the TV is already at the minimum channel, it changes to the maximum channel"""

        if self.status == False:
            pass
        else:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self) -> None:
        """Increases the volume by one.
        If the volume is already at the maximum volume, it remains the same
        It also unmutes the TV if it is muted"""

        if self.status == False:
            pass
        else:
            if self.muted == True:
                self.muted = False
                self.volume = 2
            else:
                if self.volume == self.MAX_VOLUME:
                    pass
                else:
                    self.volume += 1

    def volume_down(self) -> None:
        """Decreases the volume by one.
        If the volume is already at the minimum volume, it remains the same
        It also unmutes the TV if it is muted"""

        if self.status == False:
            pass
        else:
            if self.muted == True:
                self.muted = False
                self.volume = 1
            else:
                if self.volume == self.MIN_VOLUME:
                    pass
                else:
                    self.volume -= 1

    def __str__(self) -> str:
        return f'Power - {self.status}, Channel - {self.channel}, Volume - {self.volume}'
