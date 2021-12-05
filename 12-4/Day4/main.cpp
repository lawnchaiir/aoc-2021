#include "stdafx.h"

#include <fstream>

#include "Board.h"


int main()
{
    std::string filename("..\\input.txt");
    std::string line;

    std::ifstream input_file(filename);

    std::string bingoNumbersInput;

    if (std::getline(input_file, line))
    {
        bingoNumbersInput = line;
    }

    std::vector<uint32_t> bingoNumbers;

    {
        std::string buffer;
        std::stringstream ss(bingoNumbersInput);
        while (std::getline(ss, buffer, ',') && buffer.size() != 0)
        {
            uint32_t bingoNum = std::stoi(buffer);
            bingoNumbers.push_back(bingoNum);
        }
    }

    std::vector<Board> boards;
    boards.reserve(10);

    std::vector<std::string> boardInput;
    boardInput.reserve(Board::cBoardSize);

    uint32_t rowCount = 0;
    while (std::getline(input_file, line))
    {
        if (line.size() == 0)
        {
            continue;
        }
        boardInput.push_back(line);

        ++rowCount;
        if (rowCount == Board::cBoardSize)
        {
            boards.push_back(Board{ boardInput });
            boardInput.clear();
            rowCount = 0;
        }
    }

    input_file.close();

    if (rowCount == Board::cBoardSize)
    {
        boards.push_back(Board{ boardInput });
    }

    for (const auto bingoNum : bingoNumbers)
    {
        for (auto& board : boards)
        {
            // Part 2 Adjustment. 
            if (board.Won())
            {
                continue;
            }

            board.CallNumber(bingoNum);
            if (board.CheckBingo())
            {
                uint32_t score = board.GetScore();
                std::string output;
                output.append("Bingo\n");
                output.append(std::to_string(score)).append("\n");
                output.append(std::to_string(score * bingoNum)).append("\n");
                output.append(board.ToString()).append("\n");
                std::cout << output;
            }
        }
    }        
}
