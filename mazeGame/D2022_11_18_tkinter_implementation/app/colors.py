class Colors: # TODO reduce colors back to RYGCBMKW, and add in FOREST and PURPLE
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)

    def __init__(self):
        pass

    def show(self):
        return self

    def get_all_clrs(self):
        return [self.BLACK, self.RED , self.YELLOW , self.GREEN , self.CYAN , self.BLUE , self.MAGENTA , self.WHITE]

    def rgb2dec(self, clr):
        return tuple(item / 255 for item in clr)

    def dec2rgb(self, clr):
        return tuple(item * 255 for item in clr)

    def rgb2hex(self, clr):
        return '#%02x%02x%02x' % clr

    def hex2rgb(self, clr):
        clr = clr.lstrip('#')
        lv = len(clr)
        return tuple(int(clr[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def rgb2cmyk(self, clr):
        R = clr[0] / 255
        G = clr[1] / 255
        B = clr[2] / 255
        K = 1 - max(R, G, B)
        C = (1 - R - K) / (1 - K)
        M = (1 - G - K) / (1 - K)
        Y = (1 - B - K) / (1 - K)
        cmyk = (C, M, Y, K)
        return cmyk

    def cmyk2rgb(self, clr):
        C = clr[0]
        M = clr[1]
        Y = clr[2]
        K = clr[3]
        R = 255 * (1 - C) * (1 - K)
        G = 255 * (1 - M) * (1 - K)
        B = 255 * (1 - Y) * (1 - K)
        rgb = (R, G, B)
        return rgb