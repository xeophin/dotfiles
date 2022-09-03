"""This script converts the CSV provided by Neon to UBS format

This script lives here for version tracking. The actual script is a folder action created in Automator.
"""
from operator import itemgetter
from pathlib import Path
import re
import sys


UBS_ENCODING = "utf-8-sig"
NEON_ENCODING = "utf-8"
TARGET_FOLDER = "/Users/oliverburkhard/Documents/Buchhaltung/Kontoauszüge_xml"


def convert_content(content: str) -> str:
    lines = [line for line in content.split("\n") if line]
    extractor = itemgetter(0, 1, 5, 6, 8)

    def maybe_extract(line: str):
        try:
            return extractor(line)
        except:
            return tuple()

    transactions = [maybe_extract([elem.strip(" \"") for elem in line.split(";")]) for line in lines]  # type: ignore
    ubs_head = (
        "Bewertungsdatum;Bankbeziehung;Portfolio;Produkt;IBAN;Whrg.;Datum von;Datum bis;Beschreibung;Abschluss;"
        "Buchungsdatum;Valuta;Beschreibung 1;Beschreibung 2;Beschreibung 3;Transaktions-Nr.;"
        "Devisenkurs zum Originalbetrag in Abrechnungswährung;Einzelbetrag;Belastung;Gutschrift;Saldo"
    )
    ubs_body = "\n".join([
        ".".join(itemgetter(2, 1, 0)(transaction[0].split("-")))
        + ";"*10
        + (".".join(itemgetter(2, 1, 0)(transaction[0].split("-"))) + ";") * 2
        + ";".join(map(lambda x: "" if not x else str(x), transaction[2:]))
        + ";"*4
        + (f";{transaction[1]}" if not transaction[1].startswith("-") else f"{transaction[1][1:]};")
        + ";0"
        for transaction in transactions[1:] if transaction
    ])
    ubs_foot = (
        ";;;;;;;;;;;;;;;;;;;;\n"
        "Schlusssaldo;Anfangssaldo;;;;;;;;;;;;;;;;;;;\n"
        "0;0;;;;;;;;;;;;;;;;;;;\n"
    )
    return "\n".join([ubs_head, ubs_body, ubs_foot])


def convert_file(infile: str, outfile: str):
    with open(infile, "r", encoding=NEON_ENCODING) as f:
        content = f.read()
    to_write = convert_content(content)
    with open(outfile, "w", encoding=UBS_ENCODING) as f:
        f.write(to_write)


if __name__ == "__main__":
    for arg in sys.argv:
        new_filepath = str(arg)
        parts = re.search("([0-9]{4})_([0-9]+)_account_statements.csv$", new_filepath)
        if parts:
            year, mon = parts.groups()
            convert_file(Path(new_filepath), Path(new_filepath).with_name(f"{year}_{mon.zfill(2)}_neon.csv"))  # type: ignore
