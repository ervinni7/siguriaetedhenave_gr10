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


def build_grid(plaintext: str, num_cols: int) -> list[list[str]]:
    text = plaintext.upper().replace(" ", "")
    padding = (num_cols - len(text) % num_cols) % num_cols
    text += "X" * padding

    grid = []
    for i in range(0, len(text), num_cols):
        grid.append(list(text[i:i + num_cols]))

    return grid


def encrypt(plaintext: str, key: str) -> str:
    key = key.upper()
    num_cols = len(key)
    column_order = get_column_order(key)
    grid = build_grid(plaintext, num_cols)
    num_rows = len(grid)
    max_rank = max(column_order) + 1
    ciphertext = ""

    for rank in range(max_rank):
        cols_with_rank = [c for c, r in enumerate(column_order) if r == rank]
        for row in range(num_rows):
            for col in cols_with_rank:
                ciphertext += grid[row][col]

    return ciphertext

#Pjesa e Dekriptimit

def decrypt(ciphertext: str, key: str) -> str:
    key = key.upper()
    ciphertext = ciphertext.upper()
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


def print_demo(plaintext: str, key: str):
    print(f"\n{'='*50}")
    print(f"  Teksti origjinal   : {plaintext}")
    print(f"  Çelësi             : {key}")

    encrypted = encrypt(plaintext, key)
    print(f"  Teksti i enkriptuar: {encrypted}")

    decrypted = decrypt(encrypted, key)
    print(f"  Teksti i dekriptuar: {decrypted}")

    orig_clean = plaintext.upper().replace(" ", "")
    ok = decrypted == orig_clean
    print(f"  Verifikimi         : {'KORREKT' if ok else 'GABIM!'}")


if __name__ == "__main__":
   print_demo("HELLO WORLD", "MAMMA")
   print_demo("SEKRET I RENDESISHEM", "LETTER")
   print_demo("SULMI FILLON NESER", "BALLOON")
   print_demo("KRIPTOGRAFIA MODERNE", "COMMITTEE")