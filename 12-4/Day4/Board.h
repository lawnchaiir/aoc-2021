#pragma once


class Board
{
public:
    Board(std::vector<std::string> input);
    Board(const Board&) = delete;
    Board(const Board&&) = delete;
    Board& operator=(Board&) = delete;
    Board& operator=(Board&&) = delete;
    ~Board() = default;

    std::string ToString() const;

    void CallNumber(uint32_t num);
    bool CheckBingo();
    uint32_t GetScore() const;

    bool Won() const { return m_won; }
    
    static constexpr uint32_t cBoardSize = 5;
private:
 
    static uint32_t GetBitIndex(uint32_t row, uint32_t col);

    bool HasMatch(uint32_t row, uint32_t col) const;

    uint32_t m_board[cBoardSize][cBoardSize] = { false };
    uint32_t m_matchesFlag = 0;

    bool m_won = false;
};
