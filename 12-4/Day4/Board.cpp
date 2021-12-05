#include "stdafx.h"
#include "Board.h"


Board::Board(std::vector<std::string> input)
{
    uint32_t row = 0;
    uint32_t col = 0;

    std::string buffer;
    for (const auto rowString : input)
    {
        std::stringstream ss(rowString);
        while (std::getline(ss, buffer, ' ') )
        {
            if (buffer.size() == 0)
            {
                continue;
            }
            uint32_t boardValue = std::stoi(buffer);
            m_board[row][col] = boardValue;
            col = (col + 1) % cBoardSize;
        }
        row = (row + 1) % cBoardSize;
    }
}

void Board::ToString()
{
    uint32_t row = 0;
    uint32_t col = 0;

    std::cout << "----------" << std::endl;
    for (uint32_t i = 0; i < cBoardSize; ++i)
    {
        std::cout << "[";
        for (uint32_t j = 0; j < cBoardSize; ++j)
        {
            std::cout << m_board[row][col];
            if (m_matches[row][col])
            {
                std::cout << "*";
            }
            std::cout << ",";

            col = (col + 1) % cBoardSize;
        }
        std::cout << "]" << std::endl;
        row = (row + 1) % cBoardSize;
    }
    std::cout << "----------" << std::endl;
}

void Board::CallNumber(uint32_t num)
{
    uint32_t row = 0;
    uint32_t col = 0;
    for (uint32_t i = 0; i < cBoardSize; ++i)
    {
        for (uint32_t j = 0; j < cBoardSize; ++j)
        {
            if (m_board[row][col] == num)
            {
                m_matches[row][col] = true;
                return;

            }
            col = (col + 1) % cBoardSize;
        }

        row = (row + 1) % cBoardSize;
    }
}

bool Board::CheckBingo()
{
    uint32_t row = 0;
    uint32_t col = 0;


    uint32_t row2 = 0;
    uint32_t col2 = 0;

    for (uint32_t i = 0; i < cBoardSize; ++i)
    {
        bool fullRow = true;
        bool fullCol = true;
        for (uint32_t j = 0; j < cBoardSize; ++j)
        {
            if (!m_matches[row][col])
            {
                fullRow = false;
            }

            if (!m_matches[row2][col2])
            {
                fullCol = false;
            }
            col = (col + 1) % cBoardSize;
            row2 = (row2 + 1) % cBoardSize;
        }

        if (fullRow || fullCol)
        {
            m_won = true;
            return true;
        }

        col2 = (col2 + 1) % cBoardSize;
        row = (row + 1) % cBoardSize;
    }


    return false;
}

uint32_t Board::GetScore() const
{
    uint32_t row = 0;
    uint32_t col = 0;
    uint32_t sum = 0;
    for (uint32_t i = 0; i < cBoardSize; ++i)
    {
        for (uint32_t j = 0; j < cBoardSize; ++j)
        {
            if (!m_matches[row][col])
            {
                sum += m_board[row][col];
            }
            col = (col + 1) % cBoardSize;
        }

        row = (row + 1) % cBoardSize;
    }
    return sum;
}
