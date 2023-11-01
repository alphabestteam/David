//A better way of doing this would be using a Map to contain everything, then go over the array once
// to check if currValue - target is in the map. This would lead to time and space complexity -> O(n)
const findSeashellsIndicies = (target, values) => {
    for (let i = 0; i < values.length; i++) {
        for (let j = 0; j < values.length; j++) {
            if (values[i] + values[j] === target) {
                if (i === j) continue  //make sure they aren't the same index.
                return [i, j]
            }
        }
    }
    return []
}