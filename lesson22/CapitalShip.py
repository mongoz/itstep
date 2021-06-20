class CapitalShip:
    _counter = 0
    def __init__(self,
                 name,
                 maximum_speed,
                 length,
                 capacity,
                 health_point,
                 power
                 ):
        self.id = CapitalShip._counter
        self.name = name + ' ' + str(self.id)
        self.maximum_speed = maximum_speed
        self.length = length
        self.capacity = capacity
        self.health_point = health_point
        self.power = power
        self.form = name + '.png'
        self.available = True
        CapitalShip._counter += 1
        __init__(self)

    def damage(self, damage) -> bool:
        '''
        Takes life from the enemy and returns True if he died.
        '''
        if damage < self.health_point:
            self.health_point -= damage
            return False
        else:
            self.health_point = 0
            self.kill()
            return True