from cProfile import label
from tabnanny import verbose

import tensorflow as tf
from docutils.languages.af import labels
from tensorflow.keras.models import Sequential  # Corrected import statement
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# DADOS DE EXEMPLO
x_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])

# DEFINIMOS OS DADOS DE EXEMPLO X_TRAIN (ENTRADAS) Y_TRAIN (SAIDAS DESEJADAS) PARA TREINAR
# O MODELO. NO EXEMPLO, ESTAMOS USANDO PARES DE ENTRADA E SAIDA QUE REPRESENTAM UMA RELAÇÃO
# LINEAR SIMPLES (O DOBRO DAS ENTRADAS).

# Modelo de Regressão Linear Simples
model = Sequential()
model.add(Dense(units=1, input_shape=(1,)))
model.compile(optimizer='sgd', loss='mean_squared_error')

# DEFINIMOS O MODELO DE REGRESSÃO LINEAR SIMPLES USANDO A API KERAS SEQUENTIAL.
# O MODELO CONSISTE EM UMA UNICA CAMADA DENSA (OU TOTALMENTE CONECTADAS) COM UM
# NEURÔNIO (OU UNIDADE) E UMA ENTRADA. ESTAMOS USANDO A FUNÇÃO DE PERDA (loss) de erro
# quadratico médio (mean squared error - 'mean_squared_error') e ao otimizador 'sgd'
# (descida de gradiente estocástica)

# TREINAMENTO DO MODELO
history = model.fit(x_train, y_train, epochs=1000, verbose=0)

# Nesta seção treinamos o modelo usando os dados de exemplo.
# Executamos 100 épocas de treinamento (epochs) e armazenamos o histórico do
# treinamento em history. o argumento verbose=0 faz com que o treinamento seja
# Executado em modo silencioso, sem exibir informações de progresso.

# PREVISÃO
x_new = tf.constant([[5.0]])
prediction = model.predict(x_new)  # Corrected the call to predict
print("Predição:", prediction[0][0])  # Corrected the print statement to access the prediction value

# Aqui, fazemos uma nova previsão usando o modelo treinado.
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
# Configuramos o titulo e rótulos do eixos e exibimos o grafico  com plt.show().
# Isso nos permite visualizar como a perda do modelo diminuiu durante o treinamento, o que é uma
# Indicação do aprendizado do modelo.


from cProfile import label
from tabnanny import verbose

import tensorflow as tf
from docutils.languages.af import labels
from tensorflow.keras.models import Sequential  # Corrected import statement
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

import gym

# ... other imports
# ... some previous code
# TREINAMENTO POR REFORÇO (EXEMPLO FICTICIO)
env = gym.make('CartPole-v1')
max_episodes = 1000

# Define the model_reinforcement here before using it
model_reinforcement = Sequential()
model_reinforcement.add(Dense(units=24, activation='relu', input_shape=env.observation_space.shape))
model_reinforcement.add(Dense(units=24, activation='relu'))
model_reinforcement.add(Dense(units=env.action_space.n, activation='linear'))  # Output layer with linear activation
model_reinforcement.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=0.01))  # Using Adam optimizer

for episode in range(max_episodes):
    # ... your existing code...

    # Initialize 'done' and 'state' before the 'while' loop
    done = False
    state = env.reset()  # Get initial state

    while not done:
        # Escolhe uma ação aleatória do espaço de ação
        action = env.action_space.sample()
        # Executa a ação e obtém o próximo estado, recompensa e se o episódio
        # terminou
        next_state, reward, done, _ = env.step(action)  # Corrected assignment
        # Calcula o alvo para a ação tomada
        target = reward + 0.95 * tf.reduce_max(
            model_reinforcement.predict(next_state.reshape(1, -1)))  # Corrected float value

        # obtém o valor Que previsto para o estado atual
        target_f = model_reinforcement.predict(state.reshape(1, -1))

        # Atualiza o valor Q para a ação tomada com o novo alvo
        target_f[0][action] = target

        # Treina o modelo usando o par (estado, novo valor Q)
        model_reinforcement.fit(state.reshape(1, -1), target_f, epochs=1, verbose=0)

        # Atualiza o estado para o próximo estado
        state = next_state

    # Condição de parada: Se a média da recompensa dos ultimos 10 episódios atingir a 1
    if episode % 10 == 0:  # Corrected indentation
        average_reward = sum(
            reward for _ in range(10)) / 10.0  # Corrected variable name to sum and changed to float division
        print(f'Episode {episode}, Average Reward: {average_reward}')

    # Adicionando uma condição de Parada
    if average_reward == 1:  # PODE AJUSTAR ESSE VALOR CONFORME NECESSARIO
        print(f'Solved after {episode} episodes!')
        break

# ... (Rest of your code below remains unchanged) ...

import numpy as np
import pandas as pd  # Import pandas
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import tensorflow as tf

# CRIE um dataframe
dados = pd.DataFrame({'Mês': meses, 'Vendas': vendas})  # Changed to pd.DataFrame

# Divida os dados em conjunto de treinamento e teste
x = dados[['Mês']]  # Changed 'Mes' to 'Mês'
y = dados['Vendas']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
                                                    random_state=42)  # Changed randon_state to random_state

# Normalização dos dados de treinamento e teste
x = dados[['Mês']]  # Changed 'Mes' to 'Mês'
y = dados[['Vendas']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Crie e treine o modelo de regressão linear usando tensorflow
model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),  # Camada de entrada using tf.keras.Input
    tf.keras.layers.Dense(units=64, activation='relu'),  # Camada escondida with 64 units and relu activation
    tf.keras.layers.Dense(units=1)  # Camada de Saída
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Treine o modelo por mais épocas
model.fit(x_train, y_train, epochs=500, verbose=0)

# Normalization of training and test data
x = dados[['Mês']]
y = dados[['Vendas']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create a MinMaxScaler instance
scaler = MinMaxScaler()

# Fit the scaler on the training data and transform both training and test data
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# ... (Rest of the code) ...

# Make predictions on the test set using the scaled data
predictions_scaled = model.predict(x_test_scaled)

# Desfaça a normalização para avaliar o desempenho
predictions_inverse = scaler.inverse_transform(predictions_scaled)
y_test_inverse = scaler.inverse_transform(np.array(y_test).reshape(-1, 1))

# Visualize as previsões em relação aos dados reais
plt.scatter(x_test, y_test_inverse, label='Dados Reais')
plt.plot(x_test, predictions_inverse, color='red', label='Previsões')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Previsão de vendas com Regressão Linear (TensorFlow)')
plt.legend()
plt.show()

# Avalie o desempenho do modelo
erro_mse = mean_squared_error(y_test_inverse, predictions_inverse)
print(f'Erro Médio Quadratico (MSE):{erro_mse:.2f}')

# Faça uma previsão para o proximo mês
proximo_mes_scaled = scaler.transform(np.array([[13]]))  # Corrected the method name to 'transform'
previsao_proximo_scaled = model.predict(proximo_mes_scaled)
previso_proximo_mes = scaler.inverse_transform(previsao_proximo_scaled)[0, 0]
print(f'Previsao de Vendas para o proximo Mês:{previso_proximo_mes:.2f}')



