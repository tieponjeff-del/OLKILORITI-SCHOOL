from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><head><title>OLKILORITI SENIOR SCHOOL - P.O BOX 25 LOLGORIAN</title>
    <meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body style="font-family:Arial; margin:0; background:#f0f4f8;">
    <div style="background:#0d47a1; color:white; padding:35px; text-align:center;">
    <h1 style="margin:0;">OLKILORITI SENIOR SCHOOL</h1>
    <p style="background:#ffca28; color:#0d47a1; display:inline-block; padding:7px 20px; border-radius:25px; font-weight:bold; margin:15px 0;">MOTTO: STRIVE TO EXCELL</p>
    <p style="margin:5px 0;">P.O BOX 25 LOLGORIAN | Transmara South, Narok County</p>
    <p style="margin:5px 0;">GRADE 10 TO 12 - FULLY EQUIPED FOR CBE LEARNING</p>
    </div>
    <div style="max-width:900px; margin:25px auto; padding:15px;">
    <div style="background:white; padding:30px; border-radius:15px; box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center;">
    <h2 style="color:#0d47a1;">Welcome to Olkiloriti Senior School</h2>
    <p>We are a leading CBE Senior School in Lolgorian offering all 3 pathways: STEM, Social Sciences, Arts & Sports Science.</p>
    <div style="background:#e3f2fd; padding:15px; border-radius:10px; margin-top:15px;"><b>ADMISSIONS OPEN FOR GRADE 10, 11 & 12 - 2026</b></div>
    </div>
    <div style="background:#0d47a1; color:white; text-align:center; padding:20px; border-radius:15px; margin-top:20px;">
    Contact: P.O BOX 25 LOLGORIAN | STRIVE TO EXCELL
    </div></div></body></html>
    """

if __name__ == '__main__':
    app.run()
