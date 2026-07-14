class circle:
    def draw(self):
        print("drawing circle")

class rectangle:
    def draw(self):
        print("drawing rectangle")
class square:
    def draw(self):
        print("drawing square")
shapes=[circle(),rectangle()]
for shape in shapes:
    shape.draw()