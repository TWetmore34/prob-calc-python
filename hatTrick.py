import random

class Hat ():
    def __init__(self, **colors):
        # error handlers
        if colors == {}:
            raise ValueError('At least one Ball required')
        if 0 in colors.values():
            raise ValueError('No null entries')

        # create arr of str w colors
        self.colorObj = colors
        self.colorList = []
        for color in colors:
            for number in range(colors[color]):
                self.colorList.append(color)

    def draw(self, num):
        if num > len(self.colorList):
            return self.colorList
        
        removed = []
        # creates removed
        for x in range(num):
            popped = self.colorList.pop(random.randint(0, len(self.colorList) - 1))
            removed.append(popped)
        # resets colorList
        for x in removed:
            self.colorList.append(x)
        
        return removed

def experiment(hat, expected_balls, num_drawn, num_experiments):
    success = 0

    for x in range(num_experiments):
        result = {}
        drawn = hat.draw(num_drawn)
        for entry in drawn:
            result[entry] = result.get(entry, 0) + 1
        
        for color in expected_balls:
            reduce = result.get(color, 0)
            expected_balls[color] = expected_balls.get(color, False) - reduce

        if all(x <= 0 for x in expected_balls.values()):
            success += 1
        
        for color in expected_balls:
            reduce = result.get(color, 0)
            expected_balls[color] = expected_balls.get(color, False) + reduce
    
    return success / num_experiments

hat = Hat(blue=3, red=2, green=6)

probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "green": 1},
    num_drawn=4,
    num_experiments=1000)
print(probability)
