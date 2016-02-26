from itertools import chain


def genFrontPoints(w, h, d, t, n):
    return chain(
        genHorizontalLinePoints(0, 0, w / n, n, t, 0),
        genVerticalLinePoints(w - t, 0, h / n, n, t, 0),
        genHorizontalLinePoints(w, h - t, -w / n, n, t, -t),
        genVerticalLinePoints(0, h, -h / n, n, t, -t),
    )


def genBackPoints(w, h, d, t, n):
    return chain(
        genHorizontalLinePoints(0, 0, w / n, n, t, 0),
        genVerticalLinePoints(w - t, 0, h / n, n, t, 0),
        genHorizontalLinePoints(w, h - t, -w / n, n, t, -t),
        genVerticalLinePoints(0, h, -h / n, n, t, -t),
    )


def genLeftPoints(w, h, d, t, n):
    return chain(
        genHorizontalLinePoints(0, 0, -d / n, n, t, -t),
        genVerticalLinePoints(-d + t, 0, h / n, n, -t, 0),
        genHorizontalLinePoints(-d, h - t, d / n, n, t, t),
        genVerticalLinePoints(-t, h, -h / n, n, t, -t),
    )


def genRightPoints(w, h, d, t, n):
    return chain(
        genHorizontalLinePoints(0, 0, -d / n, n, t, 0),
        genVerticalLinePoints(-d, 0, h / n, n, t, 0),
        genHorizontalLinePoints(-d, h - t, d / n, n, t, 0),
        genVerticalLinePoints(0, h, -h / n, n, -t, -t),
    )


def genBottomPoints(w, h, d, t, n):
    return chain(
        genHorizontalLinePoints(0, -t, w / n, n, t, t),
        genVerticalLinePoints(w - t, 0, -d / n, n, t, -t),
        genHorizontalLinePoints(w, -d + t, -w / n, n, -t, -t),
        genVerticalLinePoints(t, -d, d / n, n, -t, t),
    )


def genTopPoints(w, h, d, t, n):
    return chain(
        genHorizontalLinePoints(0, 0, w / n, n, -t, 0),
        genVerticalLinePoints(w, 0, -d / n, n, -t, 0),
        genHorizontalLinePoints(w, -d, -w / n, n, t, 0),
        genVerticalLinePoints(0, -d, d / n, n, t, 0),
    )


def genHorizontalLinePoints(x, y, notchWidth, notchCount, notchHeight, offset):
    # First point
    yield (x + offset, y)

    # Two points for every side of a notch
    for i in range(1, notchCount):
        x = x + notchWidth
        yield (x, y if ((i % 2) == 1) else y + notchHeight)
        yield (x, y if ((i % 2) == 0) else y + notchHeight)

    # Last point is omitted (because it will be the first point of the next side)


def genVerticalLinePoints(x, y, notchWidth, notchCount, notchHeight, offset):
    # Symmetrical with the horizontal version, but with x & y swapped
    points = genHorizontalLinePoints(y, x, notchWidth, notchCount, notchHeight, offset)
    for y, x in points:
        yield (x, y)
