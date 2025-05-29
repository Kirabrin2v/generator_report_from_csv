from typing import List, Dict, Any

def normalize_header(header: str) -> str:
    if header in ["hourly_rate", "salary"]:
        return "rate"

    return header

def normalize_value(value: str) -> Any:
    if value.isdigit():
        return int(value)

    return value

def parse_csv(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, encoding="UTF-8") as f:
        lines = f.readlines()
        if len(lines) == 0: return []
        
        headers = [normalize_header(h) for h in lines[0].strip().split(",")]
        rows = []

        for line in lines[1:]:
            line = line.strip().split(",")
            row = {}

            for i in range(len(headers)):
                header = headers[i]
                row[header] = normalize_value(line[i])

            rows.append(row)

    return rows

