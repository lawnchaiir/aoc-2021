
local f = io.open("input.txt", "r")

local data = f:read()
f:close()

local lanternFish = {}
for n in data:gmatch("%d+") do
    table.insert(lanternFish, n)
end

local days = 18

local fishCount = 0


--print(table.concat(lanternFish, ","))
for day = 0, days - 1 do
    for k, fish in pairs(lanternFish) do
        if fish == 0 then
            fish = 6
            lanternFish[k] = fish
            table.insert(lanternFish, 9) -- The rules say add an 8 and then skip a day ... or we could add 9
        else
            fish = fish - 1
            lanternFish[k] = fish
        end
    end
    --print(table.concat(lanternFish, ","))
end

print(#lanternFish)