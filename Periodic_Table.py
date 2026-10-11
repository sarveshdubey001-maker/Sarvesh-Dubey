symbols = [
    "H", "He",
    "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
    "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni",
    "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd",
    "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
    "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd",
    "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W",
    "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po",
    "At", "Rn",
    "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
    "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg",
    "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv",
    "Ts", "Og",
]

periods = [
    [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 2],
    [3, 4, None, None, None, None, None, None, None, None, None, None, 5, 6, 7, 8, 9, 10],
    [11, 12, None, None, None, None, None, None, None, None, None, None, 13, 14, 15, 16, 17, 18],
    list(range(19, 37)),
    list(range(37, 55)),
    [55, 56, "*", *range(72, 87)],
    [87, 88, "**", *range(104, 119)],
]


def format_cell(element):
    if isinstance(element, int):
        return f"{element:>3} {symbols[element - 1]:<2} "
    if element is None:
        return " " * 7
    return f"{element:>3}    "


print("PERIODIC TABLE")
print("Atomic number and element symbol")
print("".join(f"{group:>7}" for group in range(1, 19)))

for period in periods:
    print("".join(format_cell(element) for element in period))

print()
print("Lanthanides (*):")
print(" " * 21 + "".join(format_cell(element) for element in range(57, 72)))
print("Actinides (**):")
print(" " * 21 + "".join(format_cell(element) for element in range(89, 104)))
