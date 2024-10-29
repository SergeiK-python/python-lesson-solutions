# Домашнее задание по теме "Режимы открытия файлов"
import os

class Product:
    def __init__(self, name: str, weight: float or str, category: str):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def from_str(self, sources: str):
        sources = sources.replace('\n','').split(',')
        return Product(*sources)



class Shop:
    __file_name = 'products.txt'
    __with_appended = False  # as another shop's option (control for added products), in the task use False

    def get_products(self):
        database = ''
        if os.path.isfile(Shop.__file_name):
            file =  open(Shop.__file_name, 'r')
            database = file.read()
            file.close()
        return database

    def add(self, *products):
        existed = self.get_products().split('\n')
        existed.remove('')
        existed = [*existed]
        for product in products:
            if isinstance(product, Product):
                if self._contains(product, existed):
                    print(f'Продукт {product.name if Shop.__with_appended else product} уже есть в магазине')
                else:
                    file = open(Shop.__file_name, 'a')
                    out = str(product)
                    file.write(out + '\n')
                    file.close()
                    if Shop.__with_appended:
                        existed.append(out)  # to evaluate also right now added products after

    def _contains(self, product: Product, products) -> bool:
        for _product in products:
            if _product != '':
                another_product = product.from_str(_product)
                if another_product.name == product.name:
                    return True
        return False




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

#print(p4 := p3.from_str('Potato,5.5,Vegetables\n'))