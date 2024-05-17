#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:09:38 2024

@author: alexandre
"""



def main():

    apl_txt = '''*la présence d'au moins une incapacité parmi la liste suivante:
    la recherche d'information, la communication, la résolution de problèmes et l'usage de logiciels.'''
    
    zonage_txt = '''**l’illectronisme désigne le fait de ne pas posséder les compétences numériques
    de base : envoyer des courriers électroniques, consulter ses comptes en ligne, utiliser des logiciels, etc.)
    ou de ne pas se servir d’Internet (incapacité ou impossibilité matérielle).'''
    
    
    
    col_0, col_1, col_2, col_3, col_4, col_5, col_200 = '#099268','#51cf66','#c0eb75','#ffd43b','#ffa94d','#f03e3e', 'lightgrey'
    
    
    legend_html = f"""
    <div style="margin-top: 20px;">
        <p style="margin-bottom: 5px;"><b>Vulnérabilité numérique:</b></p>
        
        <div class="legend-item">
            <div class="legend-color" style="background-color: {col_0};"></div>
            <div class="legend-text">Exposition non significative</div>
        </div>
        
        <div class="legend-item">
            <div class="legend-color" style="background-color: {col_1};"></div>
            <div class="legend-text">Très faible exposition</div>
        </div>
        
        <div class="legend-item">
            <div class="legend-color" style="background-color: {col_2};"></div>
            <div class="legend-text">Faible exposition</div>
        </div>
        
        <div class="legend-item">
            <div class="legend-color" style="background-color: {col_3};"></div>
            <div class="legend-text">Exposition modérée</div>
        </div>
        
        <div class="legend-item">
            <div class="legend-color" style="background-color: {col_4};"></div>
            <div class="legend-text">Forte exposition</div>
        </div>
        
        <div class="legend-item">
            <div class="legend-color" style="background-color: {col_5};"></div>
            <div class="legend-text">Très forte exposition</div>
        </div>
        
        <div class="legend-item">
            <div class="legend-color" style="background-color: {col_200};"></div>
            <div class="legend-text">IRIS de moins de 200 habitants</div>
        </div>
        
    </div>
    """


    
    legende = f"""
    <div style="position: fixed; bottom: 50px; right: 10px; width: 300px;
                z-index: 1000; background-color: rgba(255, 255, 255, 0.8);
                border-radius: 5px; padding: 10px; font-size: 10px; line-height: 1.5; word-wrap: break-word;">
        
        
        <!-- Styles pour les rectangles colorés et le texte -->
        <style>
            .legend-item {{
                display: flex;
                align-items: center;
                margin-bottom: 5px;
            }}
            .legend-color {{
                width: 30px;
                height: 15px;
                margin-right: 10px;
                border: 1px solid #ccc;
            }}
            .legend-text {{
                font-size: 10px;
                color: #333;
            }}
        </style>
    
    
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin-bottom: 2px">{apl_txt}</li>
            <li style="margin-bottom: 2px">{zonage_txt}</li>
        </ul>
        
        <!-- Insérer la légende de rectangles colorés ici -->
        {legend_html}
        
        <div id="legend_content" style="display: none; position: relative; bottom: 10px;">
            <p style="margin-top: 20px; "><b>Sources:</b></p>
            <ul>
                <li>Vulnérabilité: <i>Insee RP 2019 calculs LARIIS</i></li>
                <li>Points: <i>Banque du Numérique</i></li>
            </ul>
        </div>
        
        <button onclick="toggleLegend()" style="position: absolute; bottom: 2px; right: 10px">Sources</button>
        
    </div>
    
    
    <script>
    var isSourceVisible = false;
        function toggleLegend() {{
            var legendContent = document.getElementById("legend_content");
            var button = document.querySelector("button");
            
            if (!isSourceVisible) {{
                legendContent.style.display = "block";
                button.textContent = "Masquer les sources";
            }} else {{
                legendContent.style.display = "none";
                button.textContent = "Sources"
            }}
            
            isSourceVisible = !isSourceVisible;
        }}
                      
    </script>
    """

    return(legende)

