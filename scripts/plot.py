import matplotlib.pyplot as plt


beam_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bleu_scores = [17.7, 18.4, 18.6, 18.5, 18.8, 18.8, 18.9, 18.7, 18.7, 18.7]
time_taken = [146, 66, 77, 95, 125, 197, 212, 264, 309, 304]

fig1, ax1 = plt.subplots(figsize=(7, 5))
ax1.plot(beam_sizes, bleu_scores, marker='o', color='#2980b9', linewidth=2, markersize=6)
ax1.set_title('Impact of Beam Size on BLEU Score', fontsize=12, fontweight='bold', pad=15)
ax1.set_xlabel('Beam Size (K)', fontsize=10)
ax1.set_ylabel('SacreBLEU Score', fontsize=10)
ax1.set_xticks(beam_sizes)
ax1.grid(True, linestyle='--', alpha=0.5)

for i, txt in enumerate(bleu_scores):
    ax1.annotate(f'{txt}', (beam_sizes[i], bleu_scores[i]), 
                 textcoords="offset points", xytext=(0, 10), 
                 ha='center', fontsize=9, fontweight='bold', color='#1a365d')

ax1.set_ylim(17.0, 19.5) 
plt.tight_layout()
plt.savefig('beam_bleu.png', dpi=300)
plt.close(fig1)


fig2, ax2 = plt.subplots(figsize=(7, 5))
ax2.plot(beam_sizes, time_taken, marker='s', color='#e74c3c', linewidth=2, markersize=6)
ax2.set_title('Impact of Beam Size on Translation Time', fontsize=12, fontweight='bold', pad=15)
ax2.set_xlabel('Beam Size (K)', fontsize=10)
ax2.set_ylabel('Time Taken (seconds)', fontsize=10)
ax2.set_xticks(beam_sizes)
ax2.grid(True, linestyle='--', alpha=0.5)

for i, txt in enumerate(time_taken):
    if i == 0:
        ax2.annotate(f'{txt}s', (beam_sizes[i], time_taken[i]), 
                     textcoords="offset points", xytext=(0, -15), 
                     ha='center', fontsize=9, fontweight='bold', color='#2c3e50')
    else:
        ax2.annotate(f'{txt}s', (beam_sizes[i], time_taken[i]), 
                     textcoords="offset points", xytext=(0, 10), 
                     ha='center', fontsize=9, fontweight='bold', color='#2c3e50')


ax2.set_ylim(40, 350) 
plt.tight_layout()
plt.savefig('beam_time.png', dpi=300)
plt.close(fig2)

print("yes 'beam_bleu.png'  'beam_time.png' ")