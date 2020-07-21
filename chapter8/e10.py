from typing import List


class Image(list):
    def __repr__(self):
        r = ""
        for row in self:
            row = [str(x) for x in row]
            r += "".join(row) + "\n"

        return r
    

class Painter:
    image: Image

    def __init__(self, image: Image):
        self.image = image

    def fill(self, color, x, y):
        if self.image[y][x] == color:
            return

        self.image[y][x] = color
        print(self.image)

        if y > 0 and self.image[y-1][x] != color:
            self.fill(color, x, y-1)
        if x > 0 and self.image[y][x-1] != color:
            self.fill(color, x-1, y)
        if y < (len(self.image) - 1) and self.image[y+1][x] != color:
            self.fill(color, x, y+1)
        if x < (len(self.image[0]) - 1) and self.image[y][x+1] != color:
            self.fill(color, x+1, y)


if __name__ == '__main__':
    painter = Painter(Image([
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1],
    ]))
    painter.fill(color=0, x=4, y=6)

    assert painter.image == Image([
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
    ])
