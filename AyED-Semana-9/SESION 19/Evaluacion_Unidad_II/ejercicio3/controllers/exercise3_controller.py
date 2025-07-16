from ejercicio3.models.linked_list import LinkedList
from ejercicio3.views.exercise3_view import Exercise3View

class Exercise3Controller:
    def __init__(self):
        self.playlist = LinkedList()
        self.view = Exercise3View()

    def add_song(self, song):
        self.playlist.add_song(song)
        return True

    def remove_song(self, song):
        return self.playlist.remove_song(song)

    def play_next(self):
        return self.playlist.next_song()

    def play_previous(self):
        return self.playlist.previous_song()

    def show_playlist(self):
        return self.playlist.get_playlist()

    def start(self):
        while True:
            self.view.show_menu()
            option = input("Seleccione una opción: ")
            
            if option == "1":
                song = input("Ingrese el nombre de la canción: ")
                self.add_song(song)
                self.view.show_success("Canción agregada exitosamente")
            elif option == "2":
                song = input("Ingrese el nombre de la canción a eliminar: ")
                if self.remove_song(song):
                    self.view.show_success("Canción eliminada exitosamente")
                else:
                    self.view.show_error("Canción no encontrada")
            elif option == "3":
                next_song = self.play_next()
                if next_song:
                    self.view.show_current_song(next_song)
                else:
                    self.view.show_error("No hay más canciones")
            elif option == "4":
                prev_song = self.play_previous()
                if prev_song:
                    self.view.show_current_song(prev_song)
                else:
                    self.view.show_error("No hay canciones anteriores")
            elif option == "5":
                playlist = self.show_playlist()
                self.view.show_playlist(playlist)
            elif option == "6":
                break
            else:
                self.view.show_invalid_option() 