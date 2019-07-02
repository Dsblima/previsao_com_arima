from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

#get data
def GetData(fileName):
    return read_csv(fileName, header=0, parse_dates=[0], index_col=0).values

#Function that calls ARIMA model to fit and forecast the data
def StartARIMAForecasting(Actual, P, D, Q):
	model = ARIMA(Actual, order=(P, D, Q))
	model_fit = model.fit(disp=0)
	prediction = model_fit.forecast()[0]
	return prediction
    
#Get exchange rates
ActualData = GetData('dez/dezsem.csv')
#Size of exchange rates
NumberOfElements = len(ActualData)

#Use 70% of data as training, rest 30% to Test model
TrainingSize = int(NumberOfElements * 0.7)
TrainingData = ActualData[0:TrainingSize]
TestData = ActualData[TrainingSize:NumberOfElements]

#new arrays to store actual and predictions
Actual = [x for x in TrainingData]
Predictions = list()

arquivo = open('dez/dez.txt', 'r')
conteudo = arquivo.readlines()

# insira seu conteúdo
# obs: o método append() é proveniente de uma lista
conteudo.append('ATUAL\t\tPREVISTO\n')

# Abre novamente o arquivo (escrita)
# e escreva o conteúdo criado anteriormente nele.

#in a for loop, predict values using ARIMA model
for timepoint in range(len(TestData)):
	ActualValue =  TestData[timepoint]
	#forcast value
	Prediction = StartARIMAForecasting(Actual, 3,1,0)    
	print('Actual=%f, Predicted=%f' % (ActualValue, Prediction))
	conteudo.append('%f, %f\n' % (ActualValue, Prediction))
	#add it in the list
	Predictions.append(Prediction)
	Actual.append(ActualValue)

#Print MSE to see how good the model is
#Error = MeanSquaredError(TestData, Predictions)
Error = mean_squared_error(TestData, Predictions)
conteudo.append('Mean Squared Error: %f\n' % (Error))
print('Test Mean Squared Error (smaller the better fit): %.3f' % Error)

arquivo = open('dez/dez.txt', 'w')
arquivo.writelines(conteudo)
arquivo.close()

# plot
pyplot.plot(TestData)
pyplot.plot(Predictions, color='red')
pyplot.show()