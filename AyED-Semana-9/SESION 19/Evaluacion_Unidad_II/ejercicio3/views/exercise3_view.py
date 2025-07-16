class Exercise3View:
    def show_menu(self):
        print("\n=== EJERCICIO 3: LISTA DE REPRODUCCIÓN ===")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente canción")
        print("4. Reproducir canción anterior")
        print("5. Mostrar lista de reproducción")
        print("6. Volver al menú principal")

    def show_success(self, message):
        print(f"\n✓ {message}")

    def show_error(self, message):
        print(f"\n✗ {message}")

    def show_current_song(self, song):
        print(f"\nReproduciendo: {song}")

    def show_playlist(self, playlist):
        print("\nLista de reproducción actual:")
        if not playlist:
            print("La lista está vacía")
        else:
            for i, song in enumerate(playlist, 1):
                print(f"{i}. {song}")

    def show_invalid_option(self):
        print("Opción no válida. Por favor, intente de nuevo.") 