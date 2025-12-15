print("""
==== demo str/repr behavior ====
""")

class Demo_nada:
    pass

class Demo_str_repr:
    def __str__(self):
        return 'specfic __str__'
    def __repr__(self):
        return 'specific __repr__'

class Demo_str_only:
    def __str__(self):
        return 'specfic __str__'

class Demo_repr_only():
    def __repr__(self):
        return 'specific __repr__'

def showme(obj):
    print(f'{type(obj)=} {str(obj)=} {repr(obj)=}')

def demo_str_repr():

    na = Demo_nada()
    showme (na)

    ro = Demo_repr_only()
    showme(ro)

    so = Demo_str_only()
    showme(so)

    sr = Demo_str_repr()
    showme (sr)


def main():
    demo_str_repr()

print("""
Conclusion:
        dfn str dfn repr        use str        use repr
        0       0               default         default
        0       1               [use repr]      OK              <<--**
        1       0               OK              default
        1       1               OK              OK
""")

main()

[]
