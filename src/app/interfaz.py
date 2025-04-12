from termcolor import colored
from wcwidth import wcswidth

def print_fancy_box(titles, align='center', border_style='simple', colors=None):
    if isinstance(titles, str):
        titles = [titles]

    # Usamos el ancho visual real
    visual_widths = [wcswidth(title) for title in titles]
    max_len = max(visual_widths)
    padding = 4
    content_width = max_len + padding

    # Bordes
    if border_style == 'double':
        tl, tr, bl, br, hor, ver = '╔', '╗', '╚', '╝', '═', '║'
    else:
        raise ValueError("Estilo de borde inválido. Usa 'simple' o 'double'.")

    print(f"{tl}{hor * content_width}{tr}")

    for i, title in enumerate(titles):
        visual_len = wcswidth(title)
        total_space = content_width - visual_len

        if align == 'center':
            left = total_space // 2
            right = total_space - left
        else:
            left = 2
            right = total_space - left

        line = f"{ver}{' ' * left}{title}{' ' * right}{ver}"

        if colors and i < len(colors):
            print(colored(line, colors[i]))
        else:
            print(line)

    print(f"{bl}{hor * content_width}{br}")

def interfaz_principal(): 
    print_fancy_box([
        "▁ ▂ ▃ ▄ ▅ ▆ ▇ ▉ ▊ ▋ █ ▌ Bienvenidos ▌ █ ▋ ▊ ▉ ▇ ▆ ▅ ▄ ▃ ▂ ▁",
        "➥ En el siguiente programa podrá guardar información educativa para brindar una mejor organización al usuario",
        "1. Opciones",
        "2. Salir"
    ], align='center', border_style='double')

     