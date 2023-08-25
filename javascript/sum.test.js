
import sum from './sum.js'


test('add normal flow', () => {
    expect(sum(1,4)).toBe(5)
})

test('test adge case', () => {
    expect(sum(1, 0)).toBe(1)
})