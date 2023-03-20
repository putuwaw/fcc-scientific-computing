import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, n):
        if n >= len(self.contents):
            return self.contents
        else:
            result = []
            while n > 0:
                length = len(self.contents) - 1
                selected = random.randint(0, length)
                result.append(self.contents.pop(selected))
                n -= 1
            return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        is_success = True
        temp = copy.deepcopy(hat)
        result = temp.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if result.count(key) < value:
                is_success = False
                break
        if is_success:
            success += 1
    return success / num_experiments
