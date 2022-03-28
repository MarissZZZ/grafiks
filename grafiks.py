import matplotlib.pyplot as plt
#plt.style.use('ggplot')

x_ass_koord=['Nav pieredzes','1-2','3-5','5-10','10 un vairāk'] #pieredze
y_ass_koord=[75,84,62,35,44] #gadu pieredze viriesiem
y_ass_koord2=[65,85,58,37,41] #gadu pieredze sievietem

fig, ax = plt.subplots(facecolor=('White'))
ax.set_facecolor('#93E1FC')

plt.xlabel('Gadu pieredze')
plt.ylabel('Cilvēku skaits aptaujā')
plt.title('Darba pieredze')

plt.plot(x_ass_koord,y_ass_koord, label='Vīrieši', linewidth=3, linestyle='dotted', color='blue')
plt.plot(x_ass_koord,y_ass_koord2, label='Sievietes', linewidth=3, color='red')
plt.legend(loc='upper right') #legendas novietojums
plt.show()