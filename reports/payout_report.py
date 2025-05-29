from typing import List, Dict, Any

widths = [15, 20, 15, 15]

def align_parameters(parameters: List[Any]) -> str:
	text = " " * widths[0] + parameters[0]
	index = 1

	for value in parameters[1:]:
		text += " " * (widths[index] - len(str(parameters[index-1]))) + str(value)
		index += 1
	return text 

def group_by_department(employees: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
	departments = {}
	for employee in employees:
		department = employee["department"]

		if department in departments:
			departments[department].append(employee)
		else:
			departments[department] = [employee]

	return departments

def generate_payout_report(employees: List[Dict[str, Any]]) -> str:
	departments = group_by_department(employees)

	text = ""
	text += "PAYOUT REPORT\n"
	text += "-" * 80 + "\n"
	text += align_parameters(["name", "hours", "rate", "payout"]) + "\n"

	for dep, employs in departments.items():
		text += dep + "\n"

		global_hours = 0
		global_payout = 0

		for emp in employs:
			emp["payout"] = emp["hours_worked"] * emp["rate"]
			global_hours += emp["hours_worked"]
			global_payout += emp["payout"]

			text += align_parameters([emp["name"], emp["hours_worked"], emp["rate"], emp["payout"]]) + "\n"

		text += align_parameters(["", global_hours, "", global_payout]) + "\n"

	return text

