# First Chess Attempt
import numpy as np


def create_empty_bitmap():
    return np.zeros(64, dtype='byte')


class Board:
    def __init__(self):
        self.white_pawn_bitboard = create_empty_bitmap()
        self.white_knight_bitboard = create_empty_bitmap()
        self.white_bishop_bitboard = create_empty_bitmap()
        self.white_rook_bitboard = create_empty_bitmap()
        self.white_queen_bitboard = create_empty_bitmap()
        self.white_king_bitboard = create_empty_bitmap()

        self.black_pawn_bitboard = create_empty_bitmap()
        self.black_knight_bitboard = create_empty_bitmap()
        self.black_bishop_bitboard = create_empty_bitmap()
        self.black_rook_bitboard = create_empty_bitmap()
        self.black_queen_bitboard = create_empty_bitmap()
        self.black_king_bitboard = create_empty_bitmap()
        self.white_board_list = [self.white_pawn_bitboard,
                                 self.white_knight_bitboard,
                                 self.white_bishop_bitboard,
                                 self.white_rook_bitboard,
                                 self.white_queen_bitboard,
                                 self.white_king_bitboard]
        self.black_board_list = [self.black_pawn_bitboard,
                                 self.black_knight_bitboard,
                                 self.black_bishop_bitboard,
                                 self.black_rook_bitboard,
                                 self.black_queen_bitboard,
                                 self.black_king_bitboard]
        self.board_list = [self.white_board_list,
                           self.black_board_list]

        self.init_pieces()

    def init_pieces(self):
        self.white_rook_bitboard[0] = 1
        self.white_rook_bitboard[7] = 1
        self.white_knight_bitboard[1] = 1
        self.white_knight_bitboard[6] = 1
        self.white_bishop_bitboard[2] = 1
        self.white_bishop_bitboard[5] = 1
        self.white_queen_bitboard[3] = 1
        self.white_king_bitboard[4] = 1
        for i in range(8, 16):
            self.white_pawn_bitboard[i] = 1
            self.black_pawn_bitboard[63 - i] = 1
        self.black_rook_bitboard[63] = 1
        self.black_rook_bitboard[56] = 1
        self.black_knight_bitboard[62] = 1
        self.black_knight_bitboard[57] = 1
        self.black_bishop_bitboard[61] = 1
        self.black_bishop_bitboard[58] = 1
        self.black_queen_bitboard[59] = 1
        self.black_king_bitboard[60] = 1



