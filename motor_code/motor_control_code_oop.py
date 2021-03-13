class Wheels(RPi.GPIO):
    def __init__(self,inx,iny):
        setmode(BOARD)
        self.inx=setup(inx,OUT)
        self.iny=setup(iny,OUT)
    
    def control(self,o1,o2)
        output(self.inx,o1)
        output(self.iny,o2)

    def hault(self):
        self.inx.cleanup()
        self.iny.cleanup()

        
        
