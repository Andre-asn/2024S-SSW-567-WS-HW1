import pytest
from HW1.lib.triangleClass import classify_triangle

class Test_Triangle:

    def test_tri(self):
        tri = classify_triangle(2,2,4)
        assert tri == 'Isosceles Triangle'

        tri2 = classify_triangle(4,4,4)
        assert tri2 == 'Equilateral Triangle'

        tri3 = classify_triangle(5,6,4)
        assert tri3 == 'Scalene Triangle'

        #tri4 = classify_triangle("x",6,8)
        #assert tri4 == 'NotATriangle'

        #tri5 = classify_triangle(-3,6,8)
        #assert tri5 == 'NotATriangle'