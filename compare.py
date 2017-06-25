from PIL import Image
from PIL import ImageChops
import math, operator
import os.path

class Compare():
    countLive = []
    countDead = []
    liveMutants = []
    deadMutants = []

    def compare(self, pathOrigin, image):

        im1 = Image.open(pathOrigin + "/Images/imagem1.png")
        im2 = Image.open(image)

        result = ImageChops.difference(im1, im2).getbbox() is None

        if result is True:
            self.countLive.append(1)
            self.liveMutants.append(os.path.basename(image))
            print "VIVO VIVO VIVO",image
        else:
            self.countDead.append(1)
            self.deadMutants.append(os.path.basename(image))
            print "MORTO MORTO MORTO",image
            
        return "Number of live mutants, in others words, which don't had change in the GUI: " + str(sum(self.countLive)-1) + ".\nLive Mutants: " + str(self.liveMutants[1:]) + ".\nNumber of dead mutants, in others words, which had change in the GUI: " + str(sum(self.countDead)) + ".\nDead Mutants: " + str(self.deadMutants[0:])
