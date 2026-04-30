import argparse

def evaluate(expr: str) -> float:
    allowed = set("0123456789+-*/(). ")
    if not all(c in allowed for c in expr):
        raise ValueError("Invalid chars")
    return eval(expr)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("expression")
    args = ap.parse_args()
    print(f"{args.expression} = {evaluate(args.expression)}")

if __name__ == "__main__":
    main()
