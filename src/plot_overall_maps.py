## basic map
for indx, year in enumerate(sorted(df.year.unique(), reverse=True)):
    df[df.year == year].plot.scatter(x='longitude', y='latitude', figsize=(10, 5), alpha=0.011);
    plt.suptitle(year)
#     plt.savefig(PATH_TO_IMAGES + 'scatters_{}.png'.format(year), dip=600)
#     break
plt.show()

## this one need more space to place map + density
fig, axes = plt.subplots(nrows=3, ncols=2)
fig.delaxes(axes.flatten()[-1])
fig.suptitle('Year based crimes by caterogy, density')
for indx, year in enumerate(sorted(df.year.unique(), reverse=True)):
    axis = axes.flatten()[indx]
    df[df.year == year].plot.scatter(x='longitude', y='latitude', figsize=(50, 40), alpha=0.011, ax=axis);
    axis.title.set_text('Year: ' + str(year));
#     break
plt.tight_layout()

## this one is better
fig, axes = plt.subplots(nrows=5, figsize=(20, 40))
fig.suptitle('Crimes per year, overall')
for indx, year in enumerate(sorted(df.year.unique(), reverse=True)):
    axis = axes.flatten()[indx]
    df[df.year == year].plot.scatter(x='longitude', y='latitude', alpha=0.05, ax=axis);
    axis.title.set_text('Year: ' + str(year));

fig.tight_layout(rect=[0, 0.00, 1, 0.97])

# basic with larger size
for indx, year in enumerate(sorted(df.year.unique(), reverse=True)):
    df[df.year == year].plot.scatter(x='longitude', y='latitude', figsize=(30, 20), alpha=0.011);
    plt.suptitle(year)
    plt.savefig(PATH_TO_IMAGES + 'scatters_{}.png'.format(year), dip=600)
#     break
plt.show()