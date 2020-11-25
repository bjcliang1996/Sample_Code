import lucem_illud_2020 
import networkx as nx
from collections import OrderedDict
import sklearn #For generating some matrices
import pandas #For DataFrames
import numpy as np #For arrays
import pandas as pd
import matplotlib.pyplot as plt #For plotting
import matplotlib
import seaborn as sns #Makes the plots look nice
import scipy #Some stats
import nltk #a little language code
from IPython.display import Image #for pics
import zipfile
import sys
import pickle #if you want to save layouts
import os
import sklearn.feature_extraction
import zipfile
from networkx.algorithms.community import greedy_modularity_communities
import spacy
import plotly.graph_objects as go
import math

nlp = spacy.load('en')


target_word = dict()
target_word['economy']  = ['business', 'finance',
                           'enterprise', 'tax', 'market',
                           'trade', 'monetary', 'tariff', 'bank']

target_word['religion'] = ['christian', 'church', 'religion', 'god', 
                           'baptist', 'bible', 'protestant', 'catholic',
                           'religious']

target_word['defense']  = ['communist', 'defense', 'army', 'terrorism', 
                           'nuclear', 'islam', 'military',
                           'regime', 'troop', 'submarine', 'iran']

target_word['congress'] = ['senator', 'congress', 'vote', 'election']

target_word['health']   = ['health', 'medicine', 'medication', 
                           'hospital', 'medicare', 'medicaid']

target_word['woman'] = ['baby', 'abortion', 'pregnant', 'parenthood', 'childbearing']

target_word['gun']  = ['gun', 'firearm', 'shooting']

target_word['tech'] = ['nasa', 'cyber', 'cybersecurity','scientist', 'hacker']

target_word['environment'] = ['environmental', 'conservation', 'renewable', 'energy',
                              'resort', 'pollution']

target_word['lgbt'] = ['homosexual', 'gay', 'lgbt', 'sexual',
                       'transgender', 'lgbtq']

target_word['immigration'] = ['immigrant', 'immigration', 'border', 'mexican',
                              'crossing', 'deportation']

target_word['school'] = ['tenure', 'school', 'tuition', 'student', 'teacher']



def normalizeTokens(word_list, extra_stop=[], model=nlp, lemma=True, MAX_LEN=1500000):
    #We can use a generator here as we just need to iterate over it
    normalized = []
    if type(word_list) == list and len(word_list) == 1:
        word_list = word_list[0]

    if type(word_list) == list:
        word_list = ' '.join([str(elem) for elem in word_list]) 

    # since we're only normalizing, I remove RAM intensive operations and increase max text size

    model.max_length = MAX_LEN
    doc = model(word_list.lower(), disable=["parser", "tagger", "ner"])

    if len(extra_stop) > 0:
        for stopword in extra_stop:
            lexeme = nlp.vocab[stopword]
            lexeme.is_stop = True

    # we check if we want lemmas or not earlier to avoid checking every time we loop
    if lemma:
        for w in doc:
            # if it's not a stop word or punctuation mark, add it to our article
            if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and len(w.text.strip()) > 0:
            # we add the lematized version of the word
                normalized.append(str(w.lemma_))
    else:
        for w in doc:
            # if it's not a stop word or punctuation mark, add it to our article
            if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and len(w.text.strip()) > 0:
            # we add the lematized version of the word
                normalized.append(str(w.text.strip()))

    return normalized


def normalize(vector):
    normalized_vector = vector / np.linalg.norm(vector)
    return normalized_vector

def dimension(model, words):
    return sum([normalize(model[x]) for x in words])

def plot_clusters(df_plot, x, names):
    year, ax = x[0], x[1][0]
    cut = df_plot[df_plot['year']==year]
    
    palette = dict(zip(names, sns.color_palette("Paired", 12)))
    #print(palette)
    sns.scatterplot(x = cut["pca1"], y = cut["pca2"], 
                    hue = cut['topic'], s=20, ax= ax,
                    ci=None, palette=palette)
        
    ax.set_title(f'Year = {year}', fontsize=20)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    return plt

## the following weren't used in the end

def graph_year(data, yr):
    cut = data[data['Year']==yr]
    cat = list(cut['t1']) + list(cut['t2'])
    dist = Counter(cat)
    total = sum(dist.values())
    for k in dist: dist[k] = dist[k]/total
    ind = [dist[k] for k in names]
    return graph(np.array(ind)*3, names)


def get_grid(x):
    return (x/2, math.sqrt(3)*x/(2))


def get_path(arr):
    arr = np.array(arr)
    grids = [get_grid(x) for x in arr]
    path = f"M-{grids[0][0]},{grids[0][1]}"  ## A
    path += f"L{grids[1][0]},{grids[1][1]}" ## B
    path += f"L{arr[2]},0" ## C
    path += f"L{grids[3][0]},-{grids[3][1]}" ## D
    path += f"L-{grids[4][0]},-{grids[4][1]}" ## E
    path += f"L-{arr[5]},{0}Z" ## F
    return path

def graph(index, names, color = "LightSeaGreen"):
    index = np.array(index) * 2
    b = math.sqrt(3)
    fig = go.Figure()

    fig.update_xaxes(
        range=[-4, 4],
        zeroline=False,
        showgrid=False,
        showticklabels=False
    )

    fig.update_yaxes(
        range=[-4, 4],
        zeroline=False,
        showgrid=False,
        showticklabels=False
    )
    fig.add_trace(go.Scatter(
        x=[-1, 1, -1, 1, -2, 2], y=[b, b,-b, -b,0, 0],
        mode="lines+markers+text",
        text= [names[0], names[1],names[4],names[3],names[5],names[2]],
        textposition=["top center", "top center", "bottom center",
                  "bottom center","middle left", "middle right"],
        textfont_size=14,
        marker={"color": 'rgba(0,0,0,0)'}
    ))

    fig.update_layout(
        autosize=False,
        width=500,
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
    
        shapes=[
            dict(
                type="path",
                path=f"M-1,-{b} L-2,0 L-1,{b}, L1,{b} L2,0 L1,-{b}Z",
                fillcolor="PaleTurquoise",
                line_color="LightSeaGreen",
            ),
        
            dict(
                type="line",
                xref="x", yref="y",
                x0=-1, y0=-b, x1=1, y1=b,
                line=dict(
                    color="LightSeaGreen",
                    width=1, dash='dash'),
            ),
        
            dict(
                type="line",
                xref="x", yref="y",
                x0=-2, y0=0, x1=2, y1=0,
                line=dict(
                    color="LightSeaGreen",
                    width=1, dash='dash'),
            ),
        
            dict(
                type="line",
                xref="x", yref="y",
                x0=-1, y0=b, x1=1, y1=-b,
                line=dict(
                    color="LightSeaGreen",
                    width=1, dash='dash'),
            ),
        ]
    )
    

    fig.add_shape(
        type="path",
        path=get_path(index),
        fillcolor=color,
        line_color=color,
    )

    fig.update_layout(showlegend=False)
    return fig