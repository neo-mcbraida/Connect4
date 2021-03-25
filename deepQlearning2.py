import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from keras.optimizers import Adam


import game

num_actions = 7

def create_q_model():

    inputs = inputs = layers.Input(shape=(7, 6))

    layer1 = layers.Dense(16, activation="relu")(inputs)
    layer2 = layers.Dense(16, activation="relu")(layer1)
    layer3 = layers.Dense(16, activation="relu")(layer2)


    
    action = layers.Dense(num_actions, activation="linear")(layer3)

    return keras.Model(inputs=inputs, outputs=action)

model = create_q_model()

model_target = create_q_model()

model.summary()

# improves training time
optimizer = keras.optimizers.Adam(learning_rate=0.00025, clipnorm=1.0)

print("Number of weights after calling the model:", len(model.weights))  # 6

turnCount = 0
# Experience replay buffers
action_history = []
state_history = []
state_next_history = []
rewards_history = []
done_history = []
episode_reward_history = []
running_reward = 0
episode_count = 0
frame_count = 0
# Number of frames to take random action and observe output
epsilon_random_frames = 50000
# Number of frames for exploration
epsilon_greedy_frames = 1000000.0
# Maximum replay length
# Note: The Deepmind paper suggests 1000000 however this causes memory issues
max_memory_length = 100000
# Train the model after 4 actions
update_after_actions = 4
# How often to update the target network
update_target_network = 10000
# Using huber loss for stability
loss_function = keras.losses.Huber()


while True:
    #game.run.Reset()
    state = game.episode.grid
    episode_reward = 0
    for turn in range(21):
        if turnCount < 50_000 or epsilon > np.random.rand(1)[0]:
            #random number between 1-7 to prevent model weighting being formed badly
            action = np.random.choice(num_actions)
        else:
            # Predict action Q-values
            # From environment state
            state_tensor = tf.convert_to_tensor(state)
            state_tensor = tf.expand_dims(state_tensor, 0)
            action_probs = model(state_tensor, training=False)
            # Take best action
            action = tf.argmax(action_probs[0]).numpy()

        state_next, reward, done = env.step(action)#environment uses input for turn and outputs next game env, reward for the last move
        state_next = np.array(state_next)

        episode_reward += reward

        # Save actions and states in replay buffer
        action_history.append(action)
        state_history.append(state)
        state_next_history.append(state_next)
        done_history.append(done)
        rewards_history.append(reward)
        state = state_next
        











                
