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

    std::string ToString();

    void CallNumber(uint32_t num);
    bool CheckBingo();
    uint32_t GetScore() const;

    bool Won() const { return m_won; }
    
    static constexpr uint32_t cBoardSize = 5;
private:
    
    uint32_t m_board[cBoardSize][cBoardSize] = { false };
    bool m_matches[cBoardSize][cBoardSize] = { false };

    bool m_won = false;
};