
def searchwine(tag):
    redwine = ['Red', 'Früburgunder', 'Shiraz', 'Zinfandel', 'Tinta', 'Cabernet', 'Syrah-Grenache', 'Roditis', 'Merlot', 'Traminer', 'Nero', 'Shiraz-Viognier', 'Syrah', 'Frappato', 'Nebbiolo', 'Petite', 'Duras', 'Cinsault', 'Zweigelt', 'Bordeaux-style', 'Barbera', 'Sagrantino', 'Malbec', 'Garnacha', 'Tannat-Cabernet', 'Nerello', 'Meritage', 'Primitivo', 'Mencía', 'Blaufränkisch', 'G-S-M', 'Pinot', 'Cannonau', 'Tempranillo', 'Graciano', 'Monica' , 'Merlot-Malbec', 'Bonarda', 'Carmenère', 'Monastrell', 'Gamay', 'Sangiovese', 'Montepulciano', 'Tempranillo-Merlot', 'Carignan-Grenache', 'Prugnolo', 'Port', 'Rhône-style', 'Pinotage', 'Touriga', 'Aglianico', 'Dolcetto' ,'Petite', 'Grenache', 'Shiraz-Cabernet', 'Syrah-Viognier', 'Portuguese', 'Corvina', 'Sousão']

    whitewine = ["Riesling",'Verdelho', 'Zierfandler', 'Grillo', 'Chenin', 'Ugni', 'Cortese', 'White', 'Sémillon', 'Furmint', 'Melon', 'Ribolla', 'Vignoles', 'Verdicchio', 'Inzolia', 'Garganega', 'Vilana', 'Antão', 'Viura', 'Friulano', 'Greco', 'Torrontés', 'Vidal', 'Alsace', 'Marsanne', 'Moscato', 'Vernaccia', 'Glera', 'Muscat', 'Silvaner', 'Savagnin', 'Fiano', 'Vermentino', 'Insolia', 'Catarratto', 'Grüner', 'Viognier-Chardonnay', 'Muscadelle', 'Albariño', 'Kerner', 'Carricante', 'Trebbiano', 'Scheurebe', 'Verdejo', 'Colombard', 'Assyrtico', 'Chinuri', 'Sylvaner', 'Fumé', 'Viognier', 'Verdejo-Viura' ,'Weissburgunder', 'Avesso', 'Gewürztraminer', 'Verduzzo', 'Roussanne', 'Xarel-lo', 'Sauvignon', 'Chardonnay']

    rosewine = ['Rosé', 'Roter', 'Rosato']

    spacling = ['Champagne', 'Prosecco', 'Sparkling']

    if tag in redwine:
        return '레드와인'
    elif tag in whitewine:
        return '화이트와인'
    elif tag in rosewine:
        return '로제와인'
    elif tag in spacling:
        return '스파클링와인'
    else :
        return f'미분류{tag}'