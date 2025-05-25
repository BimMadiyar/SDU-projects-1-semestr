import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class Drink:
    def __init__(self, name, volume, material, is_fizzy, taste, cost, image_path=None, quantity=0):
        self.name = name
        self.volume = volume
        self.material = material
        self.is_fizzy = is_fizzy
        self.taste = taste
        self.cost = cost
        self.quantity = quantity
        self.image_path = image_path  # Path to the drink's image


class DrinkApp:
    def __init__(self):
        self.drinks = {
            'Coke': [
                Drink('Coca Cola', 0.5, 'Glass', 'Yes', 'Normal', 360, 'C:/Users\Мадияр\pythonProject\Vending Machine project\coke_1.jpg'),
                Drink('Coca Cola', 0.5, 'Metallic', 'Yes', 'Normal', 360, 'C:/Users\Мадияр\pythonProject\Vending Machine project\Coke_2.png'),
                Drink('Coca Cola', 1.0, 'Plastic', 'Yes', 'No Sugar', 440, 'C:/Users\Мадияр\pythonProject\Vending Machine project\coke_4.png'),
            ],
            'MaxiTea': [
                Drink('MaxiTea', 0.5, 'Plastic', 'No', 'Lemon', 320, 'C:/Users\Мадияр\pythonProject\Vending Machine project\maxi_tea3.png'),
                Drink('MaxiTea', 1.4, 'Plastic', 'No', 'Strawberry', 450, 'C:/Users\Мадияр\pythonProject\Vending Machine project\maxi_tea4.png'),
                Drink('MaxiTea', 1.4, 'Plastic', 'No', 'Peach', 450, 'C:/Users\Мадияр\pythonProject\Vending Machine project\maxi_tea4.png'),

            ],
            'Water': [
                Drink('Asu', 1.0, 'Plastic', 'Yes', 'No', 310, 'C:/Users\Мадияр\pythonProject\Vending Machine project/asu.png'),
                Drink('Saryagash', 1.5, 'Plastic', 'Yes', 'No', 250, 'C:/Users\Мадияр\pythonProject\Vending Machine project\saryagash.png'),
                Drink('Borjomi', 1.0, 'Glass', 'Yes', 'Medical', 650, 'C:/Users\Мадияр\pythonProject\Vending Machine project/borjomi.png')
            ],
        }

        self.cart = []

    def main_menu(self):
        menu = tk.Tk()
        menu.geometry('750x500+150+25')
        menu.title("Main Menu")
        menu.configure(bg='white')
        menu.resizable(False, False)

        tk.Button(menu, text='<< Exit', width=8, fg='white', bg='black', font=('Arial', 12, 'bold'),
                  command=menu.destroy).place(x=10, y=10)
        tk.Label(menu, text="DRINKS", fg='black', bg='white', font=('Microsoft YaHei UI Light', 35, 'bold')).pack(pady=40)

        categories = ['Coke', 'MaxiTea', 'Water']
        x_positions = [70, 320, 570]
        for i, category in enumerate(categories):
            tk.Label(menu, text=category, fg='black', bg='white', font=('Microsoft YaHei UI Light', 15, 'bold')).place(
                x=x_positions[i], y=140)
            for j, drink in enumerate(self.drinks[category]):
                tk.Button(menu, width=11, text=f"{drink.name}, {drink.volume}L", fg='black', bg='red' if category == 'Coke' else 'yellow',
                          font=('Microsoft YaHei UI Light', 10, 'bold'), command=lambda d=drink: self.view_drink(d)).place(
                    x=x_positions[i], y=190 + j * 50)

        # Add a "View Cart and Buy" button
        tk.Button(menu, text="View Cart and Buy", fg='white', bg='green', font=('Arial', 15, 'bold'),
                  command=self.view_cart).pack(side=tk.BOTTOM, pady=20)

        menu.mainloop()

    def view_drink(self, drink):
        drink_window = tk.Toplevel()
        drink_window.geometry('500x500+250+100')
        drink_window.title(f'{drink.name}, {drink.volume}L')
        drink_window.configure(bg='white')
        drink_window.resizable(False, False)

        tk.Button(drink_window, width=10, text='<< Back', fg='white', bg='black',
                  font=('Microsoft YaHei UI Light', 10, 'bold'), command=drink_window.destroy).place(x=10, y=10)

        details = [
            f'Name: {drink.name}',
            f'Volume: {drink.volume}L',
            f'Bottle: {drink.material}',
            f'Fizzy: {drink.is_fizzy}',
            f'Taste: {drink.taste}',
            f'Cost: {drink.cost}tg',
        ]

        for i, detail in enumerate(details):
            tk.Label(drink_window, text=detail, bg='white', font=('Arial', 17)).place(x=10, y=50 + i * 40)

        # Load and display image
        if drink.image_path:
            try:
                img = Image.open(drink.image_path)
                resized_img = img.resize((250, 250))
                tk_image = ImageTk.PhotoImage(resized_img)
                image_label = tk.Label(drink_window, image=tk_image, bg='white')
                image_label.image = tk_image  # Keep reference to avoid garbage collection
                image_label.place(x=220, y=50)
            except FileNotFoundError:
                tk.Label(drink_window, text='Image not found', bg='white', fg='red', font=('Arial', 15)).place(x=220, y=150)

        tk.Label(drink_window, text='Quantity:', bg='white', font=('Arial', 17)).place(x=10, y=400)
        quantity_entry = tk.Entry(drink_window, bg='white', width=20, border=2, font=('Arial', 15))
        quantity_entry.place(x=105, y=402)

        tk.Button(drink_window, width=15, text='Add to Cart >>', bg='white', font=('Arial', 10, 'bold'),
                  command=lambda: self.add_to_cart(drink, quantity_entry)).place(x=360, y=455)

        drink_window.mainloop()

    def add_to_cart(self, drink, quantity_entry):
        try:
            quantity = int(quantity_entry.get())
            drink.quantity += quantity
            self.cart.append(drink)
            messagebox.showinfo('Success', f'Added {quantity} of {drink.name} to the cart!')
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid quantity.')

    def view_cart(self):
        cart_window = tk.Toplevel()
        cart_window.geometry('500x500+250+100')
        cart_window.title("Cart")
        cart_window.configure(bg='white')
        cart_window.resizable(False, False)

        tk.Label(cart_window, text="Your Cart", fg='black', bg='white', font=('Arial', 20, 'bold')).pack(pady=10)

        total_cost = 0
        y_position = 60
        for drink in self.cart:
            if drink.quantity > 0:
                tk.Label(cart_window,
                         text=f"{drink.name} ({drink.volume}L): {drink.quantity} pcs - {drink.cost * drink.quantity}tg",
                         bg='white', font=('Arial', 12)).place(x=10, y=y_position)
                total_cost += drink.cost * drink.quantity
                y_position += 30

        tk.Label(cart_window, text=f"Total Cost: {total_cost}tg", fg='black', bg='white',
                 font=('Arial', 15, 'bold')).pack(pady=20)

        tk.Button(cart_window, text="Buy", fg='white', bg='green', font=('Arial', 15, 'bold'),
                  command=lambda: self.buy(cart_window)).pack(side=tk.BOTTOM, pady=20)

    def buy(self, cart_window):
        if self.cart:
            for drink in self.cart:
                drink.quantity = 0
            self.cart.clear()
            messagebox.showinfo("Success", "Purchase completed successfully!")
            cart_window.destroy()
        else:
            messagebox.showerror("Error", "Your cart is empty.")


if __name__ == '__main__':
    app = DrinkApp()
    app.main_menu()
