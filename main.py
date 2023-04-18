import extcolors
import matplotlib.pyplot as plt
import os


def extract_colors(path):
    """Extracts the colors and the percentages that they occupy in the image."""
    colors, nb_pixels = extcolors.extract_from_path(path)
    return colors, nb_pixels


def create_lists(colors, nb_pixels):
    """Creates two lists: one with the colors and one with the percentages."""
    colors_rgb = []
    sizes = []

    for element in colors:
        if element[1] / nb_pixels > 0.015:
            colors_rgb.append(element[0])
            sizes.append(element[1] / nb_pixels)

    colors_hex = []

    for element in colors_rgb:
        element = convert_rgb_to_hex(element)
        colors_hex.append(element)

    return colors_hex, sizes


def convert_rgb_to_hex(color):
    """Converts any RGB color to the corresponding HEX color."""
    return '#%02x%02x%02x' % (color[0], color[1], color[2])


def draw_graph_and_image(colors_hex, sizes, path):
    """Builds the graph with the HEX colors and the corresponding percentages"""
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=colors_hex, autopct='%1.1f%%',
            pctdistance=0.6, shadow=False, startangle=0)
    ax1.axis('equal')
    plt.pie(sizes, colors=colors_hex)

    # Transforms the graph into a circle
    centre_circle = plt.Circle((0, 0), 0.75, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Displays the image on top of the graph
    img = plt.imread(path)
    plt.imshow(img, zorder=0, extent=[-1.5, 1.5, 1.25, 3])

    # Displays a message to make sure that the output is verified by the user
    txt = "To make sure that the colors are correct, \nyou can check the image above the graph."
    plt.text(0, -1.45, txt, horizontalalignment='center', fontsize=14, color='green', style='italic')

    # Displays the graph
    plt.show()


def main():
    # Colors
    red = '\x1b[91m'
    reset_color = '\x1b[0m'

    # Welcome message
    print("════════════════════════════════════════════╣ Welcome ╠════════════════════════════════════════════\n")
    print("""                        This program will extract the colors of your image.\n""")

    # List of the images in the project folder
    images = os.listdir('./images')

    print(
        f'Choose your image {red}(image must be in the \'images\' folder){reset_color}: ')
    for img in images:
        if img.endswith('.png') or img.endswith('.jpg') or img.endswith('.jpeg'):
            print(f'{images.index(img) + 1}. {img}')

    # Gets the path of the image to extract the colors from
    path = input(f'\nEnter the number of your image: ')
    path = './images/' + images[int(path) - 1]

    pwd = os.path.dirname(__file__)
    path = os.path.join(pwd, path)

    # Extracts the colors from the image
    colors, nb_pixels = extract_colors(path)

    # Creates of the colors and of the percentage that they occupy in the image
    colors_hex, sizes = create_lists(colors, nb_pixels)

    # Draws the graph + the image
    draw_graph_and_image(colors_hex, sizes, path)


if __name__ == '__main__':
    main()
