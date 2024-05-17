#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:04:18 2024

@author: alexandre
"""



import numpy as np
import pandas as pd
import geopandas as gpd
import json






def main(risque):
    
    if risque.startswith('equip'):
        risque = 'equipement'
    elif risque.startswith('incap'):
        risque = 'incapacite'
    elif risque.startswith('illec'):
        risque = 'illectronisme'
        
        
    #Communes moins 200 habitants
    data_moins200 = gpd.read_file('res/moins 200/moins200.geojson')
    data_moins200 = data_moins200[['code_iris', 'nom_iris', 'nom_com', 'vulnum_2019_Pop 2019', 'geometry']]
    data_moins200.rename(columns={'vulnum_2019_Pop 2019': 'Pop 2019'}, inplace=True)
    data_moins200 = data_moins200[data_moins200['Pop 2019']<200]

    
    data_equip = gpd.read_file(f'res/risque/{risque}.geojson')
    data_equip.rename(columns={f'ad_clusters_fr_{risque}_19_cluster': 'cluster'}, inplace=True)
    data_equip = data_equip[~data_equip['code_iris'].isin(data_moins200['code_iris'])]
    data_equip.reset_index(drop=True, inplace=True)

    dic_nom_cluster = {'0': 'Exposition non significative', '1': 'Très faible exposition', '2': 'Faible exposition',
                       '3': 'Exposition modérée', '4': 'Forte exposition', '5': 'Très forte exposition'}

    list_nom_cluster = []
    for i in range(len(data_equip)):
        cluster = int(data_equip['cluster'][i])
        nom_cluster = dic_nom_cluster[str(cluster)]
        list_nom_cluster.append(nom_cluster)
        
    data_equip['nom_cluster'] = list_nom_cluster


    json_equip = data_equip.set_index('code_iris', drop=True)
    json_equip = json_equip.to_json()
    json_equip = json.loads(json_equip)
    dic_cluster = data_equip.set_index('code_iris')['cluster']



    geo_equip = data_equip[['code_iris', 'nom_iris', 'insee_com', 'nom_com', 'nom_cluster', 'geometry']]
    info_equip = data_equip[['code_iris', 'nom_iris', 'insee_com', 'nom_com', 'nom_cluster']]



    list_clusters = [0,1,2,3,4,5]
    dic_cluster_color = {'0': '#099268', '1': '#51cf66', '2': '#c0eb75',
                         '3': '#ffd43b', '4': '#ffa94d', '5': '#f03e3e'}

    dic_data_cluster = {}
    for i in list_clusters:
        data = data_equip[data_equip['cluster']==i]
        data.reset_index(drop=True, inplace=True)
        
        geo_data = data[['code_iris', 'nom_iris', 'nom_com', 'nom_cluster','geometry']]
        geo_data = geo_data.to_json()
        geo_data = json.loads(geo_data)
        
        info_data = data[['code_iris', 'nom_iris', 'nom_com', 'nom_cluster']]
        
        i = str(i)
        dic_data_cluster[i] = {}
        dic_data_cluster[i]['geo_data'] = geo_data
        dic_data_cluster[i]['info_data'] = info_data
        dic_data_cluster[i]['color'] = dic_cluster_color[i]
        
        
        
    return({'data': data_equip, 'dic_cluster': dic_data_cluster, 'data_moins200': data_moins200})
    
    
    
    
    
    