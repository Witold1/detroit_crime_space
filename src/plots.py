'''
The reserve code of some plots temporary out of a proper module or a notebook
'''

# %%time
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(30, 30))
fig.suptitle('By category against')

for indx, cat_ag in enumerate(sorted(df['Crime Against'].unique(), reverse=True)[0:3]):
    indx *= 2 if indx > 0 else 1
    axis_map = axes.flatten()[indx]
    axis_density = axes.flatten()[indx+1]
    try:
        df_to_plot = df[df['Crime Against'] == cat_ag].sample(5000) # take a N sample to reduce kde computation
        df_to_plot[df_to_plot['Crime Against'] == cat_ag].plot.scatter(x='longitude', 
                                                                       y='latitude', 
                                                                       #figsize=(10, 5), 
                                                                       alpha=0.051, ax=axis_map)
        sns.jointplot(x=df_to_plot[df_to_plot['Crime Against'] == cat_ag]['X'], 
                      y=df_to_plot[df_to_plot['Crime Against'] == cat_ag]['Y'], 
                      kind='kde', ax=axis_density)
    except:
        df[df['Crime Against'] == cat_ag].plot.scatter(x='longitude', y='latitude', 
                                                       #figsize=(10, 5), 
                                                       alpha=0.051, 
                                                       ax=axis_map)
        sns.jointplot(x=df[df['Crime Against'] == cat_ag]['X'], 
                      y=df[df['Crime Against'] == cat_ag]['Y'], 
                      kind='kde', ax=axis_density)
    axis_map.title.set_text(cat_ag + ', map');
    axis_density.title.set_text(cat_ag + ', density')
#fig.tight_layout();

%%time
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15,10))
fig.delaxes(axes.flatten()[-1])
fig.suptitle('Year based crimes by caterogy, density')
for indx, year in enumerate(sorted(df.year.unique(), reverse=True)):
    axis = axes.flatten()[indx]
    sns.jointplot(df[df.year == year]['X'], df[df.year == year]['Y'], kind='kde', ax=axis)
    axis.title.set_text('Year: ' + str(year));
    break
plt.tight_layout()

%%time
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
fig.delaxes(axes.flatten()[-1])
fig.suptitle('By category against')

for indx, cat_ag in enumerate(sorted(df['Crime Against'].unique(), reverse=True)[0:3]):
    axis = axes.flatten()[indx]
    axis.title.set_text(cat_ag);
    try: # I forgot the reason of this all exception handling block, but let it be
        df_to_plot = df[df['Crime Against'] == cat_ag].sample(5000)
        sns.jointplot(df_to_plot[df_to_plot['Crime Against'] == cat_ag]['X'], 
                      df_to_plot[df_to_plot['Crime Against'] == cat_ag]['Y'], kind='kde', ax=axis)
    except:
        sns.jointplot(df[df['Crime Against'] == cat_ag]['X'], 
                      df[df['Crime Against'] == cat_ag]['Y'], kind='kde', ax=axis)
    break
#plt.plot();

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