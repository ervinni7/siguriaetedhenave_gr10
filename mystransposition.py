def get_column_order(key: str) -> list[int]:
  sorted_chars = sorted(enumerate(key), key = lambda x: x[1])
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
        i=j
        return order 
      
      
def build_grid(plaintext: str, num_cols: int) -> list[list[str]]:
  text = plaintext.upper().replace(" ","")
  padding = (num_cols - len(text) % num_cols) % num_cols
  text += "X" * padding
  grid = []
  for i in range(0,len(text), num_cols):
    grid.append(list(text[i:i + num_cols]))
    return grid

def encrypt(plaintext: str, key: str) -> str:
  key= key.upper()
  num_cols = len(key)
  column_order = get_column_order(key)
  grid = build_grid(plaintext,num_cols)
  num_rows = len(grid)
  max_rank = max(column_order) + 1
  ciphertext = ""

  for rank in range(max_rank):
    cols_with_rank = [c for c, r in enumerate(column_order) if r == rank]
    for row in range(num_rows):
      for col in cols_with_rank:
        ciphertext += grid[row][col]

        return ciphertext