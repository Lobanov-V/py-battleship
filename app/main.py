class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
        is_drowned: bool = False
    ) -> None:
        self.start = start
        self.end = end
        self.is_drowned = is_drowned
        self.decks: list[Deck] = []

        row1, col1 = start
        row2, col2 = end

        if row1 == row2:
            left = min(col1, col2)
            right = max(col1, col2)

            for column in range(left, right + 1):
                self.decks.append(Deck(row1, column))

        elif col1 == col2:
            top = min(row1, row2)
            bottom = max(row1, row2)

            for row in range(top, bottom + 1):
                self.decks.append(Deck(row, col1))

    def get_deck(self, row: int, column: int) -> Deck | None:
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck

        return None

    def fire(self, row: int, column: int) -> None:
        deck = self.get_deck(row, column)

        if deck is None:
            return

        deck.is_alive = False

        for current_deck in self.decks:
            if current_deck.is_alive:
                return

        self.is_drowned = True


class Battleship:
    def __init__(
        self,
        ships: list[tuple[tuple[int, int], tuple[int, int]]]
    ) -> None:
        self.field: dict[tuple[int, int], Ship] = {}

        for start, end in ships:
            ship = Ship(start, end)

            for deck in ship.decks:
                self.field[(deck.row, deck.column)] = ship

    def fire(self, location: tuple[int, int]) -> str:
        if location not in self.field:
            return "Miss!"

        row, column = location
        ship = self.field[location]
        ship.fire(row, column)

        if ship.is_drowned:
            return "Sunk!"

        return "Hit!"
