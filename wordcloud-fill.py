from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_wordcloud(word_list):
    # Convert the list of words into a single string
    text = ' '.join(word_list)
    
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400).generate(text)
    
    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

words= [
    'Rose', 'Tulip', 'Daisy', 'Sunflower', 'Lily', 'Orchid', 'Carnation', 'Daffodil', 'Iris', 'Marigold', 
    'Hyacinth', 'Lilac', 'Jasmine', 'Chrysanthemum', 'Poppy', 'Pansy', 'Peony', 'Violet', 'Magnolia', 'Hibiscus', 
    'Azalea', 'Camellia', 'Freesia', 'Geranium', 'Lavender', 'Begonia', 'Amaryllis', 'Dahlia', 'Zinnia', 'Gardenia', 
    'Hydrangea', 'Anemone', 'Aster', 'Bellflower', 'Bleeding Heart', 'Buttercup', 'Crocus', 'Dandelion', 'Foxglove', 'Hollyhock', 
    'Impatiens', 'Lupine', 'Morning Glory', 'Narcissus', 'Petunia', 'Primrose', 'Snapdragon', 'Snowdrop', 'Sweet Pea', 'Verbena', 
    'Wisteria', 'Yarrow', 'Clematis', 'Coneflower', 'Cosmos', 'Fuchsia', 'Gladiolus', 'Heather', 'Honeysuckle', 'Ivy', 
    'Larkspur', 'Lotus', 'Mimosa', 'Oleander', 'Poinsettia', 'Rhododendron', 'Sage', 'Thistle', 'Tiger Lily', 'Water Lily', 
    'Ageratum', 'Allium', 'Alyssum', 'Amaranth', 'Anthurium', 'Artemisia', 'Baby’s Breath', 'Balsam', 'Bee Balm', 'Bird of Paradise', 
    'Black Eyed Susan', 'Bluebell', 'Bougainvillea', 'Butterfly Bush', 'Calendula', 'Candytuft', 'Canna', 'Celosia', 'Cherry Blossom', 'Chicory', 
    'Chinchilla', 'Chrysanthemum', 'Cineraria', 'Cockscomb', 'Columbine', 'Cornflower', 'Cyclamen', 'Daffodil', 'Dahlia', 'Daisy', 
    'Dame’s Rocket', 'Delphinium', 'Dianthus', 'Dogwood', 'Dusty Miller', 'Echinacea', 'Edelweiss', 'Elderflower', 'Elephant Ear', 'Evening Primrose'
]


create_wordcloud(words)
