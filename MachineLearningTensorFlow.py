from tabnanny import verbose

import tensorflow as tf
from tensorfloow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import  matplotlib.pyplot as plt

#DADOS DE EXEMPLO
x_train = tf.constant([[1.0],[2.0],[3.0],[4.0]])
y_train = tf.constant([[2.0],[4.0],[6.0],[8.0]])

#DEFINIMOS OS DADOS DE EXEMPLO X_TRAIN (ENTRADAS) Y_TRAIN (SAIDAS DESEJADAS) PARA TREINAR
# O MODELO. NO EXEMPLO, ESTAMOS USANDO PARES DE ENTRADA E SAIDA QUE REPRESENTAM UMA RELAÇÃO
# LINEAR SIMPLES (O DOBRO DAS ENTRADAS).

# Modelo de Regressão Linear Simples
model = Sequential()
model.add(Dense(units =1, input_shape = (1,)))
model.compile(optimizer='sgd', loss='mean_squared_error')

#DEFINIMOS O MODELO DE REGRESSÃO LINEAR SIMPLES USANDO A API KERAS SEQUENTIAL.
# O MODELO CONSISTE EM UMA UNICA CAMADA DENSA (OU TOTALMENTE CONECTADAS) COM UM
# NEURÔNIO (OU UNIDADE) E UMA ENTRADA. ESTAMOS USANDO A FUNÇÃO DE PERDA (loss) de erro
# quadratico médio (mean squared error - 'mean_squared_error') e ao otimizador 'sgd'
# (descida de gradiente estocástica)

# TREINAMENTO DO MODELO
history = model.fit(x_train, y_train, epochs=1000, verbose = 0)

# Nesta seção treinamos o modelo usando os dados de exemplo.
# Executamos 100 épocas de treinamento (epochs) e armazenamos o histórico do
#treinamento em history. o argumento verbose=0 faz com que o treinamento seja
# Executado em modo silencioso, sem exibir informações de progresso.

# PREVISÃO
x_new = tf.constant([[5.0]])
prediction("Predição:", prediction[0][0])

#Aqui, fazemos uma nova previsão usando o modelo treinado.
# Informamos uma nova entrada x_new (5.0) e calculamos a previsao. o resultado
# é impresso na tela.


# Plantar os resultados
plt.plot(history.history['loss'])
plt.title('Model Loss over training')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

# por fim, plotamos a perda (loss) do modelo ao longo do treinamento. usamos history.history('loss')
# Para obter a lista das perdas em cada época.
#Configuramos o titulo e rótulos do eixos e exibimos o grafico  com plt.show().
# Isso nos permite visualizar como a perda do modelo diminuiu durante o treinamento, o que é uma
# Indicação do aprendizado do modelo.




import  tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# Dados de exemplo
x_unsupervised = tf.constant([[1.0,2.0],[2.0, 3.0],[3.0,4.0],[4.0,5.0]])

# Aqui será os dados wxemplo,que será testar o modelo autoencoder.
# Esses dados são armazenados na variavel x_unsuoervised como um tensor
#tesnsorflow. cada linha representa um exemplo com duas caracteristicas.

#MODELO AUTOENCODER SIMPLES
input_layer = Input(shape=(2,))
encoded = Dense(units=1)(input_layer)
decoded = Dense(units=2) (encoded)

autoencoder = Model(inputs =input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

#Define o modelo autoencoder simples usando  a API keras:

#input_layer = Input(shape=(2,)): Define uma camada de entrada  com duas caracteristicas.
#encoded = Dense(units=1) (input_layer): Define uma camada densa (totalmente conectada) com uma
# unidade neurônio que representa a camada decodificada do autoencoder
#decoded = Dense(units=2)(encoded): Define uma camada densa com duas unidades que representa a camada
# decodificada do autoencoder.
#autoencoder = Model(inputs=input_layer, outputs=decoded): Cria o modelo autoencoder, especificando
# as camadas de entrada e  saida.
#autoencoder.compile(optimizer='adam' loss='meam_squared_error'): Compila o modelo , definindo o
#Otimizador Adam e a função de perda como erro quadratico médi



#Treinamento do modelo não supervisionado
autoencoder.fit(x_unsupervised, x_unsupervised, epochs= 1000, verbose=0)
# Nesta parte voçê treina o modelo autoencoder usando os dados de exemplo x_unsupervised.
# o autoencoder é treinado para reconstruir os dados de entrada apartir de sua representação
#codificada. o treinamento é executado por 1000 épocas (epochs) e é silencioso (verbose=0)
# que significa que não exibirá informações de progresso


# Previsão
prediction_unsupervised = autoencoder.predict(x_unsupervised)
print("Predição Não Supervisionada:", prediction_unsupervised)

#Reduzir a dimensionalidade de imagens mantendo a maior parte das informações importantes.


import tensorflow as tf
import gym

#Ambiente cartPole do gym
env = gym.make('cartPole-vi')

# Modelo Simples Aprendizado por Reforço
model_reinforcement = tf.keras.Sequential([
     tf.keras.layers.Dense(24,activation='relu', input_shape =(env.observation_space.shape[0],)),
     tf.keras.layers.Dense(env.action_space.n, activation = 'linear')
])

# TREINAMENTO POR REFORÇO (EXEMPLO  FICTICIO)
ma_episoes = 1000 #Define o o número máximo de episódios
for episode in range(max_episodes):
    #Reinicializa o ambiente para um novo episódio
    state = env.reset()
    done  = False

    while not done:
        # Escolhe uma ação aleatória do espaço de ação
        action = env.action_space.sample()
        # Executa a ação e obtém o próximo estado, recompensa e se o episódio
 # terminonu
        next_state, reward, done, _ -env.step(action)
     # Calcula o alvo para a ação tomada
        target = reward + 0,95 *tf.reduce_max(model_reinforcement.predict(next_state.reshape(1, -1)))


# obtém o valor Que previsto para o estado atual
        target_f = model_reinforcement.predict(state.reshape(1, -1))

# Atualiza o valor Q para a ação tomada com o novo alvo
        target_f[0][action] = target

# Treina o modelo usando o par (estado, novo valor Q)
        model_reinforcement.fit(state.reshape(1, -1), target_f, epochs = 1, verbose=0)

# Atualiza o estado para o próximo estado
        state = next_state

# Condição de parada: Se a média da recompensa dos ultimos 10 episódios atingir 1
     if episode % 10 == 0:
         average_reward = sun(reward for _ in range(10)) / 10.0
         print(f'Episode {episode},Average Reward:  {average_reward}')

#Adicionando uma condição de Parada
    if average_reward == 1: # PODE AJUSTAR ESSE VALOR CONFORME  NECESSARIO
       print(f'Solved after {episode} episodes!')
       break