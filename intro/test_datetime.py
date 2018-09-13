import datetime

DAYOFWEEK = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

now = datetime.datetime.now()

# Tanggal
print(now.day)

print( DAYOFWEEK[now.weekday()] )

# Bulan
print(now.month)

# Tahun
print(now.year)

# jam, menit, detik
print(now.hour)
print(now.minute)
print(now.second)




