# DetroitCrime.space | calvinhacks2020
> Visualise police crime reports. Enforce "Police Data Initiative".

## What it does
It visualizes, analyzes and 'predicts' the crime reports (data provided by participated police departments) published from Police Data Initiative.

<table>
  <tr>
    <td> <i>Offenses against society</i> </td>
    <td> <i>Overall</i> </td>
  </tr>
  <tr>
    <td><img src="https://i.imgur.com/xXb3CyG.png" align="center" alt="Crimes against society at Detroit, draft" width="80%">
    </td>
    <td><img src="https://i.imgur.com/5tt9afQ.png" align="center" alt="Crimes against society at Detroit, draft" width="80%"></td>
  </tr>
</table>

## How I built it
I did find and use the crimes report dataset for the largest Michigan city. Then download it and push the raw data to MongoDB Atlas cloud database. Then made a connection with a database to process data with python scripts and saved it locally because of the resources optimization. At this step I also used geocoding, to encode some needed string addresses to geo-features (Latitude and Longitude pairs). And the final step was the insights selection, trends analysis, and static and dynamic visualization via python frameworks and webGL (probably, one of the best and stable solution to such large geospatial dataset).

## How to use it?
* Link [nbviewer](https://nbviewer.jupyter.org/github/Witold1/calvinhacks2020/blob/master/Untitled.ipynb#PRESENTATION) and [html](.) to processing and visualisation Jupyter notebook. 
* [Link to kepler.gl](https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/u0aqfbui3muxmoq/keplergl_2ndwn6n.json). May be hard to use becouse of the high 3d engine resourse consumption.

<p align="center">
  <img src="https://i.imgur.com/GNEk3Ob.jpg" align="center" alt="The first slice of a timeline" width="90%" height="70%">
</p>
