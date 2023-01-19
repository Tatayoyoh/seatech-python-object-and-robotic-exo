from controller import Robot, Motor, Camera, DistanceSensor, Keyboard

KEYBOARD_SAMPLING_PERIOD = 200
TIME_STEP = 64

class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        self.max_speed = self.getMaxVelocity()

class SeatechRobot(Robot):
    def __init__(self):
        super().__init__()
        self.__leftMotor = RobotMotor('left wheel motor')
        self.__rightMotor = RobotMotor('right wheel motor')

    def run(self):
        self.__leftMotor.setVelocity(self.max_speed)
        self.__rightMotor.setVelocity(self.max_speed)

if __name__ == '__main__':
    # create the Robot instance.
    robot = SeatechRobot()
    keyboard =  Keyboard()
    keyboard.enable(KEYBOARD_SAMPLING_PERIOD)
    while robot.step(TIME_STEP) != -1:
        if keyboard.getKey() == keyboard.UP:
            print('salut')
            robot.run()