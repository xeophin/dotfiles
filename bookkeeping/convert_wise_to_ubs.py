"""This script converts the CSV provided by Neon to UBS format

This script lives here for version tracking. The actual script is a folder action created in Automator.
"""
from operator import itemgetter
from pathlib import Path
import re
import sys


UBS_ENCODING = "utf-8-sig"
WISE_ENCODING = "utf-8"
SEP = ','
TARGET_FOLDER = "/Users/oliverburkhard/Documents/Buchhaltung/Kontoauszüge_xml"


def convert_content(content: str) -> str:
    lines = [line for line in content.split("\n") if line]
    extractor = itemgetter(0, 1, 2, 4)

    def maybe_extract(line: str):
        try:
            return extractor(line)
        except:
            return tuple()

    transactions = [maybe_extract([elem.strip(" \"") for elem in line.split(
        SEP)]) for line in lines]  # type: ignore
    ubs_head = (
        "Bewertungsdatum;Bankbeziehung;Portfolio;Produkt;IBAN;Whrg.;Datum von;Datum bis;Beschreibung;Abschluss;"
        "Buchungsdatum;Valuta;Beschreibung 1;Beschreibung 2;Beschreibung 3;Transaktions-Nr.;"
        "Devisenkurs zum Originalbetrag in Abrechnungswährung;Einzelbetrag;Belastung;Gutschrift;Saldo"
    )
    ubs_body = "\n".join([
        ".".join(itemgetter(0, 1, 2)(transaction[1].split("-")))
        + ";"*10
        + (".".join(itemgetter(0, 1, 2)(transaction[1].split("-"))) + ";") * 2
        + ";".join([transaction[3]])
        + ";"*3
        + ";".join([transaction[0]])
        + ";"*3
        + (f";{transaction[2]}" if not transaction[2].startswith("-")
           else f"{transaction[2][1:]};")
        + ";0"
        for transaction in transactions[1:] if transaction
    ])
    ubs_foot = (
        ";;;;;;;;;;;;;;;;;;;;\n"
        "Schlusssaldo;Anfangssaldo;;;;;;;;;;;;;;;;;;;\n"
        "0;0;;;;;;;;;;;;;;;;;;;\n"
    )
    return "\n".join([ubs_head, ubs_body, ubs_foot])


def convert_file(infile: Path):
    with open(infile, "r", encoding=WISE_ENCODING) as f:
        content = f.read()
    to_write = convert_content(content)

    # Read the first transaction and extract year and month
    lines = [line for line in content.split("\n") if line]
    dateElement = lines[1].split(SEP)[1].split('-')
    year = dateElement[2]
    month = dateElement[1]

    with open(infile.with_name(f"wise_{year}-{month}.csv"), "w", encoding=UBS_ENCODING) as f:
        f.write(to_write)


if __name__ == "__main__":
    for arg in sys.argv:
        filepath = Path(str(arg))

        if filepath.name == 'balance_statement.csv':

            # Convert the file
            convert_file(filepath)

            # remove the old file
            filepath.unlink()
