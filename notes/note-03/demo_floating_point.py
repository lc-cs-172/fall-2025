""" determine range and sigdig for floating point """

print("\n================\n================")

repeat = 1024+64;

## determine the range

big_int = 1;
for i in range(repeat):
    big_int *= 2;
log10_big_int = math.log10(big_int)
print(f"""
big_int={big_int}
log10_big_int={log10_big_int}
""");

inf_real = 1.0;
for i in range(repeat):
    inf_real *= 2;
print(f"inf_real={inf_real}\n");

try_real = 1.0;
for doubling in range(repeat):
    big_real = try_real;
    try_real *= 2;
    if try_real == math.inf:
        break
print("[enrichment] Why is `big_real` below less than `maxval` stated in note-02?")
print(f"big_real={big_real}\ndoubling={doubling}\n");

## determine significant digits 

one = 1.0;
tiny = 1.0;
for i in range(repeat):
    if one+tiny == one: break
    tiny /= 2
print(f"tiny={tiny}\n");

#[]#
