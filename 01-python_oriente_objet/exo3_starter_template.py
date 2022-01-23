from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicule():
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    pass

class AerialVehicule():
    """ A vehicle made for ground fields."""
    pass

class GroundVehicule():
    """ A vehicle made for ground fields."""
    pass

class UnderseaVehicule():
    """ A vehicle made for ground fields."""
    pass

class UAV():
    """Unmanned Aerial Vehicule"""
    pass

class UUV():
    """Unmanned Undersea Vehicule"""
    pass

class UGV():
    """Unmanned Ground Vehicule"""
    pass


uav = UAV()
uav.do_something_interesting()
uav.do_something_aerial_specific()

ugv = UGV()
ugv.do_something_interesting()
ugv.do_something_ground_specific()

uuv = UUV()
uuv.do_something_interesting()
uuv.do_something_undersea_specific()

