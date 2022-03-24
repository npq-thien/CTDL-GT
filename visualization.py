from tkinter import *
import redblacktree as rbt
from tkinter import *
from tkinter import Canvas
import time
import redblacktree as rbt

window_width = 1680
window_height = 1050

canvas_width = 1600
canvas_height = 970

mid_canvas_width = canvas_width // 2
mid_canvas_height = canvas_height // 2

f = ('Roboto', 16, 'bold')

colors = ['black', 'red']
radius = 20

day = "day"
nodes = []







def insert_tree():
    c.delete(day)
    ar_split = box.get().split(',')
    box.delete(0, END)
    for i in ar_split:
        rbt.insert(int(i))
        # rbt.print_tree()

        visualize()


def delete_tree():
    c.delete(day)
    ar_split = box.get().split(',')
    box.delete(0, END)
    for i in ar_split:
        nodes.remove([f'o{i}', f'l{i}'])
        rbt.delete_node(int(i))
        c.delete(ALL)
        visualize()

    print(ar_split)

def find_tree():
    c.delete(day)
    ar_split = box.get().split(',')
    box.delete(0, END)


def emtpy_canvas():
    c.delete(ALL)
    circles.clear()


def list_node():
    s = ''.join(str(i) + ' ' for i in rbt.get_list_node())
    return s


def print_tree():
    s = list_node()
    # c.delete(tags[0])
    node = c.create_text(mid_canvas_width, canvas_height - 50,
                         text=s, font=f, fill='black', tag=day, justify='center')


def visualize():
    tree = rbt.root  # start with root of the tree
    # Place root node at position tree.pos
    if tree.item != 0:
        tree.pos = [mid_canvas_width, 100]
        create_node(tree.pos, tree.color, f"{tree.item}")

        # Recursively place the other nodes and edges
        level = 0

        def add_nodes(tree, level):
            if tree.left.item != 0:  # if left subtree: position node to left of parent
                tree.left.pos[0] = tree.pos[0] - 12 * radius // level  # x
                tree.left.pos[1] = tree.pos[1] + 2 * radius  # y
                create_node(tree.left.pos, tree.left.color, f"{tree.left.item}")
                add_nodes(tree.left, level + 1)
            if tree.right.item != 0:  # if right subtree: position node to right of parent
                tree.right.pos[0] = tree.pos[0] + 12 * radius // level  # x
                tree.right.pos[1] = tree.pos[1] + 2 * radius  # y
                create_node(tree.right.pos, tree.right.color, f"{tree.right.item}")
                add_nodes(tree.right, level + 1)

        if tree.left or tree.right:
            add_nodes(tree, level + 1)


# def create_node(x,y, r = radius, color='black', text='null'):
#     new_circle = c.create_oval(x-r, y-r, x+r, y+r, fill=color, outline='black', width=2)
#     new_txt = c.create_text(x, y, text=text, font= f, fill='white', justify='center')
#     circles.append([new_circle, new_txt])

def create_node(pos, color=0, text='null'):
    x = pos[0]
    y = pos[1]
    r = radius
    cor = x - r, y - r, x + r, y + r
    o_tag = 'o'+text
    l_tag = 'l'+text
    c.create_oval(cor, fill=colors[color], outline='black', width=2, tag=o_tag)
    c.create_text(pos, text=text, font=f, fill='white',justify='center', tag=l_tag)
    nodes.append([o_tag, l_tag])


def create_edge(x0, y0, x, y, color='black'):
    c.create_line(x0, y0, x, y, fill=color, width=3)


rbt = rbt.RedBlackTree()

root = Tk()
root.title("Red Black Tree Visualization")

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# create canvas

c = Canvas(root, width=canvas_width, height=canvas_height, bg='white')


c.pack(padx=40, pady=40, fill=BOTH, expand=True)


# add insertion textbox
box = Entry(root, width=20, font=('Roboto', 16))
box.place(x=40, y=10)

# add insertion button
insert_button = Button(root, text="Insert", command=insert_tree)
insert_button.place(x=260, y=8)

# add find button
search_button = Button(root, text="Search", command=find_tree)
search_button.place(x=335, y=8)

# add deletion button
deletion_button = Button(root, text="Delete", command=delete_tree)
deletion_button.place(x=420, y=8)

# add  empty button
empty_button = Button(root, text="Empty", command=emtpy_canvas)
empty_button.place(x=500, y=8)

# add print button
print_button = Button(root, text="Print", command=print_tree)
print_button.place(x=580, y=8)

# # add exit button
# quit_button = Button(
#     root, text="Quit", command=root.destroy).place(y=860, x=10)
print(list_node())

root.mainloop()
