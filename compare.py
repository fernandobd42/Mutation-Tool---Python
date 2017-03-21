import Image
import ImageChops
import math, operator
import os.path

class Compare():
    count = []
    mutants = []

    def compare(self, image):

        im1 = Image.open("/home/fernando/Documentos/GIT/Mutation-Tool---Python/Images/imagem1.png")
        im2 = Image.open(image)

        result = ImageChops.difference(im1, im2).getbbox() is None

        if result is True:
            self.count.append(1)
            self.mutants.append(os.path.basename(image))
        else:
            pass

        return "Quantidade de Mutantes Vivos sem alteracao na GUI: " + str(sum(self.count)-1) + ".\nEqual Mutants " + str(self.mutants[1:])
