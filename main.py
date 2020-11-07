print("======================")
print("Program Ramalan Zodiak")
print("======================")
print("Script By ArizkiNewbie\nJangan ganti Copyright \nJawab y = lanjut dan n = tidak")
jwb = input("Apakah ingin dilanjutkan (y/n) : ")
if (jwb =="y"):
    print("baiklah, akan dilanjutkan !\n")
else:
    print("Terimakasih :)\n")
    exit()

print("PENTING! Jangan Input Bulan Lahir dalam bentuk angka\nContoh format input Kelahiran > 1 Januari 2002")
var = input("masukkan kelahiran sesuai format diatas : ")
out = var.split()
tl = int(out[0])
bl_up = out[1]
th = int(out[2])
bl = bl_up.capitalize()
#Capricorn 21 Desember - 19 Januari
if (tl>=21 and tl<=31 and bl=="Desember") or (tl>=1 and tl<=19 and bl=="Januari"):
    zodiak = "Capricorn : Pendiam, Rajin dan Ambisius, Materialis, Gengsi Tinggi, Suka Memerintah, Suka memperalat Orang Lain"

#Aquarius 20 Januari - 18 Februari
elif (tl>=20 and tl<=31 and bl=="Januari") or (tl>=1 and tl<=18 and bl=="Februari"):
    zodiak = "Aquarius : Tenang, Obyektif (Tidak Memihak), Jenius, Penuh Ide, Cepat Mengerti"

#Pisces 19 Februari - 20 Maret
elif (tl>=19 and tl<=29 and bl=="Februari") or (tl>=1 and tl<=20 and bl=="Maret"):
    zodiak = "Pisces : Memiliki Sisi Manusiawi Yang Besar, Penuh Cinta, Praktis, Suka Mengkhayal"

#Aries 21 Maret - 20 April
elif (tl>=21 and tl<=31 and bl=="Maret") or (tl>=1 and tl<=20 and bl=="April"):
    zodiak = "Aries : Agresif, Energik, Impulsif, Berjiwa Pemimpin, Tidak Sabaran, Egois, Cepat Emosi"

#Taurus 21 April - 20 Mei
elif (tl>=21 and tl<=31 and bl=="April") or (tl>=1 and tl<=20 and bl=="Mei"):
    zodiak = "Taurus : Keras Kepala, Materialistis, Pasif, Ramah & Sabar, Praktis dan Setia, Memiliki Jiwa Toleransi"

#Gemini 21 Mei - 20 Juni
elif (tl>=21 and tl<=31 and bl=="Mei") or (tl>=1 and tl<=20 and bl=="Juni"):
    zodiak = "Gemini : Lincah, Pandai berbicara, Tidak Stabil, Mudah Berubah-Ubah, Mudah Gugup, Sangat Peka"

#Cancer 21 Juni - 20 Juli
elif (tl>=21 and tl<=31 and bl=="Juni") or (tl>=1 and tl<=20 and bl=="Juli"):
    zodiak = "Cancer : Suasana Hati Tidak Menentu, Sentimentil, Setia, Penuh Perhatian, Sulit Memaafkan, Memiliki Daya Ingat Yang Kuat"

#Leo 21 Juli - 21 Agustus
elif (tl>=21 and tl<=31 and bl=="Juli") or (tl>=1 and tl<=20 and bl=="Agustus"):
    zodiak = "Leo : Suka Memimpin, Dermawan Dan Murah Hati, Penuh Gaya, Aristokratik, Congkak, Percaya Diri Tinggi"

#Virgo 22 Agustus - 22 September
elif (tl>=21 and tl<=31 and bl=="Agustus") or (tl>=1 and tl<=20 and bl=="September"):
    zodiak = "Virgo : Praktis, Analistis, Kritis, Berkepala Dingin Dan Logis, Rajin, Sederhana"

#Libra 23 September - 22 Oktober
elif (tl>=21 and tl<=31 and bl=="September") or (tl>=1 and tl<=20 and bl=="Oktober"):
    zodiak = "Libra : Penuh Keraguan, Bimbang, Adil Pandai Bermuka Dua, Memiliki Naluri Yang Kuat, Mempesona"

#Scorpio 23 Oktober - 22 November
elif (tl>=21 and tl<=31 and bl=="Oktober") or (tl>=1 and tl<=20 and bl=="November"):
    zodiak = "Scorpio : Panjang Akal, Pendiam, Pendendam, Gigih, Tekun"
    
#Sagitarius 23 November - 20 Desember
elif (tl>=21 and tl<=31 and bl=="November") or (tl>=1 and tl<=20 and bl=="Desember"):
    zodiak = "Sagitarius : Berjiwa Petualang, Pandai, Suka Kebebasan, Mandiri, Pandai Berdiplomasi, Berpandangan Luas"
else:
    print("\nFormat Anda salah")
    print("Terimakasih sudah meluangkan waktu :)")
    exit ()

print(f"\nZodiak untuk kelahiran {tl} {bl} {th} ialah {zodiak}.")
print("Terimakasih sudah meluangkan waktu :)\n")
exit ()