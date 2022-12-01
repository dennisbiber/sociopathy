from Undefinites.helperFunctions import B4NG, ParticlePlay, FusionParticles


__author__ = "Dennis Biber <decibelsTechnology>"

def Thread(target, args: set(), returnThread = False, acclerate = False):
    if returnThread:
        return target(target=target, args=args)
    target(target=target, args=args)

def doThatDangThingProcessor(first: bool ,thread):
    if first:
        thread.start(thread)

def Socialize(Particle):
    doThatDangThingProcessor(True, Thread())

def main():
    print(__file__)
    import sys
    # ParticlePlay()

    FusionParticles()

    # if sys.argv[-1] != __file__.split("/")[-1]:
    #     BigBang = B4NG(timeValue = float(sys.argv[-1]))
    # elif sys.argv[(sys.argv).index(__file__) + 1] == "--accel" and type(sys.argv[-1]) == float:
    #     BigBang = B4NG(timeValue = float(sys.argv[-1], accelerate = True))
    # elif len(sys.argv) > 1:
    #     BigBang = B4NG(spinAlteration = sys.argv[-2], timeValue = float(sys.argv[-1]))
    # else:
    #     BigBang = B4NG()

    # print(BigBang)
    # BigBang.spinForward()


if __name__ == "__main__":
    main()