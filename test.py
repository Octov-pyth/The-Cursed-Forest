inputUser = float(input('Masukkan angka yang lebih dari 3 dan kurang dari 10:\t'))

Isilebihdari = (inputUser > 3)
print('Lebih dari 3', Isilebihdari)

Isikurangdari = (inputUser < 10)
print('Kurang dari 10:', Isikurangdari)

IsCorrect = Isilebihdari or Isikurangdari
print('Angka yang anda masukkan:\t', IsCorrect)

print('\n', 20*'=','\n')
inputUser = float(input('Masukkan angka:\t'))

Isikurangdari = (inputUser >= 3)
print('Kurang dari 3:\t', Isikurangdari)

Isilebihdari = (inputUser <= 10)
print('Lebih dari 10:\t', Isilebihdari)

IsCorrect = Isikurangdari and Isilebihdari
print('Angka yang anda masukkan:/t', IsCorrect)

