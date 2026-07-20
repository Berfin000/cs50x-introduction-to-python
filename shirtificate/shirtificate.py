from fpdf import FPDF


class CS50Shirtificate(FPDF):
    def __init__(self, name):
        # Üst sınıf olan FPDF constructor'ını çağırıp A4 dikey sayfa oluşturuyoruz
        super().__init__(orientation="P", unit="mm", format="A4")
        self.name = name
        self.add_page()
        self.create_pdf()

    def header(self):
        # PDF'in en üstündeki ana başlık
        self.set_font("helvetica", "B", 45)
        # Genişlik: 0 (sayfa genişliği kadar), Yükseklik: 40, Hizalama: C (Center)
        self.cell(0, 40, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
        # Başlık ile tişört arasına biraz boşluk bırakalım
        self.ln(10)

    def create_pdf(self):
        # 1. Tişört Görselini Yerleştirme
        # A4 genişliği 210mm'dir. Tişörtü 170mm genişliğinde yapıp yatayda ortalıyoruz (x = 20)
        self.image("shirtificate.png", x=20, y=80, w=170)

        # 2. Tişörtün Üzerindeki Beyaz Yazı
        self.set_font("helvetica", "B", 24)
        # Yazı rengini beyaz yapıyoruz (RGB: 255, 255, 255)
        self.set_text_color(255, 255, 255)

        # Tişörtün dikey hizasına (y ekseni) denk gelecek şekilde imleci konumlandırıyoruz
        self.set_y(140)
        # Yazıyı yatayda tam ortalayarak yazdırıyoruz
        self.cell(0, 10, f"{self.name} took CS50", align="C")


def main():
    name = input("Name: ").strip()
    # Kendi yazdığımız sınıftan bir nesne üretiyoruz
    pdf = CS50Shirtificate(name)
    # PDF dosyasını kaydediyoruz
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
