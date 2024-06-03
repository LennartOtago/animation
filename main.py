import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
#matplotlib.use('Qt5Agg') #use Qt5 as backend, comment this line for default backend
from matplotlib.animation import PillowWriter

from matplotlib import pyplot as plt
from matplotlib import animation
from numpy import random

O3Res = np.loadtxt('/Users/lennart/PycharmProjects/TwoForOnePlusNonLin/O3Res.txt')
height_values = np.loadtxt('/Users/lennart/PycharmProjects/TwoForOnePlusNonLin/height_values.txt')
VMR_O3 = np.loadtxt('/Users/lennart/PycharmProjects/TwoForOnePlusNonLin/VMR_03.txt')
num_lines, num_points = O3Res.shape

heightMat = height_values.reshape((num_points,1)) * np.ones((num_points, num_lines))
#num_lines=5
ResCol = "#1E88E5"
##
#
# fig, ax = plt.subplots()
# x = np.linspace(0,num_lines-1, num_lines)
# ax.plot(x,(num_lines-x+15)/(num_lines+15))
# plt.show()
#
# print('bla')
##
# Save the animation

# fig, ax1 = plt.subplots()
# #ax1 = plt.axes(xlim=(np.min(O3Res), np.max(O3Res)), ylim=(height_values[0],height_values[-1]))
# ax1.plot(VMR_O3,height_values,marker = 'o',markerfacecolor = 'k', color = 'k' , label = 'true profile', zorder=1 ,linewidth = 1.5, markersize =7)
#
# line, = ax1.plot([], [],label='label')
# #L=plt.legend(loc=1)
# ax1.set_xlabel('OzoneValues')
# ax1.set_ylabel('heights')
# #legs = [ax.legend(loc=2, prop={'size': 6})  for ax in ax1]
# legs = ax1.legend(loc='upper right')
# #texts = ax1.text(0.9, 0.9,  '', transform=ax1.transAxes)
# lines = []
# ax1.set_xlim(np.min(O3Res), np.max(O3Res))
# ax1.set_ylim(height_values[0],height_values[-1])
#
# def init():
#     for line in lines:
#         line.set_data([],[])
#     return lines
#
# frame_num = num_lines
#
# def animate(i):
#     lines = []
#     #, alpha = (num_lines - i)/num_lines
#     #(num_lines - i + 15) / (num_lines + 15), alpha =0.1
#     for index in range(0, i):
#         lobj = ax1.plot([], [], color=ResCol, marker='+', markersize=1, linewidth=0.25, alpha=(num_lines - i +30) / (num_lines+30))[0]
#         lines.append(lobj)
#
#     for j,line in enumerate(lines):
#         line.set_data(O3Res[j, :], height_values) # set data for each line separately.
#
#
#     lab = 'sample ' + str(i)
#
#     legs.texts[-1].set_text(lab)
#
#
#     return lines + [legs]
#
# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, frames=frame_num, interval=10, blit=True, repeat =False)
#
#
# plt.show()
#





##
muProf = []

for j in  range(1,num_lines):
    fig, ax1 = plt.subplots()
    p = ax1.plot([],[], color=ResCol, marker='+', markersize=1, linewidth=0.25)
    tru = ax1.plot(VMR_O3,height_values,marker = 'o',markerfacecolor = 'k', color = 'k' , label = 'true profile', zorder=1 ,linewidth = 1.5, markersize =7)

    for i in range(0,j):
        p2 = ax1.plot(O3Res[i, :], height_values, color=ResCol, marker='+', markersize=1, linewidth=0.25, alpha= ((num_lines - j+80) / (num_lines+80)))
        p[0].set_label('sample ' + str(j))
        ax1.legend(handles=[tru[0], p[0]])
    if j == num_lines-1:
        muProf = ax1.plot(np.mean(O3Res,0), height_values, color='green', marker='v', markersize=7, linewidth=1, label = 'sample mean')
        ax1.legend(handles = [tru[0], p[0], muProf[0]])
    ax1.set_xlabel('Ozone Mixing Ratio in ppm')
    ax1.set_ylabel('Height in km')
    ax1.set_title('SNR 4')
    lab = 'sample' + str(j).zfill(3)
    #legs = ax1.legend(loc='upper right')
    #ax1.legend(p, ['sample ' + str(j)])
    # truh, trul = tru[0].get_legend_handles_labels()
    # ph, pl = p.get_legend_handles_labels()
    #ax1.legend([truh, ph], [trul, pl])

    #legs.texts[-1].set_text(lab)

    ax1.set_xlim(np.min(O3Res), np.max(O3Res))
    ax1.set_ylim(height_values[0],height_values[-1])

    plt.savefig('/Users/lennart/PycharmProjects/animation/GIF/' + lab + '.png', dpi=400)

    #plt.show()

    plt.close()


##
import glob
import contextlib
from PIL import Image

# filepaths
fp_in = "/Users/lennart/PycharmProjects/animation/GIF/*.png"
fp_out = "SNR4.gif"

# use exit stack to automatically close opened images
with contextlib.ExitStack() as stack:

    # lazily load images
    imgs = (stack.enter_context(Image.open(f))
            for f in sorted(glob.glob(fp_in)))


    # extract  first image from iterator
    img = next(imgs)
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=None)

##
# import os
#
# path = "/Users/lennart/PycharmProjects/animation/GIF/*.png"
# fileList = glob.glob(path)
# fileList.sort()
#
#
# #images = " ".join([path + filename for filename in filenames])
# #os.system('convert -alpha deactivate -verbose -delay 50 -loop 0 -density 300 {} {}animated.gif'.format(fileList, path))
# os.system('convert -delay 20 -loop 0 *.png animated.gif')
#

# ##
# ResCol = "#1E88E5"
# fig = plt.figure()
# #fig, axes = plt.subplots()
# ax1 = plt.axes(xlim=(np.min(O3Res), np.max(O3Res)), ylim=(height_values[0],height_values[-1]))
# line, = ax1.plot([], [],label='Time: 0')
# L=plt.legend(loc=1)
# plt.xlabel('OzoneValues')
# plt.ylabel('heights')
# #legs = [ax.legend(loc=2, prop={'size': 6})  for ax in axes]
# lines = []
#
#
# def init():
#     for line in lines:
#         line.set_data([],[])
#     return lines
#
# x1,y1 = [],[]
# #x2,y2 = [],[]
#
# # fake data
# frame_num = num_lines
# #gps_data = [-104 - (4 * random.rand(2, frame_num)), 31 + (3 * random.rand(2, frame_num))]
#
#
# def animate(i):
#     lines = []
# #, alpha = (num_lines - i)/num_lines
#     for index in range(0, i):
#         lobj = ax1.plot([], [], color=ResCol, marker='+', markersize=1, linewidth=1.25, alpha = 0.5)[0]
#         lines.append(lobj)
#
#     for j,line in enumerate(lines):
#         line.set_data(O3Res[j, :], height_values) # set data for each line separately.
#     lab = 'sample ' + str(i)
#     #print(lab)
#     L.get_texts()[0].set_text(lab)
#     return lines
#
# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frame_num, interval=100, blit=True, repeat =False)
#
# plt.show()
#anim.save("TLI.gif", dpi=300, writer=PillowWriter(fps=25))