#pragma once


class Board
{
public:
    Board(std::vector<std::string> input);

    void ToString();

    void CallNumber(uint32_t num);
    bool CheckBingo() const;
    uint32_t GetScore() const;

private:
    static constexpr uint32_t cBoardSize = 5;
    uint32_t board[cBoardSize][cBoardSize];
    
    bool matches[cBoardSize][cBoardSize];
};