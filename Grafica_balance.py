import matplotlib.pyplot as plt
import sqlite3


# Este fichero se encarga de temas relacionados con el historial monetario

# Creamos la clase que va a almacenar funciones y poder llamarlas desde otros ficheros
class Grafica_balance:

    # graficar_balance se ocupa de graficar un matplotlib a partir de un DNI
    @staticmethod
    def graficar_balance(dni):
        # Coge la base de datos
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        # Pilla los valores que queremos
        cursor.execute('SELECT dinero FROM hist_bal WHERE dni = ?', (str(dni),))
        # Obtiene la columna
        user = cursor.fetchall()
        a = ([i[0] for i in user])
        print(a)
        conn.close()
        lista_aux = []
        # Crea una lista con su longitud
        for i in range(0, len(a)):
            lista_aux.append(i)
        # Pono las líneas para que se vea mejor
        fig, ax = plt.subplots()
        ax.plot(lista_aux, a)

        # Títulos y demás cosas
        ax.set(xlabel='time (s)', ylabel='Dinero',
               title='Historial crediticio')
        ax.grid()

        # Guarda la imagen para que se pueda utilizar luego
        plt.savefig('Imagenes/hist_bal.png')
        plt.show()


if __name__ == '__main__':
    Grafica_balance.graficar_balance('11111111H')
