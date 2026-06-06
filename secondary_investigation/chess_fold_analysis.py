import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE
from sftoe.proof import verify_value
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.gate import verify_code

def compute_period(x):
    if x == Fraction(1, 1):
        return 1
    d = x.denominator
    while d % 2 == 0:
        d //= 2
    if d == 1:
        return 1
    val = 2 % d
    order = 1
    while val != 1 and order < 10**6:
        val = (val * 2) % d
        order += 1
    return order if val == 1 else -1

def nim_oracle(heap_sizes):
    xor = 0
    for h in heap_sizes:
        xor ^= h
    return xor != 0

def encode_nim_position_prime(heaps, max_heap, q):
    bits_per_heap = max_heap.bit_length()
    index = 0
    for i, h in enumerate(heaps):
        index |= (h << (i * bits_per_heap))
    index = index % (q - 1)
    return Fraction(index + 1, q)

def run_nim_analysis():
    print("================================================================")
    print("NIM ANALYSIS WITH PRIME DENOMINATORS")
    print("================================================================")
    
    # 1. Nim max_heap=3, q=17
    q_17 = 17
    max_heap = 3
    print(f"Nim (2 heaps, max {max_heap}) mod q={q_17}:")
    p_positions = []
    for h1 in range(max_heap + 1):
        for h2 in range(max_heap + 1):
            heaps = (h1, h2)
            x = encode_nim_position_prime(heaps, max_heap, q_17)
            winning = nim_oracle(heaps)
            p = compute_period(x)
            if not winning:
                p_positions.append((heaps, x, p))
            print(f"  Heaps: {heaps} -> x: {x} | period: {p} | Win: {winning}")
            
    print("\nP-positions classification:")
    for heaps, x, p in p_positions:
        print(f"  P-position: {heaps} -> x: {x} | numerator: {x.numerator} | period: {p}")
        
    numerators = sorted([x.numerator for heaps, x, p in p_positions])
    spacings = [numerators[i+1] - numerators[i] for i in range(len(numerators)-1)]
    print(f"Numerators: {numerators}")
    print(f"Spacings: {spacings}")
    
    # Discover and generate SADE code for spacing fraction 5/17
    spacing_frac = Fraction(5, 17)
    node = find_derivation(spacing_frac)
    code = generate_sftoe_code(node, "verify_nim_spacing_17")
    print("\nSADE Generated Code for spacing 5/17:")
    print(code)
    print("Code Complies with Gate:", verify_code(code))
    
    # 2. Nim max_heap=255, q=65537
    q_65537 = 65537
    max_heap_255 = 255
    print(f"\nNim (2 heaps, max {max_heap_255}) mod q={q_65537}:")
    p_positions_large = []
    for h in range(max_heap_255 + 1):
        heaps = (h, h)
        x = encode_nim_position_prime(heaps, max_heap_255, q_65537)
        p_positions_large.append((heaps, x))
    
    numerators_large = sorted([x.numerator for heaps, x in p_positions_large])
    spacings_large = sorted(list(set([numerators_large[i+1] - numerators_large[i] for i in range(len(numerators_large)-1)])))
    print(f"P-position count: {len(p_positions_large)}")
    print(f"Spacings: {spacings_large}")
    
    # Discover and generate SADE code for spacing fraction 257/65537
    spacing_frac_large = Fraction(257, 65537)
    node_large = find_derivation(spacing_frac_large)
    code_large = generate_sftoe_code(node_large, "verify_nim_spacing_65537")
    print("\nSADE Generated Code for spacing 257/65537:")
    print(code_large)
    print("Code Complies with Gate:", verify_code(code_large))

def encode_chess_endgame_prime(white_king, white_piece, black_king, piece_type, white_to_move, q):
    stm = 1 if white_to_move else 0
    index = (white_king * 64 * 64 * 2 +
             white_piece * 64 * 2 +
             black_king * 2 +
             stm)
    index = index % (q - 1)
    return Fraction(index + 1, q)

def run_chess_endgame_analysis():
    print("\n================================================================")
    print("CHESS ENDGAME (KQ vs K) WITH MERSENNE PRIME DENOMINATOR q=524287")
    print("================================================================")
    q = 524287
    positions = [
        (4, 59, 0, True),
        (4, 27, 60, True),
        (0, 9, 56, True),
        (28, 45, 7, True),
        (36, 53, 63, True),
        (5, 14, 7, False),
        (42, 57, 56, False),
    ]
    for wk, wp, bk, wtm in positions:
        x = encode_chess_endgame_prime(wk, wp, bk, 5, wtm, q)
        p = compute_period(x)
        print(f"  Endgame WK={wk}, WQ={wp}, BK={bk}, STM={wtm} -> x: {x} | period: {p}")
        
    # SADE discovery on a sample endgame fraction
    sample_endgame = encode_chess_endgame_prime(positions[0][0], positions[0][1], positions[0][2], 5, positions[0][3], q)
    node = find_derivation(sample_endgame)
    code = generate_sftoe_code(node, "verify_chess_endgame_state")
    print("\nSADE Generated Code for sample endgame state:")
    print(code)
    print("Code Complies with Gate:", verify_code(code))

def run_initial_position_analysis():
    print("\n================================================================")
    print("CHESS STARTING POSITION ANALYSIS WITH q=67")
    print("================================================================")
    q = 67
    pieces = [0, 1, 2, 3, 4, 5, 6, 7,
              8, 9, 10, 11, 12, 13, 14, 15,
              48, 49, 50, 51, 52, 53, 54, 55,
              56, 57, 58, 59, 60, 61, 62, 63]
    index = sum(sq * (64**i) for i, sq in enumerate(pieces))
    p = (index % (q - 1)) + 1
    x = Fraction(p, q)
    period_val = compute_period(x)
    
    # Orbit elements and sum
    orbit = []
    cur = x
    for _ in range(period_val):
        orbit.append(cur)
        cur = fold(cur).value
    orbit_sum = sum(orbit)
    
    print(f"  Starting position index: {index}")
    print(f"  Mapped rational x: {x}")
    print(f"  Period under fold: {period_val}")
    print(f"  Orbit sum: {orbit_sum}")
    
    # SADE discovery on starting state
    node = find_derivation(x)
    code = generate_sftoe_code(node, "verify_chess_starting_state")
    print("\nSADE Generated Code for starting state:")
    print(code)
    print("Code Complies with Gate:", verify_code(code))

if __name__ == "__main__":
    run_nim_analysis()
    run_chess_endgame_analysis()
    run_initial_position_analysis()
