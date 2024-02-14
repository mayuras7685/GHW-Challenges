# tetris-ai

## Demo

![Demo - First 10000 points](./demo.gif)

## How does it work

#### Reinforcement Learning

At first, the agent will play random moves, saving the states and the given reward in a limited queue (replay memory). At the end of each episode (game), the agent will train itself (using a neural network) with a random sample of the replay memory. As more and more games are played, the agent becomes smarter, achieving higher and higher scores.

Since in reinforcement learning once an agent discovers a good 'path' it will stick with it, it was also considered an exploration variable (that decreases over time), so that the agent picks sometimes a random action instead of the one it considers the best. This way, it can discover new 'paths' to achieve higher scores.

#### Training

The training is based on the **Q Learning algorithm**. Instead of using just the current state and reward obtained to train the network, it is used Q Learning (that considers the transition from the current state to the future one) to find out what is the best possible score of all the given states **considering the future rewards**, i.e., the algorithm is not greedy. This allows for the agent to take some moves that might not give an immediate reward, so it can get a bigger one later on (e.g. waiting to clear multiple lines instead of a single one).

The neural network will be updated with the given data (considering a play with reward _reward_ that moves from _state_ to _next_state_, the latter having an expected value of _Q_next_state_, found using the prediction from the neural network):

if not terminal state (last round): _Q_state_ = _reward_ + _discount_ × _Q_next_state_
else: _Q_state_ = _reward_

#### Game State

It was considered several attributes to train the network. Since there were many, after several tests, a conclusion was reached that only the first four present were necessary to train:

- **Number of lines cleared**
- **Number of holes**
- **Bumpiness** (sum of the difference between heights of adjacent pairs of columns)
- **Total Height**
- Max height
- Min height
- Max bumpiness
- Next piece
- Current piece

#### Game Score

Each block placed yields 1 point. When clearing lines, the given score is _number_lines_cleared_^2 × _board_width_. Losing a game subtracts 1 point.

#### Training

For the training, the replay queue had size 20000, with a random sample of 512 selected for training each episode, using 1 epoch.

#### Requirements

- Tensorflow (`tensorflow-gpu==1.14.0`, CPU version can be used too)
- Tensorboard (`tensorboard==1.14.0`)
- Keras (`Keras==2.2.4`)
- Opencv-python (`opencv-python==4.1.0.25`)
- Numpy (`numpy==1.16.4`)
- Pillow (`Pillow==5.4.1`)
- Tqdm (`tqdm==4.31.1`)

## Results

For 2000 episodes, with epsilon ending at 1500, the agent kept going for too long around episode 1460, so it had to be terminated. Here is a chart with the maximum score every 50 episodes, until episode 1450:

![results](./results.svg)

Note: Decreasing the `epsilon_end_episode` could make the agent achieve better results in a smaller number of episodes.

## Useful Links

#### Deep Q Learning

- PythonProgramming - https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/
- Towards Data Science - https://towardsdatascience.com/self-learning-ai-agents-part-ii-deep-q-learning-b5ac60c3f47
