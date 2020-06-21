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