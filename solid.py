#1
class  User:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, user: User):
        passre

#2
class User:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass

class UserDB:
    def get_user(self, id) -> User:
        pass

    def save(self, user: User):
        pass

#3
class Discount:
  def __init__(self, customer, price):
      self.customer = customer
      self.price = price
  def give_discount(self):
      if self.customer == 'fav':
          return self.price * 0.2
      if self.customer == 'vip':
          return self.price * 0.4

#4
class Discount:
    def __init__(self, customer, price):
      self.customer = customer
      self.price = price
    def get_discount(self):
      return self.price * 0.2
class VIPDiscount(Discount):
    def get_discount(self):
      return super().get_discount() * 2

#5
class User():
  def __init__(self, color, board):
    create_pieces()
    self.color = color
    self.board = board
  def move(self, piece:Piece, position:int):
      piece.move(position)
      chessmate_check()
  board = ChessBoard()
  user_white = User("white", board)
  user_black = User("black", board)
  pieces = user_white.pieces
  horse = helper.getHorse(user_white, 1)
  user.move(horse)

