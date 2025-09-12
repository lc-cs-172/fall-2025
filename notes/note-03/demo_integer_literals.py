print("\nTry, try, try again ...");

int_5_lit = 5
int_5_dec = 5
int_5_bin = 0b101
int_5_oct = 0o5
int_5_hex = 0x05

char_5_lit = ord('5')           # FYI: ord: Return the Unicode code point for a one-character string.
char_5_dec = 53
char_5_bin = 0b00110101
char_5_oct = 0o65
char_5_hex = 0x35

## I find this code messy

assert int_5_lit == int_5_bin == int_5_oct == int_5_dec == int_5_hex;
assert char_5_lit == char_5_bin == char_5_oct == char_5_dec == char_5_hex;

## and much prefer to align the terms for easy visual comprehension

assert   int_5_lit ==  int_5_bin ==  int_5_oct ==  int_5_dec ==  int_5_hex;
assert  char_5_lit == char_5_bin == char_5_oct == char_5_dec == char_5_hex;

print("[Fin]");

#[]#
