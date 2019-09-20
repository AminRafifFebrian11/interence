class Pegawai:
  def __init__(self, nama, gaji=0):
    self.nama = nama
    self.gaji = gaji
  def tunjangan(self, persen):
    self.gaji = self.gaji + (self.gaji * persen)
  def kerja(self):
    print(self.nama, "Pekerjaannya")
  def __repr__(self):
    return "<Pegawai:\n nama = %s, gaji = %s" %(self.nama, self.gaji)
class Koki(Pegawai):
  def __init__(self, nama):
    Pegawai.__init__(self, nama, 200000)
  def kerja(self):
    print(self.nama, "Membuat Makanan")
class Pelayan(Pegawai):
  def __init__(self, nama):
    Pegawai.__init__(self, nama, 300000)
  def kerja(self):
    print(self.nama, "Melayani Pelanggang")
class BurgerRobot(Koki):
  def __inti__(Self, nama):
    Koki.__init__(Self, nama)
  def kerja(self):
    print(self.nama, "Membuat Burger")

if __name__ == "__main__":
  dani = BurgerRobot("Dani")
  print(dani)
  dani.kerja()
  dani.tunjangan(0.10)
  print(dani)
  print

  for kelas in Pegawai, Koki, Pelayan, BurgerRobot:
    objek = kelas(kelas.__name__)
    objek.kerja()
