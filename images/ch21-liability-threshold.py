import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rcParams
from scipy import stats

rcParams['font.family'] = 'AppleGothic'
rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(1, 1, figsize=(11, 8))

# --- Bell curve ---
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x)

male_t = 1.5
female_t = 2.2

# Fill areas
ax.fill_between(x, y, alpha=0.08, color='#666666')
ax.fill_between(x[(x >= male_t) & (x <= female_t)],
                y[(x >= male_t) & (x <= female_t)],
                alpha=0.25, color='#888888')
ax.fill_between(x[x >= female_t], y[x >= female_t],
                alpha=0.5, color='#444444')

# Curve
ax.plot(x, y, color='#333333', linewidth=2.5)

# Population mean
ax.axvline(x=0, color='#aaaaaa', linewidth=1, linestyle='--', ymin=0.02, ymax=0.85)
ax.text(0, 0.43, '인구 평균', fontsize=12, ha='center', va='bottom', color='#888888')

# Male threshold (blue)
ax.plot([male_t, male_t], [0, 0.33], color='#1565c0', linewidth=3)
ax.text(male_t, 0.35, '♂', fontsize=26, ha='center', va='bottom', color='#1565c0', fontweight='bold')

# Female threshold (red)
ax.plot([female_t, female_t], [0, 0.26], color='#c62828', linewidth=3)
ax.text(female_t, 0.28, '♀', fontsize=26, ha='center', va='bottom', color='#c62828', fontweight='bold')

# Arrow between thresholds
ax.annotate('', xy=(female_t - 0.05, 0.23), xytext=(male_t + 0.05, 0.23),
            arrowprops=dict(arrowstyle='<->', color='#555555', lw=1.5))

# Diagnosed label
ax.text(3.2, 0.045, '진단받은\n사람들', fontsize=12, ha='center', color='#333333')

# Male range bracket - moved down
ax.annotate('', xy=(male_t, -0.018), xytext=(4.0, -0.018),
            arrowprops=dict(arrowstyle='-[', color='#1565c0', lw=1.5, mutation_scale=12))
ax.text(2.75, -0.04, '남성 진단 범위', fontsize=11, ha='center', color='#1565c0')

# Female range bracket - more space below
ax.annotate('', xy=(female_t, -0.065), xytext=(4.0, -0.065),
            arrowprops=dict(arrowstyle='-[', color='#c62828', lw=1.5, mutation_scale=12))
ax.text(3.1, -0.09, '여성 진단 범위 (더 높은 부담 필요)', fontsize=11, ha='center', color='#c62828')

# --- Gradient triangle --- moved lower
tri_top = -0.135
tri_height = 0.05
n_seg = 300
for i in range(n_seg):
    xl = -3.5 + (7.0 * i / n_seg)
    xr = -3.5 + (7.0 * (i + 1) / n_seg)
    h = tri_height * ((i + 1) / n_seg)
    gray = 0.88 - 0.58 * (i / n_seg)
    rect = patches.Rectangle((xl, tri_top - h), xr - xl, h,
                              facecolor=str(gray), edgecolor='none')
    ax.add_patch(rect)

# Variant labels - bigger font, more space
labels = [
    (-2.5, '공통 유전 변이'),
    (-0.2, '희귀 유전 변이'),
    (1.8, '신생 유전 변이'),
    (3.3, '염색체 이상'),
]
for xpos, label in labels:
    ax.text(xpos, tri_top - 0.08, label, fontsize=11, ha='center', va='top', color='#444444')

ax.text(3.9, tri_top - 0.02, '개별 효과\n크기 →', fontsize=9, ha='left', va='center', color='#666666')

# Axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position(('data', -4))
ax.spines['bottom'].set_position(('data', 0))
ax.plot(-4, 0.46, '^k', markersize=8, clip_on=False)
ax.plot(4.2, 0, '>k', markersize=8, clip_on=False)

ax.set_ylabel('인구집단의 비율', fontsize=14, labelpad=15, rotation=90)
ax.set_xlabel('자폐 특성의 정도 →', fontsize=14, labelpad=10)
ax.xaxis.set_label_coords(0.5, -0.08)

ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-4.3, 4.6)
ax.set_ylim(-0.24, 0.49)

plt.tight_layout()
plt.savefig('/Users/joonan/chaek/autism/images/ch21-liability-threshold.svg',
            format='svg', bbox_inches='tight', dpi=150)
plt.savefig('/Users/joonan/chaek/autism/images/ch21-liability-threshold.png',
            format='png', bbox_inches='tight', dpi=150)
print("Done")
