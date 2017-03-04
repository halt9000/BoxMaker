from itertools import chain


#: Multiple of notch height
IDEAL_NOTCH_WIDTH = 4


def genFrontPoints(w, h, d, t, faces):
    return chain(
        genHorizontalLinePoints(0, t, w, -t, t),
        genVerticalLinePoints(w - t, 0, h, t, t),
        genHorizontalLinePoints(w, h - t, -w, t, -t),
        genVerticalLinePoints(t, h, -h, -t, -t),
    )

def genBackPoints(w, h, d, t, faces):
    return genFrontPoints(w, h, d, t, faces)


def genLeftPoints(w, h, d, t, faces):
    return chain(
        genHorizontalLinePoints(0, t, -d, -t, 0),
        genVerticalLinePoints(-d, 0, h, t, t),
        genHorizontalLinePoints(-d, h - t, d, t, 0),
        genVerticalLinePoints(0, h, -h, -t, -t),
    )


def genRightPoints(w, h, d, t, faces):
    return genLeftPoints(w, h, d, t, faces)


def genBottomPoints(w, h, d, t, faces):
    return genTopPoints(w, h, d, t, faces)


def genTopPoints(w, h, d, t, faces):
    return chain(
        genHorizontalLinePoints(0, 0, w, -t, 0),
        genVerticalLinePoints(w, 0, -d, -t, 0),
        genHorizontalLinePoints(w, -d, -w, t, 0),
        genVerticalLinePoints(0, -d, d, t, 0),
    )


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
