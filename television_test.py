import pytest
from television import *

class Test:
    def setup_method(self) -> None:
        self.television = Television()

    def teardown_method(self) -> None:
        del self.television

    def test_init(self) -> None:
        """Tests the __init__ function to ensure the initial values are correct"""
        self.television.__init__()
        assert self.television.__str__() == 'Power - False, Channel - 0, Volume - 0'

    def test_power(self) -> None:
        """Tests the power function.
        Confirms that the television is turned on/off with each calling"""
        self.television.power()
        assert self.television.__str__() == 'Power - True, Channel - 0, Volume - 0'
        self.television.power()
        assert self.television.__str__() == 'Power - False, Channel - 0, Volume - 0'

    def test_mute(self) -> None:
        """Tests to ensure the mute function sets the volume to zero"""
        self.television.power()
        self.television.volume_up()
        self.television.mute()
        assert self.television.__str__() == 'Power - True, Channel - 0, Volume - 0'

    def test_channel_up(self) -> None:
        """Tests to ensure the channel_up function increases the chanel by one"""
        self.television.power()
        self.television.channel_up()
        assert self.television.__str__() == 'Power - True, Channel - 1, Volume - 0'
        self.television.channel_up()
        assert self.television.__str__() == 'Power - True, Channel - 2, Volume - 0'
        self.television.channel_up()
        self.television.channel_up()
        assert self.television.__str__() == 'Power - True, Channel - 0, Volume - 0'

    def test_channel_down(self) -> None:
        """Tests to ensure the channel_down function decreases the channel by one"""
        self.television.power()
        self.television.channel_down()
        assert self.television.__str__() == 'Power - True, Channel - 3, Volume - 0'
        self.television.channel_down()
        assert self.television.__str__() == 'Power - True, Channel - 2, Volume - 0'

    def test_volume_up(self) -> None:
        """Tests to ensure the volume_up function increases the volume by one"""
        self.television.power()
        self.television.volume_up()
        assert self.television.__str__() == 'Power - True, Channel - 0, Volume - 1'
        self.television.volume_up()
        assert self.television.__str__() == 'Power - True, Channel - 0, Volume - 2'
        self.television.volume_up()
        assert self.television.__str__() == 'Power - True, Channel - 0, Volume - 2'

    def test_volume_down(self) -> None:
        """Tests to ensure the volume_down function decreases the volume by one"""
        self.television.power()
        self.television.volume = 2
        self.television.volume_down()
        assert self.television.__str__() == 'Power - True, Channel - 0, Volume - 1'
        self.television.volume_down()
        assert self.television.__str__() == 'Power - True, Channel - 0, Volume - 0'
        self.television.volume_down()
        assert self.television.__str__() == 'Power - True, Channel - 0, Volume - 0'









