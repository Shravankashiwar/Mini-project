def generate_report(data):
    # Generate the report content
    report = "Report\n"
    report += "-----------------\n"
    for item in data:
        report += f"{item['name']}: {item['value']}\n"
    return report

def save_report(report, filename):
    # Save the report content into a file
    with open(filename, 'w') as file:
        file.write(report)
    print(f"Report saved to {filename}")

def main():
    # Example data
    data = [
        {"name": "Item 1", "value": 10},
        {"name": "Item 2", "value": 20},
        {"name": "Item 3", "value": 30}
    ]

    # Generate the report
    report = generate_report(data)

    # Save the report into a file
    filename = "report.txt"
    save_report(report, filename)

if _name_ == "_main_":
    main()