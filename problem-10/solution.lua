#!/usr/bin/lua

function iter_primes(limit)
    local primes = {false}
    local current = 1

    for i=2, limit do
        primes[i] = true
    end

    return function()
        for i=current, limit do
            if primes[i] then
                for j=i*i, limit, i do primes[j] = false end

                primes[i] = false
                current = i
                return i
            end
        end
    end
end

sum = 0
for prime in iter_primes(2000000) do
    sum = sum + prime
end

print(sum)
