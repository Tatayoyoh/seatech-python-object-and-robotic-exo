from abc import ABCMeta, abstractmethod

# You can use classes below or create your own 👍️

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """

class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

class UAV():
    """Unmanned Aerial Vehicle"""

class UUV():
    """Unmanned Undersea Vehicle"""

class UGV():
    """Unmanned Ground Vehicle"""


if __name__ == '__main__':
    uav = UAV()
    uav.do_something_interesting()
    uav.do_something_aerial_specific()

    ugv = UGV()
    ugv.do_something_interesting()
    ugv.do_something_ground_specific()

    uuv = UUV()
    uuv.do_something_interesting()
    uuv.do_something_undersea_specific()

