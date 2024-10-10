def copy_f(inp: str, out: str) -> None:
  with open (inp, 'r', encoding='utf-8') as inp_f:
    with open (out, 'w', encoding='utf-8') as out_f:
      out_f.write(inp_f.read())
