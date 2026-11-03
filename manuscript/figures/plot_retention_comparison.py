"""Standalone source: python plot_retention_comparison.py (requires matplotlib)."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

r=Path(__file__).resolve().parent
data=json.loads((r/'retention_comparison_data.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':7.2,'axes.linewidth':.5,
                     'pdf.fonttype':42,'ps.fonttype':42,'svg.fonttype':'none'})
METRICS=['F1']   # the paper reports no metric finer than F1
fig,axs=plt.subplots(1,len(METRICS),figsize=(3.25,1.5),sharey=True,squeeze=False)
axs=axs[0]
fig.subplots_adjust(left=.19,right=.97,top=.66,bottom=.2,wspace=.25)
ys=np.array([2,1,0]);gold='#997510';gray='#7b838a'
for ax,metric in zip(axs,METRICS):
    values=data[metric]
    ax.set_xlim(70,102);ax.set_ylim(-.72,2.5)
    for x in [70,80,90,100]:ax.axvline(x,color='#ededed',lw=.5,zorder=0)
    for i,y in enumerate(ys):
        a=values['Restart'][i];b=values['Ours'][i]
        ax.plot([a,b],[y,y],color='#c8cbce',lw=1.1,zorder=1)
        ax.scatter(a,y,s=16,facecolors='white',edgecolors=gray,linewidths=.9,zorder=3)
        ax.scatter(b,y,s=18,facecolors=gold,edgecolors=gold,linewidths=.6,zorder=4)
        ax.annotate(f'{a:.1f}',(a,y),xytext=(0,-9),textcoords='offset points',ha='center',va='center',color='#525960',fontsize=6.7)
        ax.annotate(f'{b:.1f}',(b,y),xytext=(0,7.5),textcoords='offset points',ha='center',va='center',color=gold,fontsize=6.7,fontweight='bold')
    ax.set_title(metric+' (%)',fontsize=8,fontweight='bold',pad=10)
    ax.set_xticks([70,80,90,100]);ax.tick_params(axis='x',labelsize=6.5,length=2,pad=2,color='#999999')
    ax.set_yticks(ys);ax.set_yticklabels(['TSDF','3DGS','Occupancy'],fontsize=7)
    ax.tick_params(axis='y',length=0,pad=5)
    for s in ['top','right','left']:ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#aaaaaa')
from matplotlib.lines import Line2D
handles=[Line2D([0],[0],marker='o',ls='',mfc='white',mec=gray,ms=4,label='Native restart'),
         Line2D([0],[0],marker='o',ls='',mfc=gold,mec=gold,ms=4,label='Ours, continued')]
fig.legend(handles=handles,ncol=2,loc='upper center',bbox_to_anchor=(.53,1.01),frameon=False,
           fontsize=7,columnspacing=1.1,handletextpad=.35)
for ext in ['pdf','svg','png']:
    fig.savefig(r/f'retention_comparison.{ext}',dpi=360,facecolor='white')
plt.close(fig)
