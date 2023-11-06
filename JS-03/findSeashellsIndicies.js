// Time complexity -> O(n), Space complexity -> 0(n)
const findSeashellsIndices = (target, values) => {
    const map = new Map()


    for (let i = 0; i < values.length; i++) {
        map.set(values[i], i)

        // Check if map contains (target - value), if it does we also need to make sure it's not the same index.
        if (map.has(target - values[i]) && i !== map.get(target - values[i])) {
            return [map.get(target - values[i]), i]
        }
    }
    return []
}