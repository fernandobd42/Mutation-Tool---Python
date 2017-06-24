from PIL import Image
from PIL import ImageChops
import math, operator
import os.path

class Compare():
    count = []
    mutants = []

    def compare(self, pathOrigin, image):

        im1 = Image.open(pathOrigin + "/Images/imagem1.png")
        im2 = Image.open(image)

        result = ImageChops.difference(im1, im2).getbbox() is None

        if result is True:
            self.count.append(1)
            self.mutants.append(os.path.basename(image))
        else:
            pass

        return "Number of muntants live without change in the GUI: " + str(sum(self.count)-1) + ".\nEqual Mutants " + str(self.mutants[1:])
