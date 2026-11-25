import hashlib, pathlib
TEXT = "I texted my boss 'I will definitely be there at 9' and autocorrect sent 'I will defiantly be there at 9' - HR wants a word."
def main():
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    data = TEXT.encode("utf-8")
    out.write_bytes(data)
    back = out.read_bytes()
    if hashlib.sha256(back).hexdigest() != hashlib.sha256(data).hexdigest():
        raise SystemExit("digest mismatch")
    if not (1 <= len(back.decode("utf-8")) <= 199):
        raise SystemExit("length out of gate")
if __name__ == "__main__":
    main()
