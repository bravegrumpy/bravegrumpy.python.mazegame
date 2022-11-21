class Colors: # TODO reduce colors back to RYGCBMKW, and add in FOREST and PURPLE
    R = (255, 0, 0)
    RRY = (255, 63, 0)
    RY = (255, 127, 0)
    RYY = (255, 191, 0)
    Y = (255, 255, 0)
    YYG = (191, 255, 0)
    YG = (127, 255, 0)
    YGG = (63, 255, 0)
    G = (0, 255, 0)
    GGC = (0, 255, 63)
    GC = (0, 255, 127)
    GCC = (0, 255, 191)
    C = (0, 255, 255)
    CCB = (0, 191, 255)
    CB = (0, 127, 255)
    CBB = (0, 63, 255)
    B = (0, 0, 255)
    BBM = (63, 0, 255)
    BM = (127, 0, 255)
    BMM = (191, 0, 255)
    M = (255, 0, 255)
    MMR = (255, 0, 191)
    MR = (255, 0, 127)
    MRR = (255, 0, 63)
    W = (255, 255, 255)
    WWK = (191, 191, 191)
    WK = (127, 127, 127)
    WKK = (63, 63, 63)
    K = (0, 0, 0)

    def __init__(self):
        pass

    def show(self):
        return self

    def get_all_clrs(self): #TODO simplify
        K = [self.W, self.WWK, self.WK, self.WKK, self.K]
        R = [self.R, self.RRY, self.RY, self.RYY]
        Y = [self.Y, self.YYG, self.YG, self.YGG]
        G = [self.G, self.GGC, self.GC, self.GCC]
        C = [self.C, self.CCB, self.CB, self.CBB]
        B = [self.B, self.BBM, self.BM, self.BMM]
        M = [self.M, self.MMR, self.MR, self.MRR]

        return K + R + Y + G + C + B + M

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