from healthcare_quality.clean_data import merged_df
import plotly.graph_objects as go
import plotly.offline as pyo

location_df=merged_df[merged_df['location'].notnull()].reset_index()

for i, row in location_df.iterrows():
    location_df.loc[i,'lat']=row['location']['coordinates'][1]
    location_df.loc[i,'lon']=row['location']['coordinates'][0]


location_df['state']=location_df['state'].astype('object')

fig=go.Figure()
datayes=location_df[location_df['is-MUA?']=='Yes']
datano=location_df[location_df['is-MUA?']=='No']
fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = datayes.lon,
        lat = datayes.lat,    
        name='MUA',
        hoverinfo="text",
        text = datayes.facility_name + ' <br> ' + datayes.city + ' , ' + datayes.state,
        mode = 'markers',
        marker = dict(
            size = 4,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Portland',
            cmin=0,
            color = location_df['rate_of_readmission'],
            colorbar= dict(len=0.5, title="Rate of Readmission"))))
fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = datano.lon,
        lat = datano.lat,
        name='not MUA', 
        hoverinfo="text",
        text = datano.facility_name + ' <br> ' + datano.city + ' , ' + datano.state,
        mode = 'markers',
        marker = dict(
            size = 4,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Portland',
            cmin=0,
            color = location_df['rate_of_readmission'],
            colorbar= dict(len=0.5, title="Rate of Readmission"))))
fig.update_layout(
    legend=dict(x=-.1, y=.9),
    autosize=False,
    width=600, height=250,
    margin=go.layout.Margin(
        l=1,r=1,b=1,t=1, pad=0
    ),
        geo = dict(
            scope='usa',
            projection_type='albers usa',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = .5,
            subunitwidth = .5
        ),
    )


fig.show()


fig.write_image('healthcare_quality/plots/map.png', width=600, height= 300, scale=3)