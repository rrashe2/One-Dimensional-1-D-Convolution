#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.,0.,1.,1.,1.,1.,1.,1.,1.,1.])
print(x)

fig1 = plt.figure(1)
plt.stem(x)
plt.pause(0.0001)

k = np.arange(-2.,8.,1.)

fig2 = plt.figure(2)
plt.stem(k,x)
plt.show()

N = 10
M = 20

x = np.hstack([np.zeros(shape=(N)), np.ones(shape=(M+1))])

k = np.arange(-10.,21.,1.)

x1 = np.hstack([np.zeros(shape=(N-5)), np.ones(shape=(M-4))])

fig1 = plt.figure(1)
plt.stem(k,x)
plt.title("u[n]")
plt.pause(0.0001)

k = np.arange(0.,21.,1.)
fig2 = plt.figure(2)
plt.stem(k,x1)
plt.title("u[n-5]")

k = np.arange(-40.,81.,1.)

x = np.hstack([(7*np.cos(0.1*k)) + np.cos(0.95*k)])


fig1 = plt.figure(1)
plt.stem(k,x)
plt.title("u[n]")

x1 = np.hstack([(7*np.cos(0.1*(k-20))) + np.cos(0.95*(k-20))])


fig1 = plt.figure(2)
plt.stem(k,x1)
plt.title("u[n-20]")

h = 1./5.*np.array([1.,1.,1.,1.,1.])

x = np.hstack([np.ones(shape=20)])

y = np.convolve(h,x, mode = 'full')

fig1 = plt.figure(1)
plt.stem(y)
plt.title("y[n]")

k =  np.arange(-40.,81.,1.)
x = np.hstack([np.cos(0.1*k)])

y = np.convolve(h,x, mode = 'full')

fig1 = plt.figure(1)
plt.stem(y)
plt.title("y[n]")

x = np.hstack([np.cos(0.95*k)])

y = np.convolve(h,x, mode = 'full')

fig1 = plt.figure(1)
plt.stem(y)
plt.title("y[n]")

h = np.array([1.,-1.])

x = np.hstack([np.ones(shape=20)])

y = np.convolve(h,x, mode = 'full')

fig1 = plt.figure(1)
plt.stem(y)
plt.title("y[n]")


h = np.array([1.,-1.])
k =  np.arange(-40.,81.,1.)
x = np.hstack([(7*np.cos(0.1*k)) + np.cos(0.95*k)])

y = np.convolve(h,x, mode = 'full')

fig1 = plt.figure(1)
plt.stem(y)
plt.title("y[n]")


