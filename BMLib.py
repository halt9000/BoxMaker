from itertools import chain
from collections import namedtuple

FaceSelection = namedtuple("FaceSelection", "front back left right bottom top")
FaceClearance = namedtuple("FaceClearance", "front back left right bottom top")

#: Multiple of notch height
IDEAL_NOTCH_WIDTH = 4


def genFrontPoints(w, h, d, t, faces, clearances):
    offset = t if faces.left else 0
    if faces.bottom:
        l1 = genHorizontalLinePoints(0, t, w, -t, offset, True, clearances.front)
        offset = t
    else:
        len = w - (0 if faces.left else t) -  (0 if faces.right else t)
        l1 = genHorizontalStraightLinePoints(0, 0, len,  offset)
        offset = 0
    if faces.right:
        l2 = genVerticalLinePoints(w - t, 0, h, t, offset, True, clearances.front)
        offset = t
    else:
        l2 = genVerticalStraightLinePoints(w, 0, h, offset)
        offset = 0
    if faces.top:
        l3 = genHorizontalLinePoints(w, h - t, -w, t, -offset, True, clearances.front)
        offset = t
    else:
        len = w - (0 if faces.right else t) -  (0 if faces.left else t)
        l3 = genHorizontalStraightLinePoints(w, h, -len, -offset)
        offset = 0
    if faces.left:
        l4 = genVerticalLinePoints(t, h, -h, -t, -offset, True, clearances.front)
    else:
        len = w - (0 if faces.top else t) -  (0 if faces.bottom else t)
        l4 = genVerticalStraightLinePoints(0, h, -len, -offset)

    return chain(l1, l2, l3, l4)

def genBackPoints(w, h, d, t, faces, clearances):
    return genFrontPoints(w, h, d, t, faces, clearances)


def genLeftPoints(w, h, d, t, faces, clearances):
    if faces.bottom:
        l1 = genHorizontalLinePoints(0, t, -d, -t, 0, True, clearances.left)
        offset = t
    else:
        l1 = genHorizontalStraightLinePoints(0, 0, -d, 0)
        offset = 0
    if faces.front:
        l2 = genVerticalLinePoints(-d, 0, h, t, offset, False, clearances.left)
    else:
        len = w - (0 if faces.bottom else t) -  (0 if faces.top else t)
        l2 = genVerticalStraightLinePoints(-d, 0, len, offset)
    if faces.top:
        l3 = genHorizontalLinePoints(-d, h - t, d, t, 0, True, clearances.left)
        offset = t
    else:
        l3 =  genHorizontalStraightLinePoints(-d, h, d, 0)
        offset = 0
    if faces.back:
        l4 = genVerticalLinePoints(0, h, -h, -t, -offset, False, clearances.left)
    else:
        len = w - (0 if faces.top else t) -  (0 if faces.bottom else t)
        l4 = genVerticalStraightLinePoints(0, h, -len, -offset)
    return chain(l1, l2, l3, l4)


def genRightPoints(w, h, d, t, faces, clearances):
    return genLeftPoints(w, h, d, t, faces, clearances)


def genBottomPoints(w, h, d, t, faces, clearances):
    return genTopPoints(w, h, d, t, faces, clearances)


def genTopPoints(w, h, d, t, faces, clearances):
    if faces.back:
        l1 = genHorizontalLinePoints(0, 0, w, -t, 0, False, clearances.top)
    else:
        l1 = genHorizontalStraightLinePoints(0, 0, -w, 0)
    if faces.right:
        l2 = genVerticalLinePoints(w, 0, -d, -t, 0, False, clearances.top)
    else:
        l2 = genVerticalStraightLinePoints(w, 0, -d, 0)
    if faces.front:
        l3 = genHorizontalLinePoints(w, -d, -w, t, 0, False, clearances.top)
    else:
        l3 = genHorizontalStraightLinePoints(w, -d, -w, 0)
    if faces.left:
        l4 = genVerticalLinePoints(0, -d, d, t, 0, False, clearances.top)
    else:
        l4 = genVerticalStraightLinePoints(0, -d, d, 0)
    return chain(l1, l2, l3, l4)


def genHorizontalLinePoints(x, y, length, notchHeight, offset, isConvex, clearance):
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
        if isConvex:
            c = clearance if ((i % 2) == 1) else -clearance
        else:
            c = -clearance if ((i % 2) == 1) else clearance
        c = c if length > 0 else -c
        if isConvex:
            h_c = 0
        else:
            h_c = clearance if notchHeight > 0 else -clearance
        yield (x + c, y if ((i % 2) == 1) else y + notchHeight + h_c)
        yield (x + c, y if ((i % 2) == 0) else y + notchHeight + h_c)

    # Last point is omitted (because it will be the first point of the next side)


def genVerticalLinePoints(x, y, length, notchHeight, offset, isConvex, clearance):
    # Symmetrical with the horizontal version, but with x & y swapped
    points = genHorizontalLinePoints(y, x, length, notchHeight, offset, isConvex, clearance)
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
