from manusia import Manusia

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class manusia.
           Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s, "Sambil belajar.")
        self.keadaan = 'kenyang'
#a
    def ambilKotaTinggal(self):
        return self.kotaTinggal
#b
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal = ubah
#c
    def TambahUangSaku(self, tambah):
        self.uangSaku += tambah


