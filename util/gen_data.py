import numpy as np
import pandas as pd

def gen_people(n, height_mean, height_std, weight_mean, weight_std, gender_label):
  hs = np.random.normal(height_mean, height_std, n)
  ws = np.random.normal(weight_mean, weight_std, n)
  gs = np.array(n * [gender_label])
  return np.array([hs, ws, gs]).T

def gen_people_default(n, female_label=1, male_label=2):
  female = gen_people(n, 158, 6.096, 54.8, 9.07185, female_label)
  male = gen_people(n, 172, 6.35, 69.5, 9.07185, male_label)

  all = np.vstack((female, male))
  np.random.shuffle(all)

  df = pd.DataFrame(all, columns=['height', 'weight', 'gender'])
  df['gender'] = df['gender'].astype(int)
  return df