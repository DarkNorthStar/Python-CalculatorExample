import Vector2D

class Grid:
# You probably shouldn't declare variables at the top like this in python but fk it
    # Max values
    MaxX = 0
    MaxY = 0

    MinX = 0
    MinY = 0

    __DistanceTraveled = 0

    # Current location
    # __ prefix means dont edit it manually use the function but python doesn't enforce this so you can mess things up
    __CurrentLocation = Vector2D.Vector2D(0,0)

    def __init__(self, minX, maxX, minY, maxY) -> None:
        self.MinX = minX
        self.MinY = minY
        self.MaxX = maxX
        self.MaxY = maxY

    def Move(self, movementVector):
        
        # Save old location value
        previousLocation = self.__CurrentLocation
        
        # Add to Location
        self.__CurrentLocation = self.__CurrentLocation.AddVector(movementVector)
        
        # Add to distance
        self.__DistanceTraveled = self.__DistanceTraveled + previousLocation.DistanceTo(self.__CurrentLocation)

    def GetCurrentLocation(self):
        return self.__CurrentLocation
    
    def GetDistanceTraveled(self):
        return self.__DistanceTraveled
    

        