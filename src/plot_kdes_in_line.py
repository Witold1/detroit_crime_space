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