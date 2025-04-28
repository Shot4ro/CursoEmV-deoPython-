medida = float(input('Digite a metragem: '))
cm = medida * 100
mm = medida * 1000
dcm = medida - cm
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))