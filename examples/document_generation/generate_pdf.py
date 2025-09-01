def create_pdf(filename):
    """Generate a sample PDF file."""
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hello from PyAutomateX!", ln=True, align='C')
    pdf.output(filename)

if __name__ == "__main__":
    create_pdf("sample.pdf")
