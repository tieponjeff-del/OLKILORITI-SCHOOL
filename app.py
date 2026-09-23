from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>OLKILORITI SENIOR SCHOOL</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body{font-family:Arial; margin:0; background:#f0f4f8;}
            .header{background:#0d47a1; color:white; padding:35px; text-align:center;}
            .motto{background:#ffca28; color:#0d47a1; display:inline-block; padding:8px 22px; border-radius:25px; font-weight:bold; letter-spacing:1px; margin:15px 0;}
            .box{max-width:900px; margin:25px auto; padding:15px;}
            .card{background:white; padding:30px; border-radius:15px; box-shadow:0 4px 12px rgba(0,0,0,0.1); text-align:center;}
            .footer{background:#0d47a1; color:white; text-align:center; padding:20px; border-radius:15px; margin-top:20px;}
        </style>
    </head>
    <body>
        <div class="header">
            <h1 style="margin:0;">OLKILORITI SENIOR SCHOOL</h1>
            <div class="motto">MOTTO: STRIVE TO EXCELL</div>
            <p>P.O BOX 25 LOLGORIAN | Transmara South, Narok County</p>
            <p style="margin:0; font-weight:bold;">GRADE 10 TO 12 - FULLY EQUIPED FOR CBE LEARNING</p>
        </div>

        <div class="box">
            <div class="card">
                <h2 style="color:#0d47a1;">Welcome to Olkiloriti Senior School</h2>
                <p>We offer Senior Secondary Education under Competency Based Education (CBE).</p>
                <p><b>Pathways Offered:</b> STEM, Social Sciences, Arts & Sports Science</p>
                <div style="background:#e3f2fd; padding:15px; border-radius:10px; margin-top:15px; border-left:5px solid #0d47a1;">
                    <b>ADMISSIONS OPEN FOR GRADE 10, 11 & 12 - 2026 INTAKE</b>
                </div>
            </div>

            <div style="display:flex; gap:15px; margin-top:20px; flex-wrap:wrap;">
                <div style="flex:1; min-width:200px; background:white; padding:20px; border-radius:10px; text-align:center;">
                    <h3>🎓 Grades</h3>
                    <p>Grade 10<br>Grade 11<br>Grade 12</p>
                </div>
                <div style="flex:1; min-width:200px; background:white; padding:20px; border-radius:10px; text-align:center;">
                    <h3>🏫 Facilities</h3>
                    <p>Modern Labs<br>ICT Centre<br>CBE Classrooms</p>
                </div>
                <div style="flex:1; min-width:200px; background:white; padding:20px; border-radius:10px; text-align:center;">
                    <h3>📍 Address</h3>
                    <p><b>P.O BOX 25<br>LOLGORIAN</b></p>
                </div>
            </div>

            <div class="footer">
                <h3 style="margin:0;">OLKILORITI SENIOR SCHOOL</h3>
                <p style="margin:5px 0 0 0;">STRIVE TO EXCELL | P.O BOX 25 LOLGORIAN</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
