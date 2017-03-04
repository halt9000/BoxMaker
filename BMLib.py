from itertools import chain


#: Multiple of notch height
IDEAL_NOTCH_WIDTH = 4


def genFrontPoints(w, h, d, t, faces):
    offset = t if faces.left else 0
    if faces.bottom:
        l1 = genHorizontalLinePoints(0, t, w, -t, offset)
        offset = t
    else:
        len = w - (0 if faces.left else t) -  (0 if faces.right else t)
        l1 = genHorizontalStraightLinePoints(0, 0, len,  offset)
        offset = 0
    if faces.right:
        l2 = genVerticalLinePoints(w - t, 0, h, t, offset)
        offset = t
    else:
        l2 = genVerticalStraightLinePoints(w, 0, h, offset)
        offset = 0
    if faces.top:
        l3 = genHorizontalLinePoints(w, h - t, -w, t, -offset)
        offset = t
    else:
        len = w - (0 if faces.right else t) -  (0 if faces.left else t)
        l3 = genHorizontalStraightLinePoints(w, h, -len, -offset)
        offset = 0
    if faces.left:
        l4 = genVerticalLinePoints(t, h, -h, -t, -offset)
    else:
        len = w - (0 if faces.top else t) -  (0 if faces.bottom else t)
        l4 = genVerticalStraightLinePoints(0, h, -len, -offset)

    return chain(l1, l2, l3, l4)

def genBackPoints(w, h, d, t, faces):
    return genFrontPoints(w, h, d, t, faces)


def genLeftPoints(w, h, d, t, faces):
    if faces.bottom:
        l1 = genHorizontalLinePoints(0, t, -d, -t, 0)
        offset = t
    else:
        l1 = genHorizontalStraightLinePoints(0, 0, -d, 0)
        offset = 0
    if faces.front:
        l2 = genVerticalLinePoints(-d, 0, h, t, offset)
    else:
        len = w - (0 if faces.bottom else t) -  (0 if faces.top else t)
        l2 = genVerticalStraightLinePoints(-d, 0, len, offset)
    if faces.top:
        l3 = genHorizontalLinePoints(-d, h - t, d, t, 0)
        offset = t
    else:
        l3 =  genHorizontalStraightLinePoints(-d, h, d, 0)
        offset = 0
    if faces.back:
        l4 = genVerticalLinePoints(0, h, -h, -t, -offset)
    else:
        len = w - (0 if faces.top else t) -  (0 if faces.bottom else t)
        l4 = genVerticalStraightLinePoints(0, h, -len, -offset)
    return chain(l1, l2, l3, l4)


def genRightPoints(w, h, d, t, faces):
    return genLeftPoints(w, h, d, t, faces)


def genBottomPoints(w, h, d, t, faces):
    return genTopPoints(w, h, d, t, faces)


def genTopPoints(w, h, d, t, faces):
    if faces.back:
        l1 = genHorizontalLinePoints(0, 0, w, -t, 0)
    else:
        l1 = genHorizontalStraightLinePoints(0, 0, -w, 0)
    if faces.right:
        l2 = genVerticalLinePoints(w, 0, -d, -t, 0)
    else:
        l2 = genVerticalStraightLinePoints(w, 0, -d, 0)
    if faces.front:
        l3 = genHorizontalLinePoints(w, -d, -w, t, 0)
    else:
        l3 = genHorizontalStraightLinePoints(w, -d, -w, 0)
    if faces.left:
        l4 = genVerticalLinePoints(0, -d, d, t, 0)
    else:
        l4 = genVerticalStraightLinePoints(0, -d, d, 0)
    return chain(l1, l2, l3, l4)


def genHorizontalLinePoints(x, y, length, notchHeight, offset):
    idealNotch = abs(notchHeight) * IDEAL_NOTCH_WIDTH
    notchCount = int(abs(length) / idealNotch)
    x = float(x)
    y = float(y)
    if notchCount % 2 == 0:
        notchCount += 1

    notchWidth = length / notchCount

    # First point
    yield (x + offset, y)

    # Two points for every side of a notch
    for i in range(1, notchCount):
        x = x + notchWidth
        yield (x, y if ((i % 2) == 1) else y + notchHeight)
        yield (x, y if ((i % 2) == 0) else y + notchHeight)

    # Last point is omitted (because it will be the first point of the next side)


def genVerticalLinePoints(x, y, length, notchHeight, offset):
    # Symmetrical with the horizontal version, but with x & y swapped
    points = genHorizontalLinePoints(y, x, length, notchHeight, offset)
    for y, x in points:
        yield (x, y)


def genHorizontalStraightLinePoints(x, y, length, offset):
    x = float(x)
    y = float(y)
    yield (x + offset, y)
    yield (x + length - offset, y)


def genVerticalStraightLinePoints(x, y, length, offset):
    points = genHorizontalStraightLinePoints(y, x, length, offset)
    for y, x in points:
        yield (x, y)
