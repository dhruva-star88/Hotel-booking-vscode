from fpdf import FPDF

def pdf_gen(content):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=30)
    pdf.cell(w=0, h=0, txt="Digital Reservation Ticket", align="L", ln=1)
    pdf.line(x1=10, y1=15, x2=200, y2=15)
    pdf.ln(4)
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=0, h=20, txt=f"Welcome To {content[3]}", align="L", ln=1)
    pdf.set_font(family="Times",style="B", size=15)
    pdf.cell(w=0, h=4, txt="Thank you for visiting our Hotel", align="L", ln=1)
    pdf.ln(4)
    pdf.set_font(family="Times",style="B", size=15)
    pdf.cell(w=0, h=4, txt="Here Your Booking Deatils:", align="L", ln=1)
    pdf.ln(8)
    pdf.set_font(family="Times",style="B", size=15)
    pdf.cell(w=0, h=4, txt=f"Name: {content[0]}", align="L", ln=1)
    pdf.ln(3)
    pdf.set_font(family="Times",style="B", size=15)
    pdf.cell(w=0, h=4, txt=f"Mobile Number: {content[1]}", align="L", ln=1)
    pdf.ln(3)
    pdf.set_font(family="Times",style="B", size=15)
    pdf.cell(w=0, h=4, txt=f"Email ID: {content[2]}", align="L", ln=1)
    pdf.ln(3)
    pdf.set_font(family="Times",style="B", size=15)
    pdf.cell(w=0, h=4, txt=f"Hotel: {content[3]}", align="L", ln=1)
    pdf.ln(4)
    pdf.set_font(family="Times",style="B", size=15)
    pdf.cell(w=0, h=4, txt="Your Ticket Has Been Booked Successfully", align="L", ln=1)
    output = pdf.output("output.pdf")
    return output


if __name__ == "__main__":
    pdf_gen(content=("Dhruva", "8867291499", "ncjsxmks@gmail.com", "Snow Place"))