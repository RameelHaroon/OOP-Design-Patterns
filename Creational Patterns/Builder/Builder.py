class Computer:

    def __init__(self, ComputerBuilder):
        self.RAM = ComputerBuilder.RAM
        self.HDD = ComputerBuilder.HDD
        self.SSD = ComputerBuilder.SSD
        self.GPU = ComputerBuilder.GPU
        self.CPU = ComputerBuilder.CPU


    def getRAM(self):
        return self.RAM
    
    def getHDD(self):
        return self.HDD
    
    def getSSD(self):
        return self.SSD
    
    def getGPU(self):
        return self.GPU
    
    def getCPU(self):
        return self.CPU
    
    def print_specs(self):
        print("Specs for this computer")
        print("RAM" + self.RAM)
        print("HDD" + self.HDD)
        print("SSD" + self.SSD)
        print("GPU" + self.GPU)
        print("CPU" + self.CPU)
    
class ComputerBuilder:
    
    def __init__(self):
        self.RAM = None
        self.HDD = None
        self.SSD = None
        self.GPU = None
        self.CPU = None

    def setRAM(self, RAM):
        self.RAM = RAM
        return self
    
    def setHDD(self, HDD):
        self.HDD = HDD
        return self
    
    def setSSD(self, SSD):
        self.SSD = SSD
        return self
    
    def setGPU(self, GPU):
        self.GPU = GPU
        return self
    
    def setCPU(self, CPU):
        self.CPU = CPU
        return self
    
    def build(self):
        return Computer(self)

def main():
    
    builder = ComputerBuilder()
    computer = builder.setRAM("16GB").setHDD("1TB").setSSD("512GB").setGPU("NVIDIA RTX 3080").setCPU("Intel i7").build()
    computer.print_specs()


if __name__=="__main__":
    main()