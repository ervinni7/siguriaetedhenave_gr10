def get_column_order(key: str) -> list[int]:
    key = key.upper()
    sorted_chars = sorted(enumerate(key), key=lambda x: (x[1], x[0]))
    order = [0] * len(key)

    rank = 0
    i = 0
    while i < len(sorted_chars):
        j = i
        while j < len(sorted_chars) and sorted_chars[j][1] == sorted_chars[i][1]:
            j += 1
        for idx, _ in sorted_chars[i:j]:
            order[idx] = rank
        rank += 1
        i = j

    return order


def build_grid(plaintext: str, num_cols: int) -> tuple[list[list[str]], int]:
    text = plaintext.upper().replace(" ", "")
    padding = (num_cols - len(text) % num_cols) % num_cols
    text += "X" * padding

    grid = []
    for i in range(0, len(text), num_cols):
        grid.append(list(text[i:i + num_cols]))

    return grid, padding


def encrypt(plaintext: str, key: str) -> str:
    key = key.upper()
    num_cols = len(key)
    column_order = get_column_order(key)
    grid, _ = build_grid(plaintext, num_cols)
    num_rows = len(grid)
    max_rank = max(column_order) + 1
    ciphertext = ""

    for rank in range(max_rank):
        cols_with_rank = [c for c, r in enumerate(column_order) if r == rank]
        for row in range(num_rows):
            for col in cols_with_rank:
                ciphertext += grid[row][col]

    return ciphertext


def decrypt(ciphertext: str, key: str) -> str:
    key = key.upper()
    ciphertext = ciphertext.upper().replace(" ", "")
    num_cols = len(key)
    column_order = get_column_order(key)
    total_chars = len(ciphertext)

    if total_chars % num_cols != 0:
        raise ValueError("Gjatësia e ciphertextit nuk përputhet me gjatësinë e çelësit.")

    num_rows = total_chars // num_cols
    max_rank = max(column_order) + 1

    rank_col_count = {}
    for rank in range(max_rank):
        cols = [c for c, r in enumerate(column_order) if r == rank]
        rank_col_count[rank] = len(cols)

    rank_segments = {}
    pos = 0
    for rank in range(max_rank):
        segment_len = num_rows * rank_col_count[rank]
        rank_segments[rank] = ciphertext[pos:pos + segment_len]
        pos += segment_len

    grid = [[""] * num_cols for _ in range(num_rows)]
    for rank in range(max_rank):
        cols_with_rank = [c for c, r in enumerate(column_order) if r == rank]
        seg = rank_segments[rank]
        idx = 0
        for row in range(num_rows):
            for col in cols_with_rank:
                grid[row][col] = seg[idx]
                idx += 1

    plaintext = ""
    for row in grid:
        plaintext += "".join(row)

    return plaintext.rstrip("X")


def print_grid(grid: list[list[str]], key: str, column_order: list[int]):
    num_cols = len(key)
    col_width = 4

    print("\n  Rrjeti i enkriptimit:")
    header = "     " + "".join(f"{key[c]:^{col_width}}" for c in range(num_cols))
    print(header)

    order_row = "     " + "".join(f"({column_order[c]+1}){' ' * (col_width - 3)}" for c in range(num_cols))
    print(order_row)

    separator = "     " + "-" * (num_cols * col_width)
    print(separator)

    for r_idx, row in enumerate(grid):
        row_str = f"  {r_idx+1} |" + "".join(f"{cell:^{col_width}}" for cell in row)
        print(row_str)

    print()


def menu():
    print("\n" + "=" * 50)
    print("   Myszkowski Transposition Cipher")
    print("=" * 50)

    while True:
        print("\n  Zgjidhni një opsion:")
        print("  1. Enkriptim")
        print("  2. Dekriptim")
        print("  3. Dilni")
        print()

        choice = input("  Zgjedh: ").strip()

        if choice == "1":
            print()
            plaintext = input("  Teksti origjinal  : ").strip()
            key = input("  Çelësi             : ").strip().upper()

            if not key.isalpha():
                print("\n  [!] Çelësi mund të përmbajë vetëm shkronja.")
                continue
            if len(key) < 2:
                print("\n  [!] Çelësi duhet të ketë të paktën 2 shkronja.")
                continue

            column_order = get_column_order(key)
            grid, pad = build_grid(plaintext, len(key))
            ciphertext = encrypt(plaintext, key)

            print()
            print_grid(grid, key, column_order)

            if pad > 0:
                print(f"  [*] U shtuan {pad} shkronjë 'X' si mbushje (padding).")

            print(f"\n  Teksti i enkriptuar: {ciphertext}")
            print()

        elif choice == "2":
            print()
            ciphertext = input("  Teksti i enkriptuar: ").strip()
            key = input("  Çelësi              : ").strip().upper()

            if not key.isalpha():
                print("\n  [!] Çelësi mund të përmbajë vetëm shkronja.")
                continue
            if len(key) < 2:
                print("\n  [!] Çelësi duhet të ketë të paktën 2 shkronja.")
                continue

            try:
                column_order = get_column_order(key)
                plaintext = decrypt(ciphertext, key)

                num_cols = len(key)
                ct_clean = ciphertext.upper().replace(" ", "")
                num_rows = len(ct_clean) // num_cols
                max_rank = max(column_order) + 1
                rank_col_count = {rank: sum(1 for r in column_order if r == rank) for rank in range(max_rank)}
                rank_segments = {}
                pos = 0
                for rank in range(max_rank):
                    seg_len = num_rows * rank_col_count[rank]
                    rank_segments[rank] = ct_clean[pos:pos + seg_len]
                    pos += seg_len
                grid = [[""] * num_cols for _ in range(num_rows)]
                for rank in range(max_rank):
                    cols_with_rank = [c for c, r in enumerate(column_order) if r == rank]
                    seg = rank_segments[rank]
                    idx = 0
                    for row in range(num_rows):
                        for col in cols_with_rank:
                            grid[row][col] = seg[idx]
                            idx += 1

                print()
                print_grid(grid, key, column_order)
                print(f"  Teksti i dekriptuar: {plaintext}")
                print()

            except ValueError as e:
                print(f"\n  [!] Gabim: {e}")

        elif choice == "3":
            print("\n  Mirupafshim!\n")
            break

        else:
            print("\n  [!] Opsion i pavlefshëm. Provo përsëri.")


if __name__ == "__main__":
    menu()