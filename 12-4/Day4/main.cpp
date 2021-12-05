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

    std::vector<std::string> boardInput;
    uint32_t rowCount = 0;
    while (std::getline(input_file, line))
    {
        if (line.size() == 0)
        {
            continue;
        }
        boardInput.push_back(line);

        ++rowCount;
        if (rowCount == 5)
        {

            boards.push_back(Board{ boardInput });
            boardInput.clear();
            rowCount = 0;
        }
        
    }
    if (rowCount == 5)
    {
        boards.push_back(Board{ boardInput });
    }
    

    for (const auto bingoNum : bingoNumbers)
    {
        for (auto& board : boards)
        {
            board.CallNumber(bingoNum);
            if (board.CheckBingo())
            {
                std::cout << "Bingo!" << std::endl;
                uint32_t score = board.GetScore();
                std::cout << score << std::endl;
                std::cout << score * bingoNum << std::endl;
                board.ToString();
                return 0;
            }
        }
    }
    
    input_file.close();
}
