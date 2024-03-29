
# Design a parking system for a parking lot.
#  The parking lot has three kinds of parking spaces:
#  big, medium, and small, with a fixed number of slots
#  for each size.

# Implement the ParkingSystem class:

#     ParkingSystem(int big, int medium, int small)
# Initializes object of the ParkingSystem class.
# The number of slots for each parking space are
# given as part of the constructor.
#     bool addCar(int carType) Checks whether there
#  is a parking space of carType for the car that
#  wants to get into the parking lot. carType can
# be of three kinds: big, medium, or small, which
# are represented by 1, 2, and 3 respectively.
#  A car can only park in a parking space of its
# carType. If there is no space available, return
#  false, else park the car in that size space and
# return true.

#
#
#
#  Simplest Solution
# def __init__(self, big, medium, small):
#         self.A = [big, medium, small]

#     def addCar(self, carType):
#         self.A[carType - 1] -= 1
#         return self.A[carType - 1] >= 0

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.maxValues = [big, medium, small]
        self.currentValues = [0, 0, 0]

    def addCar(self, carType: int) -> bool:
        if(self.currentValues[carType-1] < self.maxValues[carType-1]):
            self.currentValues[carType-1] += 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
