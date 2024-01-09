def print_player_health(player):
    print(f"Hp: {player.hp}")

class Player():
    def __init__(self,hitpoints):
        self.hp = hitpoints

    def hit(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            print("Game Over")
            exit()

player = Player(10)

print_player_health(player)
player.hit(2)
print_player_health(player)
player.hit(4)
print_player_health(player)
player.hit(6)
print_player_health(player)