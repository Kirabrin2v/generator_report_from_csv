import argparse
from parser_csv import parse_csv
from reports.payout_report import generate_payout_report

def main():
    parser = argparse.ArgumentParser(prog="", description="Генерирует отчёты на основе данных из CSV-файлов")
    parser.add_argument("files", nargs="+", help="Пути к CSV-файлам")
    parser.add_argument("--report", required=True, choices=["payout"], help="Тип генерируемого отчёта")

    args = parser.parse_args()

    employees = []
    for file_path in args.files:
        employees.extend(parse_csv(file_path))

    report = generate_payout_report(employees)
    print(report)

if __name__ == "__main__":
    main()

