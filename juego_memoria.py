import random
import time

class MemoryGame:
    def __init__(self, size=4):
        """Inicializa el juego de memoria con una grid de tamaño size x size"""
        self.size = size
        self.total_cards = size * size
        self.cards = self._generate_cards()
        self.revealed = [[False] * size for _ in range(size)]
        self.matched = [[False] * size for _ in range(size)]
        self.score = 0
        self.attempts = 0

    def _generate_cards(self):
        """Genera pares de números aleatorios para las tarjetas"""
        numbers = list(range(1, self.total_cards // 2 + 1)) * 2
        random.shuffle(numbers)
        grid = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(numbers[i * self.size + j])
            grid.append(row)
        return grid

    def display_board(self):
        """Muestra el tablero del juego"""
        print("\n" + "=" * 30)
        print("  JUEGO DE MEMORIA")
        print("=" * 30)
        print("  ", end="")
        for j in range(self.size):
            print(f"{j}  ", end="")
        print()
        
        for i in range(self.size):
            print(f"{i} ", end="")
            for j in range(self.size):
                if self.matched[i][j]:
                    print(f"✓  ", end="")
                elif self.revealed[i][j]:
                    print(f"{self.cards[i][j]:2} ", end="")
                else:
                    print(f"?  ", end="")
            print()
        print("=" * 30)
        print(f"Puntuación: {self.score} | Intentos: {self.attempts}")
        print("=" * 30 + "\n")

    def reveal_card(self, row, col):
        """Revela una tarjeta en la posición (row, col)"""
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            print("❌ Posición inválida. Intenta de nuevo.")
            return False
        
        if self.matched[row][col]:
            print("⚠️  Esa tarjeta ya fue emparejada.")
            return False
        
        if self.revealed[row][col]:
            print("⚠️  Esa tarjeta ya está revelada.")
            return False
        
        self.revealed[row][col] = True
        return True

    def hide_cards(self, positions):
        """Oculta las tarjetas después de un intento"""
        for row, col in positions:
            self.revealed[row][col] = False

    def play_round(self):
        """Juega una ronda: revela dos tarjetas e intenta emparejarlas"""
        print("Selecciona 2 tarjetas para emparejar.")
        
        positions = []
        for attempt in range(2):
            while True:
                try:
                    pos = input(f"Tarjeta {attempt + 1} (fila col): ").strip().split()
                    if len(pos) != 2:
                        print("❌ Ingresa fila y columna separadas por espacio.")
                        continue
                    row, col = int(pos[0]), int(pos[1])
                    if self.reveal_card(row, col):
                        positions.append((row, col))
                        self.display_board()
                        break
                except ValueError:
                    print("❌ Ingresa números válidos.")

        self.attempts += 1
        
        row1, col1 = positions[0]
        row2, col2 = positions[1]
        
        if self.cards[row1][col1] == self.cards[row2][col2]:
            print("🎉 ¡Excelente! ¡Encontraste un par!")
            self.matched[row1][col1] = True
            self.matched[row2][col2] = True
            self.score += 10
        else:
            print(f"❌ No coinciden: {self.cards[row1][col1]} y {self.cards[row2][col2]}")
            print("Ocultando tarjetas...")
            time.sleep(2)
            self.hide_cards(positions)
        
        self.display_board()

    def is_finished(self):
        """Verifica si el juego ha terminado (todas las tarjetas emparejadas)"""
        for i in range(self.size):
            for j in range(self.size):
                if not self.matched[i][j]:
                    return False
        return True

    def play(self):
        """Inicia el juego completo"""
        print("\n🎮 ¡Bienvenido al JUEGO DE MEMORIA! 🎮")
        print(f"Debes emparejar todas las tarjetas.\n")
        
        self.display_board()
        
        while not self.is_finished():
            self.play_round()
        
        print("🏆 ¡FELICITACIONES! ¡Ganaste el juego! 🏆")
        print(f"Puntuación final: {self.score}")
        print(f"Total de intentos: {self.attempts}\n")

if __name__ == '__main__':
    size = 4  # Grid de 4x4 (16 tarjetas)
    game = MemoryGame(size)
    game.play()