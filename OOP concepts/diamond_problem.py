class A:
    def introduce(self):
        return f"It is A class"


class B(A):
    def introduce(self):
        return f"It is B class"


class C(A):
    def introduce(self):
        return f"It is C class"


class D(B, C):
    def introduce(self):
        return f"It is D class"


ins_a = A()
ins_b = B()
ins_c = C()
ins_d = D()

print(ins_a.introduce())
print(ins_b.introduce())
print(ins_c.introduce())
print(ins_d.introduce())

print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
