numbers = [str(n) for n in range(10)]
VOCABULARY = [" ","\n","+","-","*","/","(",")"] + numbers

SEQUENCE = {
    "number": ["operator", "eof"],
    "operator": ["number"],
    "": ["number"],
    "prio": ["number"],
}