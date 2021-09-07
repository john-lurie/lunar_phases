from matplotlib import pyplot as plt

from draw import draw_phase

# Draw the phases in one degree increments.
phases = range(361)

for phase in phases:
    draw_phase(phase)
    plt.savefig('frames/phase_{:03d}.png'.format(phase), bbox_inches='tight',
                dpi=100)
    plt.close()
