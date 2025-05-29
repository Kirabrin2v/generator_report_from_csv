from parser_csv import parse_csv

def test_parser_csv_reads_data_correctly():
    employees = parse_csv("tests/test_data.csv")

    assert employees == [
        {'id': 1, 'email': 'alice@example.com', 'name': 'Alice Johnson', 'department': 'Marketing', 'hours_worked': 160, 'rate': 50},
        {'id': 2, 'email': 'bob@example.com', 'name': 'Bob Smith', 'department': 'Design', 'hours_worked': 150, 'rate': 40},
        {'id': 3, 'email': 'carol@example.com', 'name': 'Carol Williams', 'department': 'Design', 'hours_worked': 170, 'rate': 60}
    ]
