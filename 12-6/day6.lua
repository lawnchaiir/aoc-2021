
local f = io.open("input.txt", "r")

local data = f:read()
f:close()

local lanternFish = {}
for n in data:gmatch("%d+") do
    table.insert(lanternFish, tonumber(n))
end

local fishCounts = {}
-- use more sensible table indexing
for i = 0, 8 do
    fishCounts[i] = 0
end

for k, v in ipairs(lanternFish) do
    fishCounts[v] = fishCounts[v] + 1
end

local days = 256
for day = 1, days do
    local readyFish = fishCounts[0]
    for i = 0, 8 do
        fishCounts[i] = fishCounts[i + 1]
    end

    -- each fish that was at day 0 will have another fish, so start them up at day 8
    fishCounts[8] = readyFish

    -- all of our day 0 fish now move back to day 6
    fishCounts[6] = readyFish + fishCounts[6]
end

local sum = 0
for k,v in pairs(fishCounts) do
    sum = sum + v
end

print(sum)