class Biodata:
    siswa = 0
    
    def __init__(self, name,nim, tahun):
       self.name = name
       self.nim = nim
       self.tahun = tahun
       Biodata.siswa += 1
   
    def printbio(self):
        print('Nama: ' + self.name + '\nNim: ' + str(self.nim) 
              + '\nAngkatan: ' + str(self.tahun))

attr1 = input("Masukan Namamu: ")
attr2 = input("Masukan NIM kamu: ")
attr3 = input("Masukan Tahun Angkatanmu: ")
siswa1 = Biodata(attr1, attr2, attr3)
siswa1.printbio()
