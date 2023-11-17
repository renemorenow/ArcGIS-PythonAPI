# import numpy as np
# import matplotlib
# from matplotlib import pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import confusion_matrix
# from sklearn.ensemble import RandomForestClassifier

# mndata = MNIST('MNIST_data')
# mndata
# datos, labels = mndata.load_training()

# plt.gray()

# for i in range(25):
# 	plt.subplot(5, 5, i+1)
# 	d_image = datos[i]
# 	d_image = np.array(d_image, dtype='float')
# 	pixels = d_image.reshape((28, 28))
# 	plt.imshow(pixels, cmap='gray')
# 	plt.title(labels[i])
# 	plt.axis('off')
# plt.show()

import connectionDB
esquema = connectionDB.Connection_DB.esquema_sgc
result = []
with connectionDB.Connection_DB("postgres") as cnn_DB:
	cursor = cnn_DB.execute_query("select user")
	result = cursor.fetchall()
print(str(result))