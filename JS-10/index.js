const bobsMap = new Map()

bobsMap.set('Main character', 'spongebob');
bobsMap.set('Best friend', 'patrick');
bobsMap.set('pet', 'gary');
bobsMap.set('word buddy', 'squidward');
bobsMap.set('manager', 'Mr. Krabs');
bobsMap.set('teacher', 'Mrs. Puff');
bobsMap.set('location', 'bikini bottom');


console.log(bobsMap)
console.log(Array.from(bobsMap.keys()))

console.log(bobsMap.get('location'))
console.log(bobsMap.size)

bobsMap.delete('location')

console.log(bobsMap.size)
console.log(bobsMap)
console.log(bobsMap.has('location'))
