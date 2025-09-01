def automate_excel(file_path):
    """Example RPA workflow to modify Excel files."""
    import openpyxl

    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    sheet['A1'] = "Updated by PyAutomateX"
    wb.save(file_path)

if __name__ == "__main__":
    automate_excel("sample.xlsx")
