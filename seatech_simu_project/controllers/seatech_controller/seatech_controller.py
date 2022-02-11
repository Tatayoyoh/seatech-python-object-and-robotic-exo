from controller import Robot, Motor, Camera, DistanceSensor, Keyboard

class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

class SeatechRobot(Robot):
    def __init__(self):
        super().__init__()
        self.__leftMotor = RobotMotor('left wheel motor')
        self.__rightMotor = RobotMotor('right wheel motor')

    def run(self):
        self.__leftMotor.setVelocity(MAX_SPEED)
        self.__rightMotor.setVelocity(MAX_SPEED)

if __name__ == '__main__':
    TIME_STEP = 64
    MAX_SPEED = 6.28
    # create the Robot instance.
    robot = SeatechRobot()
    keyboard =  Keyboard()
    keyboard.enable(samplingPeriod=100)
    robot.run()
    while robot.step(TIME_STEP) != -1:
        if keyboard.getKey() == keyboard.UP:
            print('salut')