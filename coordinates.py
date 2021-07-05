import random, webbrowser

def main():
    coordinates = get_coordinates()
    new_coordinates = shorten_coordinates(coordinates)
    url = create_link(new_coordinates)
    open_in_browser(url)

def get_coordinates():
    lon_x = float(random.uniform(-180,180))
    lat_y = float(random.uniform(-90,90))
    coordinates = [lat_y, lon_x]
    return coordinates

def shorten_coordinates(coord):
    new_coord = []
    for value in coord:
        value = round(value, 4)
        new_coord.append(value)
    return new_coord

def open_in_browser(url):
    webbrowser.open_new_tab(url)

def create_link(coord):
    url_string = f'https://www.openstreetmap.org/#map=10/{coord[0]}/{coord[1]}'
    return url_string

if __name__ == '__main__':
    main()