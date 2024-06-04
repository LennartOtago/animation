import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
#matplotlib.use('Qt5Agg') #use Qt5 as backend, comment this line for default backend
from matplotlib.animation import PillowWriter

from matplotlib import pyplot as plt
from matplotlib import animation
from numpy import random

# O3Res = np.loadtxt('/Users/lennart/PycharmProjects/TwoForOnePlusNonLin/O3Res.txt')
# height_values = np.loadtxt('/Users/lennart/PycharmProjects/TwoForOnePlusNonLin/height_values.txt')
# VMR_O3 = np.loadtxt('/Users/lennart/PycharmProjects/TwoForOnePlusNonLin/VMR_03.txt')

O3Res = np.loadtxt('/home/lennartgolks/PycharmProjects/TwoForOnePlusNonLin/O3Res.txt')
height_values = np.loadtxt('/home/lennartgolks/PycharmProjects/TwoForOnePlusNonLin/height_values.txt')
VMR_O3 = np.loadtxt('/home/lennartgolks/PycharmProjects/TwoForOnePlusNonLin/VMR_O3.txt')
PressResults = np.loadtxt('/home/lennartgolks/PycharmProjects/TwoForOnePlusNonLin/PressRes.txt')
pressure_values = np.loadtxt('/home/lennartgolks/PycharmProjects/TwoForOnePlusNonLin/pressure_values.txt')



#heightMat = height_values.reshape((num_points,1)) * np.ones((num_points, num_lines))

ResCol = "#1E88E5"


# ##
# muProf = []
#
# for j in  range(1,num_lines):
#     fig, axs = plt.subplots(1,2)
#     ax0 = axs[0]
#     ax1 = axs[1]
#     p0 = ax0.plot([],[], color=ResCol, marker='+', markersize=1, linewidth=0.25)
#     p1 = ax1.plot([],[], color=ResCol, marker='+', markersize=1, linewidth=0.25)
#     truP = ax0.plot(pressure_values,height_values,marker = 'o',markerfacecolor = 'k', color = 'k' , label = 'true profile', zorder=1 ,linewidth = 1.5, markersize =7)
#     truO3 = ax1.plot(VMR_O3,height_values,marker = 'o',markerfacecolor = 'k', color = 'k' , label = 'true profile', zorder=1 ,linewidth = 1.5, markersize =7)
#
#     for i in range(0,j):
#         line1 = ax1.plot(O3Res[i, :], height_values, color=ResCol, marker='+', markersize=1, linewidth=0.25, alpha= ((num_lines - j+80) / (num_lines+80)))
#         p1[0].set_label('sample ' + str(j))
#         ax1.legend(handles=[truO3[0], p1[0]])
#         line0 = ax0.plot(PressResults[i, :], height_values, color=ResCol, marker='+', markersize=1, linewidth=0.25, alpha= ((num_lines - j+80) / (num_lines+80)))
#         p0[0].set_label('sample ' + str(j))
#         ax0.legend(handles=[truP[0], p0[0]])
#     if j == num_lines-1:
#         muProfO3 = ax1.plot(np.mean(O3Res,0), height_values, color='green', marker='v', markersize=7, linewidth=1, label = 'sample mean')
#         ax1.legend(handles = [truO3[0], p1[0], muProfO3[0]])
#         muProfP = ax0.plot(np.mean(PressResults,0), height_values, color='green', marker='v', markersize=7, linewidth=1, label = 'sample mean')
#         ax0.legend(handles = [truP[0], p0[0], muProfP[0]])
#     ax1.set_xlabel('O3 Mixing Ratio in ppm')
#     #ax1.set_ylabel('Height in km')
#     ax0.set_xlabel('Pressure in hPa')
#     ax0.set_ylabel('Height in km')
#     fig.suptitle('SNR 90')
#     lab = 'sample' + str(j).zfill(3)
#     #legs = ax1.legend(loc='upper right')
#     #ax1.legend(p, ['sample ' + str(j)])
#     # truh, trul = tru[0].get_legend_handles_labels()
#     # ph, pl = p.get_legend_handles_labels()
#     #ax1.legend([truh, ph], [trul, pl])
#
#     #legs.texts[-1].set_text(lab)
#
#     ax1.set_xlim(np.min(O3Res), np.max(O3Res))
#     ax0.set_xlim(-30, np.max(PressResults))
#     ax1.set_ylim(height_values[0],height_values[-1])
#
#     #plt.savefig('/Users/lennart/PycharmProjects/animation/GIF/' + lab + '.png', dpi=400)
#     plt.savefig('/home/lennartgolks/PycharmProjects/animation/GIF/' + lab + '.png', dpi=100)
#
#
#     #plt.show()
#
#     plt.close()



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



## load data for linear part

# O3Res = np.loadtxt('/home/lennartgolks/PycharmProjects/firstModelCheck/O3Res.txt')
# height_values = np.loadtxt('/home/lennartgolks/PycharmProjects/firstModelCheck/height_values.txt')
# VMR_O3 = np.loadtxt('/home/lennartgolks/PycharmProjects/firstModelCheck/VMR_O3.txt')
# RegSol = np.loadtxt('/home/lennartgolks/PycharmProjects/firstModelCheck/RegSol.txt')
# y = np.loadtxt('/home/lennartgolks/PycharmProjects/firstModelCheck/dataY.txt')
# tan_height_values = np.loadtxt('/home/lennartgolks/PycharmProjects/firstModelCheck/tan_height_values.txt')

O3Res = np.loadtxt('/home/lennartgolks/PycharmProjects/NonLinModel/O3Res.txt')
height_values = np.loadtxt('/home/lennartgolks/PycharmProjects/NonLinModel/height_values.txt')
VMR_O3 = np.loadtxt('/home/lennartgolks/PycharmProjects/NonLinModel/VMR_O3.txt')
y = np.loadtxt('/home/lennartgolks/PycharmProjects/NonLinModel/NonLinDataY.txt')
tan_height_values = np.loadtxt('/home/lennartgolks/PycharmProjects/NonLinModel/tan_height_values.txt')


num_lines, num_points = O3Res.shape
num_lines = 100


## just plot first pic

# muProf = []
# RegCol = "#D81B60"#"#D55E00"
# fig, ax1 = plt.subplots()
# ax2 = ax1.twiny()  # ax1 and ax2 share y-axis
# data = ax2.scatter(y/1e11, tan_height_values, color='gray', marker='x', s=15, label='data', zorder = 0)
# #ax2.spines[:].set_visible(False)
# #ax2.set_xticks([])
# tru = ax1.plot(VMR_O3,height_values,marker = 'o',markerfacecolor = 'k', color = 'k' , label = 'true profile', zorder=1 ,linewidth = 1.5, markersize =7)
# i = 0
# p2 = ax1.plot(O3Res[i, :], height_values, color=ResCol, marker='+', markersize=1, linewidth=0.25, label = 'sample ' + str(i))
#
#
# ax1.legend(handles = [tru[0],p2[0], data], loc = "upper right")
# ax2.set_xlabel(r'Spectral Ozone radiance in $\frac{W}{m^2 sr} \times \frac{1}{\frac{1}{cm}}$',labelpad=10 )# color =dataCol,
# #ax2.set_xlabel(r'Spectral radiance in $\frac{\text{W } \text{cm}}{\text{m}^2 \text{ sr}} $',labelpad=10)# color =dataCol,
#
# ax1.set_xlabel('Ozone Mixing Ratio in ppm')
# ax1.set_ylabel('Height in km')
#
#
#
# ax1.set_xlim(np.min(O3Res), np.max(O3Res))
# ax1.set_ylim(height_values[0],height_values[-1])
# plt.savefig('/home/lennartgolks/PycharmProjects/animation/firstNonLin.png', dpi=100)
#
# #plt.show()
#
# plt.close()


##
muProf = []
RegCol = "#D81B60"#"#D55E00"
for j in  range(1,num_lines):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twiny()  # ax1 and ax2 share y-axis
    data = ax2.scatter(y, tan_height_values, color='gray', marker='x', s=15, label='data', zorder = 0)
    ax2.spines[:].set_visible(False)
    ax2.set_xticks([])
    tru = ax1.plot(VMR_O3,height_values,marker = 'o',markerfacecolor = 'k', color = 'k' , label = 'true profile', zorder=1 ,linewidth = 1.5, markersize =7)
    p = ax1.plot([],[], color=ResCol, marker='+', markersize=1, linewidth=0.25)


    for i in range(0,j):
        p2 = ax1.plot(O3Res[i, :], height_values, color=ResCol, marker='+', markersize=1, linewidth=0.25, alpha= ((num_lines - j+80) / (num_lines+80)))
        p[0].set_label('sample ' + str(j))
        ax1.legend(handles=[tru[0], p[0]])
    if j == num_lines-1:
        muProf = ax1.plot(np.mean(O3Res,0), height_values, color='green', marker='v', markersize=10, linewidth=1, label = 'sample mean')
        #RegProf = ax1.plot(RegSol, height_values, color=RegCol, marker='s', markersize=3, linewidth=1,label = 'reg. solution')
        #ax1.legend(handles = [tru[0], p[0], muProf[0],RegProf[0], data], loc = "upper right")

        ax1.legend(handles = [tru[0], p[0], muProf[0], data], loc = "upper right")

    ax1.set_xlabel('Ozone Mixing Ratio in ppm')
    ax1.set_ylabel('Height in km')
    ax1.set_title('SNR 40')
    lab = 'sample' + str(j).zfill(3)

    ax1.set_xlim(np.min(O3Res), np.max(O3Res))
    ax1.set_ylim(height_values[0],height_values[-1])
    plt.savefig('/home/lennartgolks/PycharmProjects/animation/GIF/' + lab + '.png', dpi=100)

    #plt.show()

    plt.close()


##
import glob
import contextlib
from PIL import Image

# filepaths
fp_in = "/home/lennartgolks/PycharmProjects/animation/GIF/*.png"
fp_out = "SNR40NonLinear.gif"

# use exit stack to automatically close opened images
with contextlib.ExitStack() as stack:

    # lazily load images
    imgs = (stack.enter_context(Image.open(f))
            for f in sorted(glob.glob(fp_in)))


    # extract  first image from iterator
    img = next(imgs)
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=200)

##

