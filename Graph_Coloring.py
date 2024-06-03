import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

class GraphColoringApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kolorowanie Grafów")
        self.root.geometry("1240x720")
        self.root.config(bg = "#CBCBCB")

        self.root.iconbitmap("icon.png")

        bckFile = "background.jpg"
        img = Image.open(bckFile)
        img = img.resize((1240, 720), resample = 3)

        bck = ImageTk.PhotoImage(img)

        bckPanel = tk.Label(self.root, image = bck)
        bckPanel.pack(side = "top", fill = "both", expand = True)
        bckPanel.image = bck
        
        self.title_label = tk.Label(self.root, text="Kolorowanie Grafów", font =("Aller", 30), bg = "black", foreground="white")
        self.title_label.place(relx=0.18, rely = 0.25, anchor = "center")
        
        self.subtitle_label = tk.Label(self.root, text = "by Greń Piotr, Kiwacka Gabriela", font = ("Aller", 10), bg = "black", foreground="white")
        self.subtitle_label.place(relx=0.1065, rely = 0.30, anchor = "n")
        
        self.start_button = tk.Button(self.root, text="ROZPOCZNIJ", font =("Aller", 20), bg = "#1f1f1f", fg = "white", padx = 10, command=self.go_to_menu)
        self.start_button.place(relx=0.1065, rely = 0.40, anchor = "n")
        self.start_button.bind("<Enter>", lambda event, button = self.start_button: self.start_button.config(bg = "#2f2f2f", fg = "white"))
        self.start_button.bind("<Leave>", lambda event, button = self.start_button: self.start_button.config(bg = "#1f1f1f", fg = "white"))
        
        #self.root.wm_attributes("-transparentcolor", "#acbc13")
        self.vertices = None
        self.matrix = None

    def go_to_menu(self):
        self.start_button.destroy()
        self.title_label.destroy()
        self.subtitle_label.destroy()
        self.menu()
        
    def menu(self):
        self.own_butt = tk.Button(self.root, text="Stwórz Graf", font =("Aller", 20), width = 30, height = 2, bg = "#1f1f1f", fg = "white", padx = 10, command=self.leave_menu0)
        self.own_butt.place(relx=0.5, rely = 0.10, anchor = "center")
        self.own_butt.bind("<Enter>", lambda event, button = self.own_butt: self.own_butt.config(bg = "#2f2f2f", fg = "white"))
        self.own_butt.bind("<Leave>", lambda event, button = self.own_butt: self.own_butt.config(bg = "#1f1f1f", fg = "white"))

        self.c5_butt = tk.Button(self.root, text="Graf C5", font =("Aller", 20), width = 30, height = 2, bg = "#1f1f1f", fg = "white", padx = 10, command=self.leave_menu1)
        self.c5_butt.place(relx=0.5, rely = 0.30, anchor = "center")
        self.c5_butt.bind("<Enter>", lambda event, button = self.c5_butt: self.c5_butt.config(bg ="#2f2f2f", fg = "white"))
        self.c5_butt.bind("<Leave>", lambda event, button = self.c5_butt: self.c5_butt.config(bg ="#1f1f1f", fg = "white"))

        self.tree_butt = tk.Button(self.root, text="Drzewo", font =("Aller", 20), width = 30, height = 2, bg = "#1f1f1f", fg = "white", padx = 10, command=self.leave_menu2)
        self.tree_butt.place(relx=0.5, rely = 0.50, anchor = "center")
        self.tree_butt.bind("<Enter>", lambda event, button = self.tree_butt: self.tree_butt.config(bg="#2f2f2f", fg = 'white'))
        self.tree_butt.bind("<Leave>", lambda event, button = self.tree_butt: self.tree_butt.config(bg="#1f1f1f", fg = 'white'))

        self.m4_butt = tk.Button(self.root, text="Graf Grotzsch'a", font =("Aller", 20), width = 30, height = 2, bg = "#1f1f1f", fg = "white", padx = 10, command=self.leave_menu3)
        self.m4_butt.place(relx=0.5, rely = 0.70, anchor = "center")
        self.m4_butt.bind("<Enter>", lambda event, button = self.m4_butt: self.m4_butt.config(bg = "#2f2f2f", fg = "white"))
        self.m4_butt.bind("<Leave>", lambda event, button = self.m4_butt: self.m4_butt.config(bg = "#1f1f1f", fg = "white"))

        self.random_butt = tk.Button(self.root, text="Losowy Graf", font =("Aller", 20), width = 30, height = 2, bg = "#1f1f1f", fg = "white", padx = 10, command=self.leave_menu4)
        self.random_butt.place(relx=0.5, rely = 0.90, anchor = "center")
        self.random_butt.bind("<Enter>", lambda event, button = self.random_butt: self.random_butt.config(bg = "#2f2f2f", fg = "white"))
        self.random_butt.bind("<Leave>", lambda event, button = self.random_butt: self.random_butt.config(bg = "#1f1f1f", fg = "white"))

        self.end_button = tk.Button(self.root, text = "Zamknij", font = ("Aller", 15), bg = "#1f1f1f", fg = "white", width = 10, height = 1, command = self.end_app)
        self.end_button.place(relx = 0.94, rely = 0.96, anchor = "center")
        self.end_button.bind("<Enter>", lambda event, button = self.end_button: self.end_button.config(bg = "#2f2f2f", fg = "white"))
        self.end_button.bind("<Leave>", lambda event, button = self.end_button: self.end_button.config(bg = "#1f1f1f", fg = "white"))


    def leave_menu0(self):
        self.own_butt.destroy()
        self.c5_butt.destroy()
        self.tree_butt.destroy()
        self.m4_butt.destroy()
        self.random_butt.destroy()
        self.end_button.destroy()
        self.show_form()

    def leave_menu1(self):
        self.own_butt.destroy()
        self.c5_butt.destroy()
        self.tree_butt.destroy()
        self.m4_butt.destroy()
        self.random_butt.destroy()
        self.end_button.destroy()

        import networkx as nx
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        # Tworzenie pustego grafu
        self.G = nx.Graph()
        self.G.add_nodes_from([1, 2, 3, 4, 5])
        self.G.add_edge(1, 5)
        self.G.add_edge(1, 2)
        self.G.add_edge(2, 3)
        self.G.add_edge(3, 4)
        self.G.add_edge(4, 5)

        self.chroma()
        
    def leave_menu2(self):
        import networkx as nx
        import random

        self.own_butt.destroy()
        self.c5_butt.destroy()
        self.tree_butt.destroy()
        self.m4_butt.destroy()
        self.random_butt.destroy()
        self.end_button.destroy()

        self.G = nx.Graph()
        self.G.add_node(1)

        num_nodes = random.randrange(2, 26)

        for i in range(2, num_nodes + 1):
            parent = random.choice(list(self.G.nodes()))
            self.G.add_node(i)
            self.G.add_edge(i, parent)

        self.chroma()
        
    def leave_menu3(self):
        import networkx as nx

        self.own_butt.destroy()
        self.c5_butt.destroy()
        self.tree_butt.destroy()
        self.m4_butt.destroy()
        self.random_butt.destroy()
        self.end_button.destroy()

        self.G = nx.Graph()
        self.G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.G.add_edges_from([(1,2), (1,3), (1,4), (1,6), (1,9), 
                               (2,3), (2,5), (2,7), (2,8), 
                               (3,4), (3,5), (3,7), (3,9), 
                               (4,6), (4,8), (4,9), 
                               (5,6), (5,8), (5,9), 
                               (6,7), (6,8), (6,9), 
                               (7,8), (7,9), 
                               (8,9)])
        
        self.chroma()
        
    def leave_menu4(self):
        import random
        import networkx as nx

        self.own_butt.destroy()
        self.c5_butt.destroy()
        self.tree_butt.destroy()
        self.m4_butt.destroy()
        self.random_butt.destroy()
        self.end_button.destroy()

        vertices = random.randrange(2, 26)
        matrix = []
        for i in range(vertices):
            row = [0] * vertices
            matrix.append(row)

        for i in range(vertices):
            for j in range(i+1, vertices):
                if i == j:
                    return
                else:
                    value = random.randint(0, 1)
                    matrix[i][j] = value
                    matrix[j][i] = value

        self.G = nx.Graph()

        for i in range(vertices):
            self.G.add_node(i + 1)
        # Przejście przez macierz sąsiedztwa i dodawanie krawędzi do grafu
        for i in range(vertices):
            for j in range(i+1, vertices):
                if matrix[i][j] == 1:
                    self.G.add_edge(i+1, j+1)

        self.chroma()



    def show_form(self):
        self.form_label = tk.Label(self.root, text="Podaj liczbę wierzchołków:", font = ("Aller", 25), bg='black', fg="white")
        self.form_label.place(relx=0.18, rely = 0.25, anchor = "center")
        
        self.vertices_entry = tk.Entry(self.root, font = ("Aller", 20), justify = "center")
        self.vertices_entry.place(relx=0.145, rely = 0.35, anchor = "center")

        def validate_value():
            value = int(self.vertices_entry.get())
            if value < 2:
                self.status_label.config(text="Wartość za mała", fg="red")
            elif value > 25:
                self.status_label.config(text="Wartość za duża", fg="red")
            else:
                self.create_matrix()
        
        self.submit_button = tk.Button(self.root, text="Zatwierdź", font = ("Aller", 14), bg = "#1f1f1f", fg = "white", command=validate_value)
        self.submit_button.place(relx=0.32, rely = 0.352, anchor = "center")
        self.submit_button.bind("<Enter>", lambda event, button = self.submit_button: self.submit_button.config(bg = "#2f2f2f", fg = 'white'))
        self.submit_button.bind("<Leave>", lambda event, button = self.submit_button: self.submit_button.config(bg = "#1f1f1f", fg = 'white'))

        self.backm_butt = tk.Button(self.root, text = "Wstecz", font = ("Aller", 15), bg = "#1f1f1f", fg="white", width = 39, height = 1, command = self.go_back_menu)
        self.backm_butt.place(relx = 0.19, rely = 0.5, anchor = "center")
        self.backm_butt.bind("<Enter>", lambda event, button = self.backm_butt: self.backm_butt.config(bg = "#2f2f2f", fg = "white"))
        self.backm_butt.bind("<Leave>", lambda event, button = self.backm_butt: self.backm_butt.config(bg = "#1f1f1f", fg = "white"))

        self.status_label = tk.Label(self.root, text="", font=("Aller", 15), bg = "black")
        self.status_label.place(relx=0.5, rely=0.75, anchor="center")

        self.matrix_frame = tk.Frame(self.root, bg="black")
        self.matrix_frame.place(relx = 0.033, rely = 0.05)

        self.create_matrix()
    
    def go_back_menu(self):
        self.vertices_entry.destroy()
        self.form_label.destroy()
        self.status_label.destroy()
        self.submit_button.destroy()
        self.backm_butt.destroy()
        self.matrix_frame.destroy()
        self.menu()

    def create_matrix(self):
        import random
        self.vertices = int(self.vertices_entry.get())
        
        self.form_label.destroy()
        self.vertices_entry.destroy()
        self.submit_button.destroy()
        self.status_label.destroy()
        self.backm_butt.destroy()
        
        self.matrix_frame.config(width = 650, height=650)
        
        if self.vertices in(21, 22, 23, 24):
            cell_width = 2
            cell_height = 1
        else:
            a = int((25 - self.vertices))
            if a%2 != 0:
                cell_width = (a - 1)//2
            else:
                cell_width = a//2
            cell_height = cell_width//2
        #cell_size = 650//(self.vertices)
        
        self.matrix = []
        for i in range(self.vertices):
            row = [0] * self.vertices
            self.matrix.append(row)
        
        for i in range(self.vertices):
            for j in range(self.vertices):
                button = tk.Button(self.matrix_frame, text="0", bd=1, bg="#1f1f1f", fg="white", command=lambda i=i, j=j: self.toggle_edge(i, j))
                button.config(width=cell_width, height=cell_height)
                button.grid(row=i+1, column=j+1, sticky="nsew")
                color = ["red", "green","#f3ba02", "blue", "purple", "#ff6912", "brown", "pink", "#666912", "#1fb3ea", "#c9b3ea", "#474482"]
                button.bind("<Enter>", lambda event, button=button: button.config(bg=random.choice(color), fg="black"))
                button.bind("<Leave>", lambda event, button=button: button.config(bg="#1f1f1f", fg="white"))
                

        for i in range(self.vertices):
            row_label = tk.Label(self.matrix_frame, text=str(i+1), width=1, height=1, bg="black", fg="white")
            row_label.grid(row=i+1, column=0, sticky="nsew")
            col_label = tk.Label(self.matrix_frame, text=str(i+1), width=1, height=1, bg="black", fg="white")
            col_label.grid(row=0, column=i+1, sticky="nsew")

        self.matrix_frame.grid_rowconfigure(0, weight=1)
        self.matrix_frame.grid_columnconfigure(0, weight=1)
        for i in range(self.vertices):
            self.matrix_frame.grid_rowconfigure(i+1, weight=1)
            self.matrix_frame.grid_columnconfigure(i+1, weight=1)
        

        self.random_butt = tk.Button(self.root, text = "Generuj losowo", font = ("Aller", 15), bg = "#1f1f1f", fg="white", width = 30, height = 3, command = self.generate_random_matrix)
        self.random_butt.place(relx=0.80, rely = 0.15, anchor = "center")
        self.random_butt.bind("<Enter>", lambda event, button=self.random_butt: self.random_butt.config(bg="#2f2f2f", fg="white"))
        self.random_butt.bind("<Leave>", lambda event, button=self.random_butt: self.random_butt.config(bg="#1f1f1f", fg="white"))


        self.submit_butt = tk.Button(self.root, text = "Zatwierdź", font = ("Aller", 15), bg = "#1f1f1f", fg="white", width = 30, height = 3, command = self.graph_create)
        self.submit_butt.place(relx=0.80, rely = 0.35, anchor = "center")
        self.submit_butt.bind("<Enter>", lambda event, button=self.submit_butt: self.submit_butt.config(bg="#2f2f2f", fg="white"))
        self.submit_butt.bind("<Leave>", lambda event, button=self.submit_butt: self.submit_butt.config(bg="#1f1f1f", fg="white"))

        self.back_butt = tk.Button(self.root, text = "Wstecz", font = ("Aller", 15), bg = "#1f1f1f", fg="white", width = 30, height = 3, command = self.go_back)
        self.back_butt.place(relx=0.80, rely = 0.55, anchor = "center")
        self.back_butt.bind("<Enter>", lambda event, button=self.back_butt: self.back_butt.config(bg="#2f2f2f", fg="white"))
        self.back_butt.bind("<Leave>", lambda event, button=self.back_butt: self.back_butt.config(bg="#1f1f1f", fg="white"))

    def go_back(self):
        self.submit_butt.destroy()
        self.random_butt.destroy()
        self.back_butt.destroy()
        self.matrix_frame.destroy()
        self.show_form()

    def generate_random_matrix(self):
        import random
    
        for i in range(self.vertices):
            for j in range(i+1, self.vertices):
                if i == j:
                    return
                else:
                    value = random.randint(0, 1)
                    self.matrix[i][j] = value
                    self.matrix[j][i] = value
        
                    button_text = str(self.matrix[i][j])
                    self.matrix_frame.grid_slaves(row=i+1, column=j+1)[0].configure(text=button_text)
                    self.matrix_frame.grid_slaves(row=j+1, column=i+1)[0].configure(text=button_text)

    def toggle_edge(self, i, j):
        if i == j:
            return
        if self.matrix[i][j] == 0:
            self.matrix[i][j] = 1
        else:
            self.matrix[i][j] = 0
        
        button_text = str(self.matrix[i][j])
        self.matrix_frame.grid_slaves(row=i+1, column=j+1)[0].configure(text=button_text)
        self.matrix_frame.grid_slaves(row=j+1, column=i+1)[0].configure(text=button_text)

    def graph_create(self):

        import networkx as nx
        import networkx as nx
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        # Tworzenie pustego grafu
        self.G = nx.Graph()

        for i in range(self.vertices):
            self.G.add_node(i + 1)

        # Przejście przez macierz sąsiedztwa i dodawanie krawędzi do grafu
        for i in range(self.vertices):
            for j in range(i+1, self.vertices):
                if self.matrix[i][j] == 1:
                    self.G.add_edge(i+1, j+1)


        self.matrix_frame.destroy()
        self.submit_butt.destroy()
        self.random_butt.destroy()
        self.back_butt.destroy()
        self.chroma()
        
    def chroma(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        #coloring = nx.coloring.greedy_color(self.G, strategy = "smallest_last")

        def smallest_last(G):
            G_copy = G.copy()
            removed_nodes = []
            degrees = list(G_copy.degree())
            degrees.sort(key = lambda x: x[1])
            colors = [None] * len(G.nodes)

            while degrees:
                node, degree = degrees.pop(0)
                removed_nodes.append(node)
                G_copy.remove_node(node)
                neighbour_colors = set(colors[i - 1] for i in G.neighbors(node) if colors[i - 1] is not None)
                for color in range(len(colors)):
                    if color not in neighbour_colors:
                        colors[node - 1] = color
                        break
                degrees = list(G_copy.degree())
                degrees.sort(key = lambda x: x[1])

            
            for node in reversed(removed_nodes):
                neighbours = set(G[node])
                neighbour_colors = set(colors[i] for i in range(len(G.nodes)) if G.has_edge(node, i) and colors[i] is not None)
                for color in range(len(G.nodes)):
                    if color not in neighbour_colors:
                        colors[node - 1] = color
                        break

            return max(colors) + 1


        #chromatic_number = max(coloring.values()) + 1
        self.chromatic_number_sl = smallest_last(self.G)

        self.Chroma_Label = tk.Label(self.root, text = (f"Liczba chromatyczna grafu: {self.chromatic_number_sl}"), font =("Aller", 30), bg = "black", foreground="white")
        self.Chroma_Label.place(relx=0.22, rely = 0.05, anchor = "center")

        pos = nx.spring_layout(self.G)  # określenie pozycji wierzchołków
        fig, ax = plt.subplots(figsize = (6, 6))

        nx.draw(self.G, pos, with_labels=True, node_color = "gray", edge_color = "white", font_color = "white", ax = ax)  # rysowanie grafu z etykietami wierzchołków
        fig.set_facecolor("black")
        ax.set_facecolor("black")

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()

        self.canvas.get_tk_widget().place(relx=0.25, rely=0.55, anchor="center")

        self.optimalize_butt = tk.Button(self.root, text = "Optymalizuj i koloruj", font = ("Aller", 15), fg = "white", bg = "#1f1f1f", width = 30, height = 3, command = self.go_to_optimalize)
        self.optimalize_butt.place(relx = 0.80, rely = 0.15, anchor = "center")
        self.optimalize_butt.bind("<Enter>", lambda event, button = self.optimalize_butt: self.optimalize_butt.config(bg = "#2f2f2f", fg = "white"))
        self.optimalize_butt.bind("<Leave>", lambda event, button = self.optimalize_butt: self.optimalize_butt.config(bg = "#1f1f1f", fg = 'white'))

        self.back_button = tk.Button(self.root, text = "Powrót do menu", font = ("Aller", 15), bg = "#1f1f1f", fg = 'white', width = 30, height = 3, command = self.back_to_menu)
        self.back_button.place(relx=0.80, rely = 0.35, anchor = "center")
        self.back_button.bind("<Enter>", lambda event, button=self.back_button: self.back_button.config(bg = "#2f2f2f", fg = "white"))
        self.back_button.bind("<Leave>", lambda event, button=self.back_button: self.back_button.config(bg = "#1f1f1f", fg = 'white'))

    def back_to_menu(self):
        self.Chroma_Label.destroy()
        self.back_button.destroy()
        self.canvas.get_tk_widget().place_forget()
        self.optimalize_butt.destroy()
        self.menu()
    
    def go_to_optimalize(self):
        self.Chroma_Label.destroy()
        self.back_button.destroy()
        self.canvas.get_tk_widget().place_forget()
        self.optimalize_butt.destroy()
        self.optimalize()

    
    def optimalize(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        self.colors = ["red", "green", "#f3ba02", "blue", "purple", "#ff6912", "brown", "pink", "#666912", "#1fb3ea", "#c9b3ea", "#474482"]
        #self.colors = ['#F2A20C', '#E66F01', '#D94E67', '#C91F37', '#B20D57', '#A21864', '#8D3F3F', '#7E3E50', '#6B2C5F', '#5E4B5C', '#4D5360', '#374785', '#175E8A', '#008C8D', '#00A885']

        def is_coloring_valid(G, v, color, c):
            """Sprawdza, czy przypisanie koloru c do wierzchołka v jest poprawne."""
            for u in G.neighbors(v):
                if color[u-1] == c:
                    return False
            return True

        def color_graph(G, colors, color, v):
            """Rekurencyjnie koloruje wierzchołki grafu."""
            if v == len(G.nodes()) + 1:
                return True
            for c in colors:
                if is_coloring_valid(G, v, color, c):
                    color[v - 1] = c
                    if color_graph(G, colors, color, v+1):
                        return True
                    color[v - 1] = None
            return False

        def graph_coloring(G, colors):
            """Koloruje graf G za pomocą dostępnych kolorów."""
            color = [None] * len(G.nodes())
            if color_graph(G, colors, color, 1):
                return color
            else:
                return None
    
        self.colored = graph_coloring(self.G, self.colors)
        

        if self.colored is None:
            self.text_ao = "Nie udało się pokolorować grafu!"
            self.colored = "grey"
            x = 0.22
        elif len(list(set(self.colored))) > self.chromatic_number_sl:
            unique_values = list(set(self.colored))
            self.text_ao = f"Liczba chromatyczna oszacowana przez algorytm zachłanny: {self.chromatic_number_sl}\n Liczba oszacowana przez backtracking: {len(unique_values)}\n Nie udało się pokolorować grafu oszacowaną liczbą kolorów [{self.chromatic_number_sl}]!"
            self.colored = 'grey'
            x = 0.25
        else:
            unique_values = list(set(self.colored))
            self.text_ao = f"Liczba chromatyczna oszacowana przez algorytm zachłanny: {self.chromatic_number_sl}\n Liczba chromatyczna oszacowana przez backtracking: {len(unique_values)}\n Udało się pokolorować graf! Liczba chromatyczna grafu to: {len(unique_values)}!"
            x = 0.25

        self.opti_label = tk.Label(self.root, text=self.text_ao, font=("Aller", 15), bg = "black", fg = "white")
        self.opti_label.place(relx=x, rely = 0.06, anchor = "center")
        
        pos = nx.spring_layout(self.G)  # określenie pozycji wierzchołków
        fig, ax = plt.subplots(figsize = (6, 6))

        nx.draw(self.G, pos, with_labels=True, node_color = self.colored, edge_color = "white", font_color = "white", ax = ax)  # rysowanie grafu z etykietami wierzchołków
        fig.set_facecolor("black")
        ax.set_facecolor("black")

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()

        self.canvas.get_tk_widget().place(relx=0.25, rely=0.55, anchor="center")

        self.end_butt = tk.Button(self.root, text = "Zakończ i zamknij", font = ("Aller", 15), bg = "#1f1f1f", fg = 'white', width = 30, height = 3, command = self.end_app)
        self.end_butt.place(relx = 0.8, rely = 0.2, anchor = "center")
        self.end_butt.bind("<Enter>", lambda event, button = self.end_butt: self.end_butt.config(bg = "#2f2f2f", fg = "white"))
        self.end_butt.bind("<Leave>", lambda event, button = self.end_butt: self.end_butt.config(bg="#1f1f1f", fg = "white"))

        self.back1_button = tk.Button(self.root, text = "Powrót do menu", font = ("Aller", 15), bg = "#1f1f1f", fg = 'white', width = 30, height = 3, command = self.back_to_menu_ac)
        self.back1_button.place(relx=0.80, rely = 0.4, anchor = "center")
        self.back1_button.bind("<Enter>", lambda event, button=self.back1_button: self.back1_button.config(bg = "#2f2f2f", fg = "white"))
        self.back1_button.bind("<Leave>", lambda event, button=self.back1_button: self.back1_button.config(bg = "#1f1f1f", fg = 'white'))

    def back_to_menu_ac(self):
        self.canvas.get_tk_widget().place_forget()
        self.end_butt.destroy()
        self.back1_button.destroy()
        self.opti_label.destroy()
        self.menu()

    def end_app(self):
        self.root.destroy()
        del self
        
app = GraphColoringApp()
app.root.mainloop()
