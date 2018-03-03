#!/usr/bin/lua

function fibonacci(limit)
    a, b = 1, 2
    sum = 0

    while a < limit do
        if a % 2 == 0 then
            sum = sum + a
        end
        a, b = b, a+b
    end

    return sum
end

print(fibonacci(4000000))
