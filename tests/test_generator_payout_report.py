from reports.payout_report import generate_payout_report, align_parameters, group_by_department, widths

def test_align_parameters():
    result = align_parameters(["name", "hours", "rate", "payout"])
    expected = (
        " " * widths[0] + "name"
        + " " * (widths[1] - len("name")) + "hours"
        + " " * (widths[2] - len("hours")) + "rate"
        + " " * (widths[3] - len("rate")) + "payout"
    )
    assert result == expected

def test_group_by_department(sample_employees):
    grouped = group_by_department(sample_employees)
    assert list(grouped.keys()) == ["Marketing", "Design"]
    assert len(grouped["Marketing"]) == 1
    assert len(grouped["Design"]) == 2

def test_generate_report(sample_employees):
    text = generate_payout_report(sample_employees)
    expected = '''PAYOUT REPORT
--------------------------------------------------------------------------------
               name                hours          rate           payout
Marketing
               Alice               160            50             8000
                                   160                           8000
Design
               Bob                 150            40             6000
               Carol               170            60             10200
                                   320                           16200
'''
    assert text == expected

