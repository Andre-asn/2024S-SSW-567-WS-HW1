def classify_triangle(a,b,c):

    if (a <= 0 or b <= 0 or c <= 0) or (a == str or b == str or c == str):
        return "NotATriangle"

    if (a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2):
        rightTri = True
    else:
        rightTri = False

    if (a == b == c):
        return "Equilateral Triangle"
    
    if (a == b or a == c or b == c):
        if rightTri:
            return "Right Isosceles Triangle"
        return "Isosceles Triangle"
    
    if (a != b != c):
        if rightTri:
            return "Right Scalene Triangle"
        return "Scalene Triangle"