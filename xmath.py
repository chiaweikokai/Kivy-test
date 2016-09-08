# using python3


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __add__(self, other):
        return Rational(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom
        )

    def __sub__(self, other):
        return Rational(
            self.numer * other.denom - other.numer * self.denom,
            self.denom * other.denom
        )

    def __mul__(self, other):
        return Rational(
            self.numer * other.numer,
            self.denom * other.denom
        )

    def __truediv__(self, other):
        return Rational(
            self.numer * other.denom,
            self.denom * other.numer
        )

    def __str__(self):
        return "{numer}/{denom}".format(
            numer=self.numer, denom=self.denom
        )

    def __repr__(self):
        return "Rational({numer}/{denom})".format(
            numer=self.numer, denom=self.denom
        )

