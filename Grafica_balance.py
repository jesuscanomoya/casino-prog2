import matplotlib.pyplot as plt
import sqlite3
import time


# Este fichero se encarga de temas relacionados con el historial monetario

# Creamos la clase que va a almacenar funciones y poder llamarlas desde otros ficheros
class Grafica_balance:

    # graficar_balance se ocupa de graficar un matplotlib a partir de un DNI
    @staticmethod
    def graficar_balance(dni):
        # Coge la base de datos
        conn = sqlite3.connect('hist_bal.db')
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

    # Esta función se encarga de meter datos en la bd para que se puedan usar
    @staticmethod
    def meter_datos_bd(DNI, dinero):
        conn = sqlite3.connect('hist_bal.db')
        cursor = conn.cursor()
        # Mute los valores y mira que no pasé nada
        try:
            cursor.execute('INSERT INTO hist_bal (dni, dinero, tiempo) VALUES (?, ?, ?)',
                           (DNI, dinero, time.time()))
            conn.commit()
            print("Todo sucedió bien")
        except sqlite3.IntegrityError:
            print("Esto no debería pasar")
        except sqlite3.OperationalError as e:
            print("Error operacional:", e)
        finally:
            conn.close()

    # Como dice su título elimina el user en la bd usando DELETE
    @staticmethod
    def eliminar_usuario(DNI):
        conn = sqlite3.connect('hist_bal.db')
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM hist_bal WHERE dni = ?', (DNI,))
            conn.commit()
            print("Usuario dado de baja correctamente.")
        except Exception as e:
            print("Error al dar de baja:", e)
        finally:
            conn.close()


if __name__ == '__main__':
    Grafica_balance.graficar_balance(257)

