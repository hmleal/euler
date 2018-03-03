#!/usr/bin/lua

sum = 0
for i=0, 1000 do
    if i % 3 == 0 or i % 5 == 0 then
        sum = sum + i
    end
end

print(sum)
