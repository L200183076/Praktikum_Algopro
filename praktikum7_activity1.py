rumus={"segitiga":"L=0.5*a*t",
       "persegi":"L=s**2",
       "persegi_panjang":"L=p*l",
       "lingkaran":"L=pi*r**2",
       "jajar_genjang":"L=a*t"}

print ("""

No | Nama Bangunan   | Rumus Luas
---|-----------------|--------------
1  | segitiga        |""",rumus["segitiga"],"""
2  | persegi         |""",rumus["persegi"],"""
3  | persegi_panjang |""",rumus["persegi_panjang"],"""
4  | lingkaran       |""",rumus["lingkaran"],"""
5  | jajar_genjang   |""",rumus["jajar_genjang"])
