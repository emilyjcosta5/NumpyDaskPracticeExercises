z = np.mean(stem_4d, axis=0)
a = np.mean(z, axis=0)
a = np.float32(a)
fig, axis = plt.subplots()
axis.imshow(a)
