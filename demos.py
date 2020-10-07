if __name__ == '__main__':

    # This import registers the 3D projection, but is otherwise unused.
    from mpl_toolkits.mplot3d import Axes3D  # nova: Fair unused import
    from mpl_toolkits.mplot3d import axes3d
    from cycler import cycler
    from numpy.random import beta

    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    import numpy as np
    
    plt.style.use('tint')

    # Fixing random state for reproducibility
    np.random.seed(19680801)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.view_init(elev=10, azim=135)

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    x, y = np.random.rand(2, 100) * 4
    hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

    # Construct arrays for the anchor positions of the 16 bars.
    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25,
            indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0

    # Construct arrays with the dimensions for the 16 bars.
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = hist.ravel()

    cmap = cm.get_cmap('tab20_r')
    max_height = np.max(dz)   # get range of colorbars
    min_height = np.min(dz)

    # scale each z to [0,1], and get their rgb values
    rgba = [cmap((k-min_height)/(max_height-min_height)) for k in dz] 

    ax.set_prop_cycle(cycler('color', rgba))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=rgba, zsort='average')


    fig1 = plt.figure()
    ax1 = fig1.gca(projection='3d')

    ax1.set_prop_cycle(cycler('color', rgba))

    ax1.view_init(elev=10, azim=135)

    # Get rid of colored axes planes
    # First remove fill
    ax1.xaxis.pane.fill = False
    ax1.yaxis.pane.fill = False
    ax1.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax1.xaxis.pane.set_edgecolor('w')
    ax1.yaxis.pane.set_edgecolor('w')
    ax1.zaxis.pane.set_edgecolor('w')

    X, Y, Z = axes3d.get_test_data(0.05)

    # Plot the 3D surface
    ax1.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)

    # Plot projections of the contours for each dimension.  By choosing offsets
    # that match the appropriate axes limits, the projected contours will sit on
    # the 'walls' of the graph
    cset = ax1.contour(X, Y, Z, zdir='z', offset=-100)
    cset = ax1.contour(X, Y, Z, zdir='x', offset=-40)
    cset = ax1.contour(X, Y, Z, zdir='y', offset=40)

    ax1.set_xlim(-40, 40)
    ax1.set_ylim(-40, 40)
    ax1.set_zlim(-100, 100)

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')


    fig, axes = plt.subplots(ncols=2, nrows=3)
    ax2, ax3, ax4, ax5, ax6, ax7 = axes.ravel()

    # histograms

    def plot_beta_hist(ax, a, b):
        ax.hist(beta(a, b, size=10000), histtype="stepfilled",
                bins=25, alpha=0.8, density=True)


    plot_beta_hist(ax2, 10, 10)
    plot_beta_hist(ax2, 4, 12)
    plot_beta_hist(ax2, 50, 12)
    plot_beta_hist(ax2, 6, 55)

    ax2.annotate('Annotation', xy=(0.25, 4.25),
                xytext=(0.9, 0.9), textcoords=ax2.transAxes,
                va="top", ha="right",
                bbox=dict(boxstyle="round", alpha=0.2),
                arrowprops=dict(
                          arrowstyle="->",
                          connectionstyle="angle,angleA=-95,angleB=35,rad=10"),
                )




    # sin waves

    x = np.linspace(0, 10)

    ax3.plot(x, np.sin(x) + x + np.random.randn(50))
    ax3.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
    ax3.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
    ax3.plot(x, np.sin(x) - 0.5 * x + np.random.randn(50))
    ax3.plot(x, np.sin(x) - 2 * x + np.random.randn(50))
    ax3.plot(x, np.sin(x) + np.random.randn(50))

    # bar graphs

    x = np.arange(5)
    y1, y2 = np.random.randint(1, 25, size=(2, 5))
    width = 0.25
    ax4.bar(x, y1, width)
    ax4.bar(x + width, y2, width,
            color=list(plt.rcParams['axes.prop_cycle'])[2]['color'])
    ax4.set_xticks(x + width)
    ax4.set_xticklabels(['a', 'b', 'c', 'd', 'e'])


    # scatter plot

    x, y = np.random.normal(size=(2, 200))
    ax5.plot(x, y, 'o')


    # sinusoidal
    L = 2*np.pi
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax6.plot(x, np.sin(x + s), '-')
    ax6.margins(0)


    # circles with colors from default color cycle
    for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
        xy = np.random.normal(size=2)
        ax7.add_patch(plt.Circle(xy, radius=0.3, color=color['color']))
    ax7.axis('equal')
    ax7.margins(0)

    # box plot

    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low))

    fig8, axs = plt.subplots(2, 3)

    # basic plot
    axs[0, 0].boxplot(data)

    # notched plot
    axs[0, 1].boxplot(data, 1)

    # change outlier point symbols
    axs[0, 2].boxplot(data, 0, 'D')

    # don't show outlier points
    axs[1, 0].boxplot(data, 0, '')

    # horizontal boxes
    axs[1, 1].boxplot(data, 0, 's', 0)

    # change whisker length
    axs[1, 2].boxplot(data, 0, 's', 0, 0.75)

    fig8.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                    hspace=0.4, wspace=0)


    x = np.arange(-5, 5, 0.01)
    y1 = -5*x*x + x + 10
    y2 = 5*x*x + x

    fig9, ax9 = plt.subplots()
    ax9.plot(x, y1, x, y2, color='black')
    ax9.fill_between(x, y1, y2, where=y2 >y1, alpha=0.5, edgecolor='white')
    ax9.fill_between(x, y1, y2, where=y2 <=y1, alpha=0.5, edgecolor='white')

    plt.show()
